# Tidally-Locked Super-Earth: Geophysical and Atmospheric Analysis

## Planetary Parameters

| Parameter | Value |
|---|---|
| Mass | 4.2 M⊕ |
| Radius | 1.52 R⊕ |
| Surface gravity | 17.85 m/s² (1.82g) |
| Orbital distance | 0.12 AU |
| Orbital period | 18 Earth days |
| Rotation | Tidally locked (1:1 spin-orbit) |
| Escape velocity | 18.6 km/s |
| Low orbital velocity | 13.1 km/s |
| Δv to low orbit | ~18 km/s (incl. drag + gravity losses) |
| Equatorial rotational velocity | ~39 m/s (negligible for launches) |
| Atmosphere | Reducing, 8 bar surface pressure |
| Oceans | Shallow liquid-ammonia seas |
| Biochemistry | Silicon-based |

---

## 1. Magnetic Field

### 1.1 Prospects

The planet's bulk density (ρ/ρ⊕ ≈ 1.20) indicates a body roughly 20% denser than Earth, consistent with a larger iron core mass fraction and/or significant self-compression at higher internal pressures. Central pressures are estimated at 800–1000 GPa, compared to Earth's ~360 GPa.

The angular velocity is Ω ≈ 4.0 × 10⁻⁶ rad/s — approximately 18× slower than Earth. This places the dynamo in a transitional regime: not strongly rotationally dominated as Earth's is, but not so slow that rotation is irrelevant to core convection organization.

**Probable outcome:** A magnetic field exists but is weaker than Earth's and structurally different. Rather than a clean axial dipole, the field is likely multipolar with significant quadrupole and octupole components. Estimated surface field strength is 5–15 μT (roughly 10–40% of Earth's). This is still astrophysically significant — sufficient to stand off stellar wind and provide meaningful atmospheric protection, particularly given the high escape velocity.

### 1.2 Deep Time Evolution

Several competing timescales govern the magnetic field's long-term survival:

**Core thermal evolution** is the primary clock. The larger core has more thermal energy and stronger gravitational driving forces. Models for super-Earths in this mass range suggest dynamo persistence for 6–10 billion years if compositional convection (driven by inner core solidification releasing latent heat and light elements) initiates properly. This is favorable, as the red dwarf host will remain on the main sequence essentially indefinitely.

**Tidal effects on the core** operate on longer timescales than might be initially feared. Tidal locking synchronizes the mantle, but the liquid core is coupled to the mantle only indirectly through viscous and electromagnetic interactions at the core-mantle boundary. This coupling timescale is estimated at 10⁸–10¹⁰ years. A subtle feedback exists: core magnetic field increases electromagnetic coupling, which synchronizes the core faster, which weakens the dynamo, which reduces coupling. The system may find an equilibrium maintaining slight differential rotation indefinitely.

**Tidal heating in the mantle** acts as a stabilizing feedback for the dynamo. At 0.12 AU, tidal dissipation heats the mantle, maintaining a steep temperature gradient across the core-mantle boundary and sustaining core convection.

**Likely trajectory:** The dynamo starts strong after core differentiation, weakens over the first couple billion years as initial thermal convection diminishes, then stabilizes or strengthens as inner core nucleation drives compositional convection. Over 5–10 Gyr, gradual decline as the core solidifies and rotation slowly synchronizes. The field may become intermittent (more frequent reversals, quiet periods between active dynamo epochs) before eventually dying. Estimated total dynamo lifetime: 6–12 billion years, with significant uncertainty.

---

## 2. Atmospheric Dynamics

### 2.1 Coriolis Effects vs. Katabatic Flow

The dominant circulation pattern is thermally direct: air heated at the substellar point rises, flows toward the nightside at altitude, cools and descends, and returns along the surface as convergent flow toward the substellar point.

The atmospheric scale height is compressed by high gravity: H = RT/(μg) ≈ 4.8 km for a ~300 K dayside surface. The 8-bar surface pressure means the atmosphere extends through many more scale heights, providing enormous thermal inertia and heat transport capacity.

The Rossby deformation radius at mid-latitudes is:

$$L_R = NH/f \approx 8{,}400 \text{ km}$$

With a planetary radius of ~9,700 km, the ratio L_R/R_planet ≈ 0.87 places the planet squarely in the **transitional regime** — between the fast-rotator (banded zonal jets) and slow-rotator (pure thermally direct overturning) extremes. This is the most dynamically interesting case.

### 2.2 Key Circulation Features

