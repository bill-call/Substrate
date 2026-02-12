# SUBSTRATE — TERMINATOR HUB

**v1.0 — February 2026**

Physics-first analysis of terminator zone dynamics. All inputs, math, and conclusions shown. Cross-references Chemistry Hub v1.2.

---

## 1. CANONICAL PLANETARY PARAMETERS

### 1.1 Inputs from World-Builder Instance

These parameters are treated as canonical constraints:

| Parameter | Value | Source |
|-----------|-------|--------|
| Surface gravity | 1.82g (17.8 m/s²) | World-builder |
| Atmospheric pressure | 8 bar | World-builder |
| Atmosphere composition | N₂-dominated | World-builder |
| Planet radius | ~1.2 Earth radii | World-builder |
| Star type | Red dwarf | World-builder |
| Orbital configuration | Tidally locked | World-builder |
| Peak surface wind | ~12.5 m/s at 30-40° from antistellar | World-builder |
| Terminator wind | ~11.5 m/s | World-builder |
| Air density at terminator | ~7.9 kg/m³ (6.5× Earth sea level) | World-builder |
| Pressure scaling α | 0.25 | World-builder |
| Drag coefficient | C_d = 0.002 | World-builder |

### 1.2 Original Temperature Profile (World-Builder)

| Location | Temperature |
|----------|-------------|
| Substellar | 360K (87°C) |
| Terminator | 338K (65°C) |
| Antistellar | 285K (12°C) |
| ΔT | 75K |

### 1.3 The Ammonia Problem

**Ammonia phase behavior at 8 bar:**

| Property | Value |
|----------|-------|
| Freezing point | ~196K |
| Boiling point at 8 bar | ~290-295K |
| Critical point | 405.4K at 113.5 bar |

**At canonical 338K terminator temperature, ammonia cannot be liquid at the surface.**

This breaks:
- Ammonia rain at terminator
- Carved channel erosion model
- Genesis void feeding mechanism
- Ammonia seas in terminator basins

### 1.4 Proposed Temperature Adjustment

**Solution: Move planet slightly further from star, reducing temperatures ~50K while preserving ΔT.**

| Location | Canonical | Revised |
|----------|-----------|---------|
| Substellar | 360K | **310K** (37°C) |
| Terminator | 338K | **288K** (15°C) |
| Antistellar | 285K | **235K** (-38°C) |
| ΔT | 75K | 75K (preserved) |

**Result:** Terminator at 288K is just below ammonia's boiling point (~290-295K at 8 bar). The terminator becomes the **condensation line**.

### 1.5 Atmospheric Composition Reconciliation

The Chemistry Hub assumed H₂-dominated atmosphere. The world-builder specifies N₂-dominated. Reconciliation:

| Component | Fraction | Role |
|-----------|----------|------|
| N₂ | ~70% | Pressure buffer, thermal mass, non-reactive |
| H₂ | ~15% | Volcanic outgassing, metabolic product, reducing agent |
| CH₄ | ~10% | Carbon source, volcanic origin |
| NH₃ | ~4% | Nitrogen source, the solvent species |
| SiH₄ | ~0.3% | Volcanic trace, primary energy source |

**Rationale:**
- N₂ dominance gives 8 bar pressure and 6.5× density
- Reactive species (CH₄, NH₃, SiH₄) remain abundant enough for silicon biochemistry
- Pure H₂ atmospheres escape over geological time; N₂ is stable
- H₂ is volcanic trace, continuously replenished and consumed

---

## 2. WIND DYNAMICS

### 2.1 Wind Speed vs. Force

**Input:** 11.5 m/s at terminator, 6.5× Earth air density

**Dynamic pressure calculation:**

```
P_dynamic = ½ρv²

Earth at 11.5 m/s:
P = 0.5 × 1.2 kg/m³ × (11.5)² = 79 Pa

This planet at 11.5 m/s:
P = 0.5 × 7.9 kg/m³ × (11.5)² = 522 Pa
```

**Equivalent Earth wind speed for same pressure:**

```
522 = 0.5 × 1.2 × v²
v = √(522 / 0.6) = √870 = 29.5 m/s
```

**✓ CONFIRMED:** 11.5 m/s at 8 bar delivers force equivalent to ~29-30 m/s on Earth.

### 2.2 Steady-State Condition

