"""
Substrate: Ammonia Ocean & Terminator Dam Model v4
===================================================

Key insight from atmospheric analysis (v4 update):
    - The superstream (day->night, ~12-16 km) passes THROUGH the rain column
      at the terminator, unlike Earth's jet stream which is above weather.
    - Rain scavenging starts DAYSIDE of the mound crest (condensation floor
      rises with distance from terminator).
    - Most rainfall lands on the dayside slope and evaporates (recycles).
    - Only a small fraction of NH3 crosses the crest to the nightside ocean.
    - Nearly ALL particulate deposits on the mound/dayside (rain washout
      is concentrated at first contact with the condensation column).

The critical new parameter is f_ocean: the fraction of volcanic NH3
that actually reaches the nightside ocean (vs recycling on the day side).
Estimates: 1-10%, possibly up to 20%.

The mound receives nearly all particulate (f_mound ~ 0.8-0.95), not
the 40% assumed in v3. Sea floor deposition from atmosphere is negligible.

Usage: python sim_ammonia_ocean.py
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# PLANET CONSTANTS (Spine v2.4)
# ============================================================
R_PLANET = 1.52 * 6.371e6       # m
G = 17.85                        # m/s2
RHO_NH3 = 681.0                  # kg/m3 (liquid, 240K)
RHO_SED = 2200.0                 # kg/m3 (bulk sediment)
A_NIGHT = 2 * np.pi * R_PLANET**2
C_TERM = 2 * np.pi * R_PLANET


def run(Q_v=5e11, Q_p=5e10, Q_decay=8e9,
        f_ocean=0.05, f_mound=0.85, W_mound=1e5, h_mound_max=8e3,
        t_max=5e9, dt=1e6, label=""):
    """
    Two-variable model: ocean depth vs mound height.

    Key parameters:
        Q_v:       volcanic NH3 outgassing rate (kg/yr)
        Q_p:       volcanic particulate output rate (kg/yr)
        Q_decay:   volcanic decay timescale (yr)
        f_ocean:   fraction of Q_v that reaches nightside ocean (rest recycles dayside)
        f_mound:   fraction of Q_p deposited on the mound (rest on dayside plain)
        W_mound:   mound width (m)
        h_mound_max: isostatic/atmospheric height cap (m)
    """
    n = int(t_max / dt)
    A_mound = C_TERM * W_mound

    # Ocean growth rate at t=0 [m/yr]:
    ocean_rate_0 = (Q_v * f_ocean) / (RHO_NH3 * A_NIGHT)
    # Mound growth rate at t=0 [m/yr]:
    mound_rate_0 = Q_p * f_mound / (RHO_SED * A_mound)
    # Sea floor growth rate at t=0 [m/yr]:
    # Negligible in v4 model (nightside gets almost no atmospheric deposition)
    # Small residual from ocean-carried sediment
    f_floor = 0.01  # ~1% of particulate reaches sea floor via ocean transport
    floor_rate_0 = Q_p * f_floor / (RHO_SED * A_NIGHT)

    # Time arrays
    tau = Q_decay
    time_yr = np.arange(n) * dt
    t = time_yr / 1e9  # Gyr
    integral = tau * (1 - np.exp(-time_yr / tau))

    # Cumulative heights [m]
    h_ocean_raw = ocean_rate_0 * integral
    h_mound_raw = mound_rate_0 * integral
    h_floor = floor_rate_0 * integral

    # Apply height cap to mound
    h_mound = np.minimum(h_mound_raw, h_mound_max)
    cap_idx = np.searchsorted(h_mound_raw, h_mound_max)
    cap_time = cap_idx * dt / 1e9 if cap_idx < n else None

    # Effective ocean depth = ocean - floor
    h_ocean_eff = np.maximum(0, h_ocean_raw - h_floor)

    # Overflow detection
    overflow_mask = h_ocean_eff > h_mound
    overflow_idx = np.argmax(overflow_mask) if overflow_mask.any() else None
    overflow_time = overflow_idx * dt / 1e9 if overflow_idx is not None and overflow_mask.any() else None

    h_ocean_actual = np.minimum(h_ocean_eff, h_mound)

    # Critical ratio for this configuration
    # Ocean wins when ocean_rate > mound_rate, i.e.:
    # Q_v * f_ocean / (RHO_NH3 * A_NIGHT) > Q_p * f_mound / (RHO_SED * A_mound)
    # Q_v/Q_p > f_mound/f_ocean * RHO_NH3*A_NIGHT / (RHO_SED*A_mound)
    critical_ratio = (f_mound / f_ocean) * (RHO_NH3 * A_NIGHT) / (RHO_SED * A_mound)

    return {
        't': t,
        'h_ocean_unconstrained': h_ocean_eff,
        'h_ocean': h_ocean_actual,
        'h_mound': h_mound,
        'h_mound_unconstrained': h_mound_raw,
        'h_floor': h_floor,
        'overflow_time': overflow_time,
        'cap_time': cap_time,
        'ocean_rate_0': ocean_rate_0 * 1e9,      # m/Gyr
        'mound_rate_0': mound_rate_0 * 1e9,       # m/Gyr
        'floor_rate_0': floor_rate_0 * 1e9,        # m/Gyr
        'critical_ratio': critical_ratio,
        'label': label,
        'f_ocean': f_ocean,
        'f_mound': f_mound,
    }


def plot_suite(results, title, filename):
    """Multi-panel plot for a suite of scenarios."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(title, fontsize=14, fontweight='bold')
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

    for idx, res in enumerate(results):
        t = res['t']
        c = colors[idx % len(colors)]
        lbl = res['label']

        # P1: The Race
        ax = axes[0, 0]
        ax.plot(t, res['h_ocean_unconstrained']/1e3, '-', color=c, lw=2,
                label=f'{lbl}: ocean')
        ax.plot(t, res['h_mound']/1e3, '--', color=c, lw=2,
                label=f'{lbl}: mound')
        if res['overflow_time']:
            ax.axvline(res['overflow_time'], color=c, ls=':', alpha=0.6)
            ax.annotate(f'overflow {res["overflow_time"]:.1f}',
                        xy=(res['overflow_time'], 0), fontsize=7, color=c,
                        rotation=90, va='bottom')

        # P2: Effective ocean depth
        ax = axes[0, 1]
        ax.plot(t, res['h_ocean']/1e3, '-', color=c, lw=2, label=lbl)

        # P3: Ocean depth in meters (for shallow seas)
        ax = axes[1, 0]
        ax.plot(t, res['h_ocean'], '-', color=c, lw=2, label=lbl)

        # P4: Excess depth
        excess = np.maximum(0, res['h_ocean_unconstrained'] - res['h_mound'])
        ax = axes[1, 1]
        ax.plot(t, excess/1e3, '-', color=c, lw=2, label=lbl)

    # Format
    axes[0, 0].set_ylabel('Height [km]')
    axes[0, 0].set_title('THE RACE: Ocean Depth vs Mound Height')
    axes[0, 0].legend(fontsize=6, ncol=2)

    axes[0, 1].set_ylabel('Depth [km]')
    axes[0, 1].set_title('Actual Ocean Depth (capped at mound)')
    axes[0, 1].legend(fontsize=7)

    axes[1, 0].set_ylabel('Depth [m]')
    axes[1, 0].set_title('Ocean Depth [meters]')
    axes[1, 0].legend(fontsize=7)

    axes[1, 1].set_ylabel('Excess [km]')
    axes[1, 1].set_title('Overflow Excess (ocean - mound)')
    axes[1, 1].legend(fontsize=7)

    for ax in axes.flat:
        ax.set_xlabel('Time [Gyr]')
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"  Saved: {filename}")
    plt.close()