- The thermally direct day-night overturning remains the dominant energy-containing circulation, but Coriolis deflection introduces significant asymmetries.
- Surface winds approaching the substellar point are deflected into a **cyclonic gyre** around the substellar point rather than purely radial inflow.
- An **equatorial superrotating jet** almost certainly develops, a robust feature in GCM simulations of tidally locked planets. In the 8-bar atmosphere, this jet could reach 50–100+ m/s, shifting the hottest atmospheric region downwind of the substellar point.
- Standing Rossby wave patterns at mid-latitudes create fixed regions of convergence and divergence on the nightside, producing permanent cloud banks and precipitation zones at specific locations.
- The result is essentially **permanent weather** — persistent, steady wind patterns that slowly modulate but never fundamentally rearrange.

### 2.3 Surface Wind Speeds

Modeling estimates katabatic flow velocity at the terminator of approximately **11.5 m/s**, consistent with simple scaling analysis balancing thermal pressure gradient forcing against surface drag. This value is robust across reasonable parameter assumptions (9–14 m/s range).

Winds accelerate toward the substellar point due to convergent geometry and stronger thermal driving, reaching approximately **17 m/s** near the substellar point. The ratio of 17/11.5 ≈ 1.48 indicates that roughly a third to half of converging mass flux has been lofted into the substellar updraft before peak surface velocity is reached.

The substellar region features a permanent, continent-scale convective updraft column — a stationary deep convective system with persistent heavy precipitation, likely the wettest region on the planet.

### 2.4 Day-Night Temperature Contrast

The 8-bar atmosphere is very efficient at heat redistribution. The day-night temperature contrast at the surface is estimated at only 30–60 K, producing moderate rather than extreme wind forcing. The day-to-terminator gradient driving katabatic flow is approximately 25–30 K.

---

## 3. Geophysics and Volcanism

### 3.1 Mantle Structure

The mantle is both deeper and under significantly higher pressure than Earth's. Pressure at the base of the mantle is estimated at 400–600 GPa, compared to Earth's ~136 GPa at the core-mantle boundary. Deep mantle silicates are pushed into high-pressure phases (post-perovskite and beyond) with substantially higher viscosity.

### 3.2 Stagnant Lid Regime

The planet most likely operates in a **stagnant lid** regime rather than exhibiting plate tectonics. Multiple reinforcing factors support this conclusion:

- Mantle viscosity increases with pressure, making the deep mantle sluggish and resistant to whole-mantle convection.
- Lithospheric yield strength scales with gravity; at 1.82g, the lithosphere is harder to fracture, and higher confining pressures make subduction initiation more difficult.
- Most numerical models of super-Earth mantle convection find that above ~2–3 Earth masses, the system preferentially settles into a stagnant lid.
- Slow rotation from tidal locking removes a modest assist to mantle stirring.

**Note:** The plate tectonics question for super-Earths remains unsettled. A minority view holds that higher convective stresses could favor plate tectonics. Most recent modeling supports the stagnant lid conclusion.

### 3.3 Plume Volcanism

Without plate tectonics, mantle plumes are the **primary heat loss mechanism**. Internal heat production scales approximately as mass (~4.2× Earth's radiogenic budget), while surface area only increases as radius squared (~2.3× Earth's). Heat flux per unit area through plumes must be roughly double Earth's or higher.

Individual plume heads could be 500–1000 km across. The resulting volcanic provinces would dwarf anything on Earth. Eruptions produce primarily basaltic to ultramafic magmas — hot, fluid melts from massive decompression melting. Higher gravity suppresses eruption column height but increases conduit pressure and effusion rates, favoring enormous lava floods over towering columns.

### 3.4 Episodic Lid Overturn

> **[SUPERSEDED — Feb 2026]** Subsequent analysis (see `substrate_planetary_geology_hub.md`) concluded that global episodic lid overturn does **not** occur on this planet. The hemispheric thermal asymmetry from tidal locking creates a permanent pressure-release valve: the thin, warm day-side lid allows continuous plume breaching (~10–30 provinces simultaneously), preventing the sub-lid heat accumulation that would trigger global foundering. The Venus analogy fails because Venus lacks this asymmetry. Dark-side plume breakthrough remains possible but rare (~500 Myr–1 Gyr) and localized, not global.

An intermediate regime between permanent stagnant lid and continuous plate tectonics is **episodic lid overturn** (analogous to what Venus may experience). During long stagnant lid phases, heat accumulates beneath the lid. Eventually the lid's negative buoyancy exceeds its yield strength, triggering a runaway positive feedback — foundering lithosphere is replaced by hot mantle material, triggering further foundering, propagating globally.

**Estimated overturn interval:** 300 million to 1 billion years.