**Critical insight:** A tidally locked planet with no axial tilt has:
- No Coriolis cells (too slow rotation)
- No seasonal variation (fixed stellar position)
- No diurnal cycle (permanent day/night)
- No variable solar input (constant illumination pattern)

**Consequence:** The atmospheric circulation reaches equilibrium and stays there. The wind at any point is constant — same direction, same speed, forever.

**There is no temporal variation in weather.** What exists, exists permanently.

---

## 3. AMMONIA HYDROLOGY

### 3.1 Phase Zones

At 8 bar surface pressure with revised temperatures:

| Zone | Temperature | Ammonia State |
|------|-------------|---------------|
| Substellar | 310K | Gas (above BP) |
| Mid day-side | 300K | Gas (above BP) |
| Near terminator (day) | 293K | Gas (at/above BP) |
| Terminator | 288K | **Liquid** (below BP) |
| Near terminator (night) | 270K | Liquid |
| Deep night | 235K | Liquid/frozen (near FP at 196K) |

### 3.2 The Rain Wall

**The terminator is the planetary condensation line.**

Atmospheric ammonia (vapor) carried from the day side meets cooling air at the terminator. Temperature drops below the dew point. Condensation occurs. Rain falls.

```
DAY SIDE              TERMINATOR              NIGHT SIDE
  310K                   288K                    235K
   
NH₃ vapor    →→→      condensation      →→→    NH₃ liquid
                           ↓
                        RAIN
```

### 3.3 Rain Angle

**Terminal velocity of ammonia drops:**

Ammonia drop: ~5-10 m/s terminal velocity (depends on size; higher gravity accelerates, denser air decelerates — partial cancellation)

**Rain angle calculation:**

```
Horizontal wind: 11.5 m/s
Vertical fall: ~8 m/s (mid-estimate)

Angle from vertical = arctan(11.5 / 8) = 55°
```

**The rain falls at ~55° from vertical — steep diagonal, not horizontal.**

### 3.4 Rain Penetration Distance

**Question:** How far does rain penetrate toward the day side before evaporating?

As drops move day-ward:
- Air temperature rises
- Evaporation rate increases
- Drops shrink and vanish

**Evaporation distance estimate:**

Small drops in warming air: evaporation in seconds to tens of seconds.

At 11.5 m/s horizontal wind:

| Evaporation time | Distance traveled |
|------------------|-------------------|
| 10 seconds | 115 m |
| 30 seconds | 345 m |
| 100 seconds | 1.15 km |

**The rain band is narrow — a few kilometers wide at most.**

### 3.5 The Flashpoint Boundary

Where temperature reaches ammonia's boiling point (~293K at 8 bar):
- All surface ammonia flashes to vapor
- Flowing channels terminate abruptly
- Dissolved/suspended material precipitates out

**This creates a sharp phase-transition boundary** — an isotherm circling the entire day side.

---

## 4. EROSION REGIMES

### 4.1 Grit Distribution

**The rain scrubs particulates from the air:**

| Zone | Airborne grit? | Reason |
|------|----------------|--------|
| Night side | Yes | Particles accumulate, wind carries them |
| Terminator rain band | **No** | Rain scrubs air clean |
| Day side | Yes | Surface recycling, wind picks up debris |

### 4.2 Erosion Types by Zone

| Zone | Dominant erosion | Agent | Result |
|------|------------------|-------|--------|
| Night side | Aeolian | Wind + grit | Polished, faceted, smooth |
| Terminator | **Fluvial** | Ammonia runoff | Carved, channeled, rough |
| Day side | Aeolian | Wind + grit | Polished, faceted, smooth |

### 4.3 Ammonia Erosion Power

**Stream power comparison to Earth:**

| Factor | Ratio | Reason |
|--------|-------|--------|
| Fluid density | 0.68× | NH₃ 680 kg/m³ vs H₂O 1000 kg/m³ |
| Gravity | 1.82× | Higher g |
| Velocity | 1.35× | v ∝ √(g × slope) |
| **Combined** | **1.67×** | 0.68 × 1.82 × 1.35 |

**Ammonia runoff erodes ~1.7× faster than water on Earth, all else equal.**

### 4.4 The Terminator Terrain

Running for billions of years at 1.7× erosion rate:
- Deeply incised canyon systems
- Mature, integrated drainage networks
- Gullies, channels, arroyos
- Caves, overhangs, undercutting
- **Rough, complex terrain**