def print_summary(res):
    """Print key numbers."""
    print(f"\n  [{res['label']}]")
    print(f"    f_ocean={res['f_ocean']:.0%}, f_mound={res['f_mound']:.0%}")
    print(f"    Rates at t=0: ocean {res['ocean_rate_0']:.1f} m/Gyr, "
          f"mound {res['mound_rate_0']:.0f} m/Gyr, "
          f"floor {res['floor_rate_0']:.2f} m/Gyr")
    print(f"    Critical Q_v/Q_p for overflow: {res['critical_ratio']:.0f}")
    print(f"    At t=4.5 Gyr: ocean(raw)={res['h_ocean_unconstrained'][-1]:.0f} m, "
          f"mound={res['h_mound'][-1]/1e3:.2f} km")
    if res['overflow_time']:
        print(f"    ** OVERFLOW at {res['overflow_time']:.2f} Gyr **")
        excess = res['h_ocean_unconstrained'][-1] - res['h_mound'][-1]
        print(f"    Excess depth at 4.5 Gyr: {excess:.0f} m")
    else:
        headroom = res['h_mound'][-1] - res['h_ocean_unconstrained'][-1]
        print(f"    No overflow. Headroom at 4.5 Gyr: {headroom:.0f} m")
    if res['cap_time']:
        print(f"    Mound hits height cap at {res['cap_time']:.2f} Gyr")