**Overturn duration at peak intensity:** 1–10 million years.

---

## 4. Volcanic Hazards to the Biosphere

### 4.1 Critical Context: Reducing Atmosphere and Silicon Biochemistry

The biosphere operates under fundamentally different chemical constraints than an Earth-like system. The atmosphere is reducing. The oceans are liquid ammonia. The biochemistry is silicon-based. Volcanic hazard analysis must be reframed entirely outside Earth-centric assumptions.

**The volcanic outgassing suite in a reducing environment** does not produce SO₂ and CO₂. Instead, expected volcanic gases include: H₂S, CH₄, CO, H₂, NH₃, HCl, HF, and possibly silicon-bearing volatiles (SiH₄, SiF₄).

### 4.2 Threat Hierarchy

The following volcanic threats are listed in approximate order of concern for silicon-based life in a reducing ammonia-ocean environment:

#### 4.2.1 Oxidation Stress (Chronic and Acute)

**The primary existential threat.** Any volcanic process introducing oxidizing species into the environment is injecting poison into a reducing biosphere. Volcanic water vapor is a particular concern — water reacting with silicon biochemistry produces siloxane bonds and ultimately silicates, effectively converting living chemistry into rock. Water vapor dissociating in the upper atmosphere could produce free oxygen.

Even CO is more oxidized than the background the biochemistry requires. Major eruptions spike the oxidant load well above chronic background levels.

This represents an ongoing, cumulative stress that the biosphere must constantly manage. Silicon-based organisms presumably have reducing defense mechanisms analogous to how Earth's anaerobes once coped with trace oxygen, but these defenses can be overwhelmed during major volcanic episodes.

#### 4.2.2 Fluorine Poisoning (Acute, During Major Eruptions)

**Potentially the sharpest kill mechanism.** Fluorine has a uniquely destructive relationship with silicon chemistry. Si-F bonds are among the strongest single bonds in chemistry (~565 kJ/mol). HF will attack virtually any silicon-based molecular structure and convert it to fluorosilicates — this is the industrial process used to etch silicon wafers.

If the mantle contains fluorine (and there is no reason to expect it would not), volcanic outgassing of HF into the ammonia atmosphere and oceans could be devastating. HF dissolved in liquid ammonia forms ammonium fluoride, which remains reactive toward silicon biochemistry. The severity scales directly with eruption volume, making mega-plume events particularly dangerous.

**Fluorine poisoning may be the primary mass extinction mechanism on this world.**

> **[REVISED — Feb 2026]** Subsequent analysis (see `substrate_planetary_geology_hub.md` and `substrate_fluorine_ecology.docx`) found that fluorine is managed by the biosphere as a chronic ecological pressure rather than an extinction-level volcanic threat. Fluorine-tolerant organisms (thorn-flora) sequester HF into stable fluorosilicates, creating a fluorine ecology. Major eruptions cause local/regional fluorine stress, but the biosphere has evolved effective defenses. HF is downgraded from "primary mass extinction mechanism" to "significant chronic hazard, locally acute during major eruptions."

#### 4.2.3 Thermal Disruption of Ammonia Seas

> **[SUPERSEDED — Feb 2026]** Subsequent analysis concluded that volcanic thermal disruption of ammonia seas is negligible. Stellar heating dominates internal heat by ~1600:1. Volcanic heat flux (~120 mW/m²) cannot meaningfully warm the seas against the stellar radiation budget. The ammonia boiling feedback described below does not operate.

Liquid ammonia has a narrower liquid range than water, even at 8 bar. Major volcanic thermal pulses risk regional or global boiling of the ammonia seas. Ammonia's latent heat of vaporization is lower than water's, requiring less energy for phase transition. A major flood basalt province erupting beneath or adjacent to a shallow ammonia sea could flash-boil enormous volumes.

A dangerous positive feedback exists: ammonia vapor is a potent greenhouse gas. Volcanic heating boils ammonia, increasing greenhouse warming, which boils more ammonia. Whether this runs away depends on whether nightside cold-trap recondensation can keep pace. The katabatic circulation works to transport ammonia vapor to the nightside for recondensation, but during severe volcanic episodes it may be insufficient.

#### 4.2.4 H₂S Loading of the Ammonia Oceans

H₂S replaces SO₂ as the dominant sulfur volcanic gas. Massive H₂S injection into ammonia oceans would produce ammonium hydrosulfide (NH₄SH) and dramatically alter ocean chemistry. H₂S is less immediately threatening to silicon biochemistry than oxidizing species or fluorine — sulfur can participate in silicon chemistry through Si-S bonds — but at massive concentrations it could disrupt biochemical equilibria.