**The terminator is the most texturally complex terrain on the planet.**

Night side and day side are wind-polished smooth. The terminator is carved.

### 4.5 The Abrupt Erosion Boundary

**Transect from terminator to day side:**

```
TERMINATOR          FLASHPOINT           DAY SIDE
   288K               ~293K                310K
    
liquid NH₃        NH₃ flashes           no liquid
    ↓                  ↓                    ↓
CARVED            DEPOSITION            POLISHED
channels          zone                  wind-worn
gullies           (payload drops)       smooth
rough             chemical-rich         featureless
    
←─────────────────→│←────────→│←─────────────────→
   ammonia          boundary      aeolian erosion
   erosion          (narrow)          only
```

**The channels terminate abruptly at the flashpoint isotherm.**

This creates a "bathtub ring" — a narrow band of chemical-rich evaporite deposits circling the entire day side at the ~293K isotherm.

---

## 5. ATMOSPHERIC FEEDSTOCK TRANSPORT

### 5.1 The Particulate Problem

**What the Chemistry Hub assumed:** Katabatic wind carries feedstock from night side across terminator to day side. Particulates complete a full circuit.

**What the rain does:** Scrubs particulates from the air at the terminator.

**Consequence:** Particulates never reach the day side via atmospheric transport.

### 5.2 Analysis of Alternative Transport Mechanisms

#### 5.2.1 Altitude Stratification

**Hypothesis:** Rain has a ceiling. High-altitude transport passes over the rain zone.

The superstream (high-altitude return flow from day to night) might pass above the condensation zone. Material lofted to superstream altitude could bypass the scrubbing.

**Result:** Fine aerosols at high altitude may reach the day side. A restricted, filtered feedstock.

#### 5.2.2 Temporal Variation

**Hypothesis:** Rain intensity varies, allowing periodic slip-through.

**REJECTED:** No mechanism for temporal variation. The system is steady-state. No seasons, no cycles, no storms that come and go.

The only possible driver is volcanic eruptions — episodic, localized, too rare to sustain an ecology.

#### 5.2.3 Geographic Gaps

**Hypothesis:** Terrain creates rain shadows; some corridors have less precipitation.

**Plausible but limited:** Mountain ranges might create local gaps. Day-side feedstock would be patchy, concentrated downwind of specific gaps.

#### 5.2.4 Underground Bypass (Aquifer)

**Hypothesis:** Liquid ammonia flows underground, pressure-stabilized, carrying dissolved material from terminator toward day side.

**Analysis:**

Lithostatic pressure gradient at 1.82g:
```
dP/dz = ρ_rock × g = 3000 kg/m³ × 17.8 m/s² ≈ 530 bar/km
```

At depth, pressure rises rapidly. Higher pressure raises ammonia's boiling point. Liquid ammonia can exist at higher temperatures underground.

Ammonia boiling point vs. pressure:

| Pressure | Boiling point |
|----------|---------------|
| 8 bar | ~293K |
| 50 bar | ~360K |
| 100 bar | ~390K |
| 113 bar (critical) | 405K |

**At ~100m depth, pressure is sufficient to keep ammonia liquid at day-side temperatures (~300-310K).**

Liquid ammonia zone extends from ~100m to ~1km depth (where you hit supercritical conditions).

**Result:** Underground aquifer can transport dissolved material from terminator to day side.

#### 5.2.5 Particle Size Selection

**Hypothesis:** Fine aerosols (<0.1 μm) follow streamlines around raindrops, escaping capture.

**Plausible:** Very fine particles have low Stokes numbers; they follow air currents around obstacles. Some fraction may slip through the rain band.

**Result:** Day side receives finest fraction only — simple precursors, not heavy oligomers.

### 5.3 Feedstock Fate Summary

| Pathway | What passes | Reaches day side? |
|---------|-------------|-------------------|
| Surface wind (bulk) | Heavy particles, oligomers | **No** — scrubbed by rain |
| High-altitude (superstream) | Fine aerosols | **Partial** — bypasses rain |
| Underground (aquifer) | Dissolved material | **Yes** — pressure-stabilized |
| Direct volcanic | Local emissions | **Yes** — at volcanic provinces |