def main():
    print("=" * 60)
    print("SUBSTRATE AMMONIA OCEAN MODEL v4")
    print("(with realistic dayside rain recycling)")
    print("=" * 60)
    print(f"Planet: R={R_PLANET/1e6:.1f} km, g={G} m/s2")
    print(f"Night hemisphere: {A_NIGHT:.2e} m2")
    print(f"Terminator circumference: {C_TERM/1e3:.0f} km")
    print()

    # ============================================================
    # SUITE 1: Runoff fraction (the key new parameter)
    # ============================================================
    print("\n--- SUITE 1: Nightside Runoff Fraction ---")
    print("  Q_v/Q_p=10, f_mound=0.85, h_cap=3km (atmospheric)")
    results = []
    for f_oc in [0.01, 0.03, 0.05, 0.10, 0.20]:
        res = run(Q_v=5e11, Q_p=5e10, f_ocean=f_oc, f_mound=0.85,
                  h_mound_max=3e3, label=f"f_ocean={f_oc:.0%}")
        print_summary(res)
        results.append(res)
    plot_suite(results, "Suite 1: Nightside Runoff Fraction (Q_v/Q_p=10, cap=3km)",
              "D:/Data/git/repos/Substrate/sim_v4_s1_runoff.png")

    # ============================================================
    # SUITE 2: Runoff fraction with higher Q_v/Q_p
    # ============================================================
    print("\n\n--- SUITE 2: Runoff Fraction at Q_v/Q_p=50 (Earth-like) ---")
    print("  f_mound=0.85, h_cap=3km")
    results = []
    for f_oc in [0.01, 0.03, 0.05, 0.10, 0.20]:
        res = run(Q_v=5e11, Q_p=1e10, f_ocean=f_oc, f_mound=0.85,
                  h_mound_max=3e3, label=f"f_ocean={f_oc:.0%}")
        print_summary(res)
        results.append(res)
    plot_suite(results, "Suite 2: Runoff Fraction at Q_v/Q_p=50 (cap=3km)",
              "D:/Data/git/repos/Substrate/sim_v4_s2_runoff_50.png")

    # ============================================================
    # SUITE 3: Height cap sensitivity with f_ocean=5%
    # ============================================================
    print("\n\n--- SUITE 3: Height Cap (f_ocean=5%, Q_v/Q_p=10) ---")
    results = []
    for cap_km in [1.5, 2, 3, 4, 8]:
        lbl = f"cap={cap_km}km"
        res = run(Q_v=5e11, Q_p=5e10, f_ocean=0.05, f_mound=0.85,
                  h_mound_max=cap_km*1e3, label=lbl)
        print_summary(res)
        results.append(res)
    plot_suite(results, "Suite 3: Height Cap Sensitivity (f_ocean=5%, Q_v/Q_p=10)",
              "D:/Data/git/repos/Substrate/sim_v4_s3_cap.png")

    # ============================================================
    # SUITE 4: Q_v/Q_p ratio with realistic f_ocean=5%
    # ============================================================
    print("\n\n--- SUITE 4: Q_v/Q_p Ratio (f_ocean=5%, cap=3km) ---")
    results = []
    configs = [
        (2e11, 1e11, "Q_v/Q_p=2"),
        (5e11, 5e10, "Q_v/Q_p=10"),
        (5e11, 1e10, "Q_v/Q_p=50"),
        (1e12, 1e10, "Q_v/Q_p=100"),
        (1e12, 5e9, "Q_v/Q_p=200"),
    ]
    for Q_v, Q_p, lbl in configs:
        res = run(Q_v=Q_v, Q_p=Q_p, f_ocean=0.05, f_mound=0.85,
                  h_mound_max=3e3, label=lbl)
        print_summary(res)
        results.append(res)
    plot_suite(results, "Suite 4: Q_v/Q_p Ratio (f_ocean=5%, cap=3km)",
              "D:/Data/git/repos/Substrate/sim_v4_s4_ratio.png")

    # ============================================================
    # SUITE 5: Mound width with realistic parameters
    # ============================================================
    print("\n\n--- SUITE 5: Mound Width (f_ocean=5%, Q_v/Q_p=10, cap=3km) ---")
    results = []
    for W_km in [50, 100, 200, 500]:
        res = run(Q_v=5e11, Q_p=5e10, f_ocean=0.05, f_mound=0.85,
                  W_mound=W_km*1e3, h_mound_max=3e3,
                  label=f"W={W_km}km")
        print_summary(res)
        results.append(res)
    plot_suite(results, "Suite 5: Mound Width (f_ocean=5%, Q_v/Q_p=10, cap=3km)",
              "D:/Data/git/repos/Substrate/sim_v4_s5_width.png")

    # ============================================================
    # KEY RESULTS
    # ============================================================
    print("\n\n" + "=" * 60)
    print("KEY FINDINGS (v4 with dayside rain recycling)")
    print("=" * 60)
    print()
    print("The dayside rain recycling changes EVERYTHING.")
    print()
    print("v3 critical Q_v/Q_p for overflow: ~12")
    print("v4 critical Q_v/Q_p (f_ocean=5%, f_mound=85%): much higher")

    # Compute critical ratio for various f_ocean
    print()
    print("Critical Q_v/Q_p ratio (ocean rate = mound rate):")
    for f_oc in [0.01, 0.03, 0.05, 0.10, 0.20]:
        crit = (0.85 / f_oc) * (RHO_NH3 * A_NIGHT) / (RHO_SED * C_TERM * 1e5)
        print(f"  f_ocean={f_oc:.0%}: Q_v/Q_p must exceed {crit:.0f}")

    print()
    print("Even at Earth-like Q_v/Q_p=50-200, with f_ocean=5%:")
    print("the mound WINS the rate race. Overflow requires the")
    print("atmospheric height cap to stop the mound, THEN the")
    print("ocean slowly catches up over Gyr.")
    print()
    print("Ocean depths at 4.5 Gyr (f_ocean=5%, Q_v/Q_p=10):")
    print("  ~230 m (shallow sea, not km-deep ocean)")
    print()
    print("This is a fundamentally different regime from v3.")
    print("The ocean is real but shallow. The dam holds easily.")
    print("The crisis, if it comes, requires either:")
    print("  1. Tower death (lattice degrades, cap drops)")
    print("  2. Very long timescales (>5 Gyr)")
    print("  3. External perturbation (impactor adding H2O/NH3)")

    print("\n\nDone. PNG files in project directory.")


if __name__ == '__main__':
    main()