### 4.3 Catastrophe Hierarchy and Recurrence

> **[REVISED — Feb 2026]** The "Full lid overturn" row is superseded — no global overturn occurs on this planet (see §3.4 note). The revised threat hierarchy is: (1) chronic oxidation stress from volcanic H₂O (the real long-term killer, via the H₂O ratchet — see `substrate_planetary_geology_hub.md`), (2) SiH₄ depletion from the one-way silicon cycle, (3) local fluorine and H₂S stress from individual eruptions. Volcanism is a chemical hazard, not a thermal one.

The volcanic threat operates on multiple timescales, each presenting different severity:

| Event Type | Recurrence | Severity |
|---|---|---|
| Continuous background plume volcanism | Always active somewhere | Locally devastating, globally manageable |
| Major plume head / large igneous province | Every few million to tens of millions of years | Mass extinction–capable; major fluorine and oxidation stress; possible regional ammonia sea disruption |
| Full lid overturn | Every 300 million to 1 billion years | Near-total extinction of complex surface life; potential sterilization of deep biosphere |

### 4.4 Overturn Events: Severity Assessment

> **[SUPERSEDED — Feb 2026]** This section assumed global lid overturn occurs. It does not — see §3.4 note. Retained for reference only.

Full lid overturn events are potentially more severe than initially estimated when accounting for the reducing-atmosphere silicon-biochemistry context:

- Massive simultaneous flood basalt eruptions across large fractions of the surface, releasing enormous quantities of volcanic gases over 1–10 million years at peak intensity.
- Fluorine poisoning at global scale from cumulative HF outgassing.
- Potential shift of the atmosphere toward a more oxidized state for millions of years — not merely an inconvenience for silicon-based life but an **existential chemical incompatibility**.
- Unlike Earth, where the deep biosphere (carbon-water chemolithotrophs) reliably survives overturn events and reseeds the surface, **a reducing-atmosphere overturn that introduces oxidizing conditions into the deep crust could sterilize even the deep biosphere refuge.** Evolutionary resets on this world may be more complete than the Earth analog suggests.

### 4.5 Implications for Evolutionary Trajectory

The biosphere faces a relentless hierarchy of volcanic stresses at every timescale. Evolution on this world would strongly favor:

- Chemical resilience, particularly against oxidation and fluorine exposure
- Rapid recolonization ability
- Tolerance for atmospheric and ocean chemistry variability
- Deep subsurface refuge strategies (though these may fail during overturns)

The window for complex life development between major catastrophes (200–700 million years between overturns, minus recovery time of 50–100+ million years) constrains evolutionary complexity. Whether technological civilization can emerge depends heavily on where in the volcanic cycle the biosphere is sampled.

The 8-bar atmosphere provides some buffering against individual eruption events (volcanic gas injection is diluted into a larger atmospheric mass), but this advantage is overwhelmed during the largest events.

---

## 5. Open Questions and Recommended Further Analysis

1. **Mantle fluorine budget:** Quantifying the fluorine content of the mantle is critical to assessing the severity of volcanic mass extinctions. This determines whether HF outgassing during major events is a significant threat or a dominant one.

2. **Oxidation budget of volcanic outgassing:** Detailed modeling of volcanic gas speciation under the specific pressure-temperature-composition conditions of this world's mantle is needed to quantify the oxidation stress per unit eruption volume.

3. **Ammonia sea thermal stability:** Coupled volcanic-atmospheric-ocean modeling to determine whether the ammonia boiling → greenhouse feedback can run away during major eruptions, or whether nightside recondensation provides a sufficient stabilizing mechanism.

4. **Deep biosphere survival during overturns:** Can reducing conditions be maintained in deep crustal refugia even during overturn events? If so, what depth and geological settings provide the most robust refuges? This determines whether overturns are "hard resets" or merely severe bottlenecks.

5. **Overturn interval refinement:** Better constraining the recurrence interval through thermal evolution modeling with this world's specific parameters (mass, radiogenic inventory, lithospheric yield strength under 1.82g) is essential for assessing evolutionary windows.

6. **Biological fluorine defense mechanisms:** Is it chemically plausible for silicon-based biochemistry to evolve effective defenses against fluorine attack? If not, fluorine may represent a hard ceiling on biological complexity in volcanically active regions.

7. **Volcanic triggering by tidal forces:** At 0.12 AU, stellar tidal forces on the mantle may modulate volcanic activity on orbital or longer timescales. Whether this increases or decreases the frequency of major eruptions relative to a non-tidally-stressed body deserves investigation.