**The day side is feedstock-starved, not feedstock-absent.** It receives:
- Fine aerosols (slip-through)
- Dissolved material (aquifer)
- Volcanic outgassing (local)

This is enough to sustain sparse pioneer ecology, not enough for tower symbiotes.

---

## 6. THE GENESIS VOID MODEL

### 6.1 The Delivery System

The carved channel network concentrates and funnels ammonia runoff:

```
ATMOSPHERE (permanent lightning)
        ⚡⚡⚡⚡⚡
           ↓
    [complex products form]
           ↓
    ↘ ↘ ↘ rain ↘ ↘ ↘
           ↓
═══════════════════════════════════════════ SURFACE
           ↓
    ~~~~ runoff ~~~~
           ↓
    carved channel network
     (billions of years
      of ammonia erosion)
           ↓
        ╲  ↓  ╱
         ╲ ↓ ╱  channels converge
          ╲↓╱
══════════╩══════════ VOLCANIC FRACTURE ZONE
           ║
           ║  ammonia + dissolved payload
           ║  flows down
           ║
──────────╨────────── VAPORIZATION DEPTH (~323K)
           │
      NH₃ flashes to vapor
           │
    payload precipitates
           ↓
    ┌─────────────┐
    │   GENESIS   │
    │    VOID     │
    │  (gas-filled │
    │   chamber)  │
    └─────────────┘
```

### 6.2 Vaporization Depth Calculation

Underground temperature rises with depth (geothermal gradient ~25-30K per km).

Starting at terminator surface (288K):

| Depth | Temperature | Pressure | NH₃ state |
|-------|-------------|----------|-----------|
| 0 | 288K | 8 bar | Liquid |
| 500m | ~300K | ~270 bar | Liquid (BP ~380K at this pressure) |
| 1 km | ~315K | ~530 bar | Liquid/supercritical |

Wait — this doesn't work. Pressure rises so fast that ammonia stays liquid/supercritical. Let me reconsider.

**Revised analysis:** The vaporization happens where ammonia flows from high-pressure zone to low-pressure zone — i.e., into a **gas-filled void** (volcanic cavity at near-surface pressure).

```
CRACK SYSTEM (high pressure, liquid NH₃)
           ↓
═══════════════════════════ void boundary
           ↓
    GAS-FILLED CAVITY
    (near-surface pressure, ~8 bar)
    (temperature from geothermal: ~320K+)
           ↓
    NH₃ flashes on entering void
    Payload drops out
```

The void is a pressure boundary, not a depth-defined isotherm. Volcanic cavities at any depth, if connected to the surface (maintaining near-surface pressure), would cause flashing.

### 6.3 What Accumulates

| From rain (above) | From volcanic (below) |
|-------------------|----------------------|
| Tholins | Fresh SiH₄ |
| Silazane oligomers | Trace metals (Ni, Fe, Co, Ti) |
| Metallosilazane fragments | Heat |
| Complex organosilicon | HF, volcanic halogens |

The genesis void is fed from both directions. Two feedstock streams converge.

### 6.4 Why This System is Robust

| Component | Constancy |
|-----------|-----------|
| Lightning | Permanent (steady-state thermal gradient) |
| Rain | Permanent (steady-state condensation) |
| Channel network | Permanent (carved over billions of years) |
| Volcanic fractures | Geologically maintained |
| Pressure differential | Physics guarantees it |

**The system runs continuously.** Not waiting for lucky events. The planet's physics funnels chemistry toward the genesis voids automatically.

---

## 7. ECOLOGICAL ZONATION

### 7.1 Zone Summary

| Zone | Temp | NH₃ state | Feedstock | Energy | Towers | Notes |
|------|------|-----------|-----------|--------|--------|-------|
| Deep night | 235K | Liquid/frozen | Accumulates | None (dark) | Dormant | Cold storage |
| Near terminator (night) | 260K | Liquid | Available | Limited | Active | Energy-limited |
| **Terminator** | 288K | **Rain** | **Concentrated** | **Lightning** | **Network heart** | Origin of life |
| Flashpoint boundary | 293K | Flash/evaporating | **Deposits** | Solar | Sparse | Deposition ring |
| Near terminator (day) | 300K | Gas | Fine aerosols, aquifer | Solar | Very sparse | Aquifer-dependent |
| Deep day | 310K | Gas | None (scrubbed) | Solar | **None** | Wild lands |

### 7.2 The Day-Side Desert

The deep day side receives no atmospheric feedstock. It is:
- Energy-rich (solar)
- Matter-poor (scrubbed)
- Tower-absent (no feedstock for tower symbiotes)
- Sparse pioneer ecology (recycling original colonizers)
- Oasis-dependent (volcanic + aquifer intersections)

### 7.3 The Deposition Ring

The flashpoint boundary (~293K isotherm) accumulates:
- Evaporite deposits from terminated channels
- Chemical-rich sediments (billions of years of deposition)
- The richest surface mineral concentration on the planet

**This may be where day-side life gets its foothold.** The "bathtub ring" as the first oasis.

### 7.4 Day-Side Oases

Limited to:

| Oasis type | Feedstock source | Notes |
|------------|------------------|-------|
| Volcanic provinces | Direct outgassing | Fresh chemistry, metals, heat |
| Aquifer upwellings | Dissolved terminator material | Deep roots required |
| Deposition ring zones | Evaporite accumulation | At flashpoint boundary |

---

## 8. IMPLICATIONS FOR LIFE

### 8.1 Origin of Life

**Location:** Terminator volcanic provinces, specifically genesis voids fed by the carved channel network.

**Mechanism:** Lightning-synthesized products → rain transport → channel concentration → vaporization precipitation → surface chemistry in gas-filled voids.

**Reference:** See Chemistry Hub §13 for detailed chemical pathway.

### 8.2 Day-Side Colonization

**Mechanism:** Passive dispersal (wind, ammonia flooding events) carries organisms/spores across the rain wall.

**Survival requirement:** Self-powered (no grid to tap), self-synthesizing (limited feedstock).

**Result:** Sparse pioneer ecology, slowly building through recycling and oasis-feeding.

### 8.3 Day-Side Ecology

Over geological time, the pioneers create new niches:

| Wave | Type | Nutrition |
|------|------|-----------|
| 1 | Pioneers | Self-synthesize from raw atmosphere + solar |
| 2 | Consumers | Eat pioneers |
| 3 | Predators | Eat consumers |
| 4 | Mutualisms | Service exchanges (e.g., thorn-flower + pollinator) |
| 5 | Arms races | Escalating offensive/defensive adaptations |

### 8.4 The Amorphs

**Origin:** Day-side desert, evolved self-sufficiency.

**Return to terminator:** Armed with fluorine weapons developed in day-side volcanic provinces.

**Status:** Day-side invaders who learned to weaponize the terminator's volcanic chemistry.

### 8.5 The Network

**Location:** Terminator and night-side only.

**Day-side extent:** None — no towers, no grid, no presence.

**Boundary:** The rain wall defines the network's extent. Beyond it, the network cannot feed itself.

---

## 9. OPEN QUESTIONS

### 9.1 For World-Builder

- [ ] Confirm revised temperature profile (288K terminator, 310K substellar, 235K antistellar)
- [ ] Confirm atmospheric composition reconciliation (N₂ 70%, H₂ 15%, CH₄ 10%, NH₃ 4%, SiH₄ 0.3%)
- [ ] Validate underground aquifer model
- [ ] Clarify night-side tower status (dormant? dead? minimal activity?)

### 9.2 For Chemistry Hub

- [ ] Update all references to "terminator ammonia seas" → ammonia exists but as rain system, not seas
- [ ] Clarify ammonia sea location (night side, not terminator)
- [ ] Add deposition ring chemistry

### 9.3 Unresolved Physics

- [ ] Exact rain density (affects scrubbing efficiency)
- [ ] Superstream altitude vs. rain ceiling (affects high-altitude bypass)
- [ ] Aquifer flow rates and recharge

---

## 10. CROSS-REFERENCES

| Topic | Document | Section |
|-------|----------|---------|
| Silicon biochemistry | Chemistry Hub | §1-11 |
| Silane metabolism | Chemistry Hub | §3.1 |
| Genesis void chemistry | Chemistry Hub | §13 |
| Fluorine ecology | Chemistry Hub | §7, Fluorine Ecology Hub (pending) |
| Thorn-flower biology | Fluorine Ecology Hub | (pending) |
| Amorph origins | (this document) | §8.4 |

---

## 11. VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Feb 2026 | Initial compilation from chemistry session |

---

*The physics found substrate and began to carve.*
