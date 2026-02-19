# Terminator Mound, Mudflat, and Rain Zone Geometry

**Derivation document — February 2026**

Load with: spine (required), planetary geology hub (recommended).

---

## 1. Temperature Gradient Map: T(θ)

### Assumptions

1. Steady-state energy balance (tidally locked, no obliquity, no seasons).
2. Single planet-wide overturning cell with massive heat transport (8 bar, cp = 1450 J/kg·K, volumetric heat capacity 10× Earth).
3. NH₃ latent heat acts as thermostat near 240K (condensation releases heat below dew point, evaporation absorbs heat above).
4. Three anchor points: T(0°) = 265K, T(90°) = 240K, T(180°) = 215K.

### Derivation

**Radiative equilibrium baseline (no transport):**

Stellar flux at the planet: S = L★/(4πd²) ≈ 1420 W/m². Absorbed: S(1−A) = 780 W/m².

Radiative equilibrium at substellar: T_eq(0°) = [780/σ]^(1/4) = 342K. Night side: T_eq → 0K.

Actual range is 265–215K = 50K, vs radiative equilibrium 342–0K. The atmosphere redistributes ~85% of stellar heating.

**Why a cosine is wrong:**

The uniform-transport solution T(θ) = 240 + 25 cos(θ) hits all three anchors but gives constant gradient everywhere. The atmosphere creates three distinct regimes:

- **Day side (0°–~70°):** Substellar thermal chimney drives vigorous convective mixing → temperatures homogenized → FLATTER than cosine.
- **Terminator zone (~70°–110°):** NH₃ condensation/evaporation concentrates the gradient. Condensation releases 1374 kJ/kg at 12.5% mixing ratio. Temperature resists dropping smoothly through 240K → STEEPER than cosine.
- **Night side (~110°–180°):** Cold, stably stratified (cold dense air at surface). No convective overturning. Radiative cooling slow (N₂/H₂ poor radiators, NH₃ depleted) → FLATTER than cosine.

**Asymmetric sigmoid model:**

Day side (0° ≤ θ ≤ 90°):

> T(θ) = 240 + 25 × tanh(k_d × (90° − θ)/90°), k_d = 3.5

Night side (90° < θ ≤ 180°):

> T(θ) = 240 − 25 × tanh(k_n × (θ − 90°)/90°), k_n = 2.5

The asymmetry (k_d > k_n) reflects: sharp day-side cutoff from convective mixing into the condensation zone, vs gentler night-side decline under stable stratification.

**Physical justification for k values:**

NH₃ column mass: P_NH₃/g = 10⁵/17.85 ≈ 5,600 kg/m². Latent heat reservoir: 5,600 × 1.374×10⁶ = 7.7 GJ/m² — equivalent to ~10⁷ seconds (115 days) of stellar heating at 780 W/m². This enormous thermal inertia concentrates the temperature transition into a narrow zone.

Night-side k is lower because: stably stratified atmosphere, poor radiative emissivity after NH₃ depletion, longer cooling length scale.

### Result: T(θ) Profile

| θ (from substellar) | T (K) | Zone |
|---|---|---|
| 0° | 265.0 | Substellar chimney |
| 15° | 264.9 | Inner day side |
| 30° | 264.5 | Inner day side |
| 45° | 263.5 | Inner day side |
| 60° | 260.6 | Outer day side |
| 70° | 256.3 | Rain onset aloft |
| 75° | 253.1 | Upper-level rain |
| 80° | 249.3 | Surface rain approaching |
| 85° | 244.8 | Surface rain zone |
| 88° | 241.9 | Heavy rain |
| 90° | 240.0 | Mound crest (terminator) |
| 92° | 238.1 | Night-side rain |
| 95° | 235.9 | Rain diminishing |
| 100° | 232.0 | Post-rain shore zone |
| 105° | 228.4 | Near night side |
| 110° | 225.5 | Night-side transition |
| 120° | 221.3 | Night-side basins |
| 135° | 217.8 | Deep dark side |
| 150° | 216.1 | Near-antistellar |
| 180° | 215.1 | Antistellar cap |

**Width of the 240K isotherm band:**

| Definition | Day boundary | Night boundary | Width (°) | Width (km) |
|---|---|---|---|---|
| T = 240 ± 5K | θ ≈ 85° | θ ≈ 95° | ~10° | ~1,700 |
| T = 240 ± 2K | θ ≈ 88° | θ ≈ 92° | ~4° | ~680 |

**Gradient at the terminator:** Peak dT/dθ = −0.97 K/° (day approach), −0.69 K/° (night departure). In linear terms: ~5.7 mK/km (day) and ~4.1 mK/km (night). Compare: pure cosine gives 0.44 K/° everywhere — actual gradient at terminator is ~2× steeper.

**Mound elevation correction:** The mound crest sits ~2 km above reference terrain (§3). At moist lapse rate ~5 K/km:

- Mound crest: T_crest ≈ 240 − 5×2 = **230K** (10K below general terminator temperature)
- Mound base (day side): T ≈ 240–242K (right at dew point)

The mound itself creates a ~10K temperature gradient over its ~2 km height. The tower forest lives at 230K, not 240K. The evaporation boundary (mudflat) coincides with the mound base.

### Implications

- Habitable terminator zone (liquid NH₃ available, moderate T): ~1,700 km wide at equator.
- Day side thermally hospitable (~260K) but ammonia-starved (no surface rain).
- Night side cools slowly — hundreds of km before conditions change significantly.
- Tower forest at 230K is colder than general terminator. Heavy, persistent condensation at the crest.

### Uncertainties

- k values (3.5, 2.5) physically motivated but not derivable without a GCM. Plausible range: k_d = 2.5–4.5, k_n = 2.0–3.5.
- Mound elevation correction depends on mound height (§3) and local lapse rate.
- Profile assumes azimuthal symmetry at leading order (confirmed: superrotation absent).

---

## 2. Rain Zone Geometry

### Assumptions

1. NH₃ dew point at 1.0 bar partial pressure ≈ 240K (spine constraint).
2. Superstream at 12–16 km carries NH₃ (as ice crystals) from the substellar chimney.
3. Rain scavenging begins well dayside of the mound crest (spine).
4. 80–95% of rainfall lands on the day-side slope of the mound (spine).

### Derivation

**Upper-level condensation onset:**

The spine gives the condensation floor (altitude where T first drops to 240K):

| Surface T | Condensation floor altitude |
|---|---|
| 280K | 4.6 km |
| 260K | 2.4 km |
| 250K | 1.2 km |
| 240K | 0 km (surface) |

The superstream at 12–16 km is ALWAYS below 240K (air at 12 km above 265K surface: T ≈ 265 − 5×12 = 205K even at substellar). The superstream carries entrained NH₃ ice crystals from the moment it leaves the chimney. Upper-level condensation/ice formation is continuous.

"Rain scavenging begins well dayside" means: ice crystals and rain from the superstream fall through the lower atmosphere. Where the lower atmosphere is warm (T > 240K), this precipitation evaporates before reaching the surface (virga). Where T_surface approaches 240K, rain reaches the ground.

**Surface rain onset:**

NH₃ raindrop terminal velocity in 8 bar air (2 mm drop):

> v_t = √(2mg/(ρ_air × C_d × A)) ≈ 3 m/s (roughly half of Earth equivalent — dense atmosphere)

Fall time through 1.5 km of sub-dew-point air: 500 s ≈ 8 min. Evaporation timescale for a 2 mm NH₃ drop at 5K above dew point in 8 bar: >30 min (diffusion slowed 8× by pressure). Drops survive easily.

Surface rain reaches the ground wherever the condensation floor is below ~2 km (drops survive the warm layer). From the condensation floor data: this occurs at T_surface ≈ 250K → **θ ≈ 80°** (from T(θ) profile).

| Rain type | Angular onset | T_surface | Character |
|---|---|---|---|
| Upper-level (virga) | θ ≈ 55–60° | ~260K | Evaporates >2 km above surface |
| Light surface rain | θ ≈ 78–82° | ~249K | Some drops survive warm lower atmosphere |
| Heavy surface rain | θ ≈ 87–90° | ~242K | Full column saturated |
| Mound crest peak | θ ≈ 90° | 230K (elevated) | Entire column well below dew point |

**Rainfall rate estimate:**

Energy budget approach. Total heat advected through the rain zone per unit length of terminator circumference:

> ṁ_per_circumference = ρ × v × H_column = 8.2 × 9.5 × 10,000 = 7.8×10⁵ kg/(m·s)

Temperature drop across rain zone (~15K):

> Sensible heat released: 7.8×10⁵ × 1450 × 15 = 1.7×10¹⁰ W per meter of circumference

Allocating ~50% to condensation (remainder: radiation, transport to night side):

> Condensation rate: 0.5 × 1.7×10¹⁰ / 1.374×10⁶ = 6,200 kg/(m·s) per meter of circumference

Over rain zone width ~2,000 km:

> **Average rainfall: 3.1×10⁻³ kg/(m²·s) = 17 mm/hr of liquid NH₃**

Cross-check with global transport:
- Day-to-night heat transport: ~1.1×10¹⁷ W (from OLR analysis)
- Latent fraction (~50–80%): 5–9 × 10¹⁶ W
- Net NH₃ condensation: 4–6 × 10¹⁰ kg/s
- If 10% crosses to night side → total condensation: 4–6 × 10¹¹ kg/s
- Over rain zone area (~1.2×10¹⁴ m²): 3–5 × 10⁻³ kg/(m²·s) = **16–27 mm/hr** ✓

**For reference:** Earth's ITCZ averages ~0.3 mm/hr sustained. This is ~50–90× Earth's tropical average. Equivalent to a permanent moderate typhoon band wrapping the entire terminator. The 12.5% condensable fraction (vs Earth's ~2–3%) and 10× volumetric heat capacity drive this intensity.

| Location | Rainfall rate (mm/hr) | Character |
|---|---|---|
| θ ≈ 78° (onset) | ~1–3 | Light, intermittent, some virga |
| θ ≈ 83° | ~5–10 | Moderate, increasing |
| θ ≈ 87° | ~15–25 | Heavy, continuous |
| θ ≈ 90° (crest) | ~50–80 | Peak — full column saturated, crest elevated to 230K |
| θ ≈ 92° (night) | ~10–20 | Diminishing, residual NH₃ |
| θ ≈ 95° | ~3–5 | Light, atmosphere depleting |
| θ ≈ 100° | ~0.5–1 | Drizzle, nearly wrung dry |
| θ > 105° | ~0 | Rain effectively ceased |

**Rain column height:**

| Position | Rain column (surface to top) | Notes |
|---|---|---|
| θ = 80° (T_surf 249K) | ~1.5 km to ~18 km = 16.5 km | Condensation floor at 1.5 km |
| θ = 85° (T_surf 245K) | ~0.6 km to ~18 km = 17.4 km | Floor lowering rapidly |
| θ = 90° (crest, 230K) | 0 to ~18 km = **18 km full column** | Mound elevation amplifies |
| θ = 95° (T_surf 236K) | 0 to ~18 km = 18 km | Full column but NH₃ depleted |

**80–95% day-side rain: mechanism**

The superstream dumps most of its NH₃ BEFORE reaching the mound crest. The mechanism:
1. Superstream carries NH₃ ice crystals from the chimney.
2. Ice crystals grow by aggregation as they transit.
3. Large crystals fall out as they encounter the cooling lower atmosphere.
4. On the day side, rain falls through increasingly cold air — survival rate increases approaching the terminator.
5. By the time air crosses the crest, 80–95% of its NH₃ has precipitated on the day slope.
6. Residual 5–20% precipitates on the night slope, feeds night-side seas (preferentially via polar gateway where mound is thin).

### Implications

- The rain zone is a planetary-scale atmospheric scrubber — all atmospheric particulate entering the condensation zone is washed out.
- Sustained 50–80 mm/hr at the mound crest = permanent sediment delivery mechanism. The mound is inevitable.
- Rain is accompanied by continuous lightning and thunder at 8 bar (shockwave bombardment). The terminator is acoustically and hydrologically extreme.
- The day-side rain onset zone (θ ≈ 78–85°) is a transitional ecology — intermittent surface wetting, not yet permanent rain.

### Uncertainties

- Rainfall rate: ±factor of 2–3 (energy partition between sensible, latent, and radiative is poorly constrained).
- The 80–95% day-side fraction is a spine constraint; the physical mechanism is consistent but the exact split depends on atmospheric dynamics.
- Rain column height assumes well-mixed NH₃ up to ~18 km. The actual NH₃ vertical distribution is complex (ice at altitude, liquid below).

---

## 3. Mound Dimensions

### Assumptions

1. Mound is accretional sediment (volcanic ash, atmospheric fines, biological debris), not bedrock.
2. Gravity: 17.85 m/s² (1.82g).
3. Dynamic equilibrium: deposition rate = erosion rate at equilibrium profile.
4. Biotic mound stabilized by SiC grass + tower breakwaters. Pre-biotic mound unstabilized.
5. Spine constraint: mound holds by 1–3 km of headroom over the shallow nightside sea (50–200 m depth).

### Derivation

**Mound crest height:**

The spine constrains: mound crest is 1–3 km above the nightside sea surface. Nightside sea is 50–200 m deep in basins, but sea level is close to the general nightside terrain level (shallow basins). Therefore mound height above surrounding terrain: **~1.5–3 km**. Central estimate: **2 km** (equatorial biotic mound).

**Pre-biotic mound:**

Without grass or towers, erosion is by laminar ammonia sheet flow (~10 cm depth, spine). Critical shear stress for fine volcanic sediment: τ_c ≈ 1–5 Pa.

Sheet flow shear stress: τ = ρ_NH₃ × g × h × sin(α) = 660 × 17.85 × 0.1 × sin(α) = 1,178 sin(α) Pa

Equilibrium slope (τ = τ_c): sin(α) = τ_c/1178

| τ_c (Pa) | Equilibrium slope (°) | Height at 200 km half-width |
|---|---|---|
| 1 | 0.05° | 175 m |
| 3 | 0.15° | 524 m |
| 5 | 0.24° | 838 m |

**Pre-biotic mound: ~0.3–0.8 km height**, gentle slopes (0.1–0.25°), broad base.

**Biotic mound amplification:**

Grass lattice disrupts sheet flow everywhere (spine: "prevents valley formation"). Effective erosion rate drops by 10–100× on grassed surfaces. Erosion is then concentrated in ungrassed channels (gullies) between tower mounds. The equilibrium profile steepens as the surface is progressively armored.

Biotic mound limited by:
1. **Isostatic compensation** — flexural rigidity of the lithosphere supports loads over length scales < flexural wavelength:
   - λ_flex = 2π(D/ρ_m g)^(1/4) ≈ 400 km (for 50 km elastic thickness)
   - Mound base width (~300 km) is comparable to λ_flex → partial isostatic support
   - A 2 km mound depresses the crust by ~6 km (Airy isostasy with ρ_sed/Δρ_mantle ≈ 3.3) — significant but within flexural limits
2. **Wave erosion on night-side face** — self-stabilizing beach profile, continuous
3. **Gully erosion on day-side face** — concentrated flow in gullies between tower mounds

**Cross-section (equatorial biotic mound):**

| Feature | Width (km) | Slope | Notes |
|---|---|---|---|
| Night-side submarine ramp | ~50–100 | 0.5–1° | Wave-deposited sediment, self-stabilizing |
| Night-side face above water | ~30–50 | 2–3° | Active wave erosion zone at top, gentler below |
| Mound crest plateau | ~30–50 | ~0° (flat) | Tower forest, grass-stabilized |
| Day-side lee face | ~100–200 | 0.7–1.2° average | Carved by gully/canyon systems |
| Mudflat transition | ~5–10 | ~0° | At mound base, ammonia evaporation zone |

**Total mound width at base: ~250–400 km** (angular width: ~1.5–2.4° of arc)

The mound is a subtle feature in planetary terms — a 2 km high, 300 km wide ridge on a 9,700 km radius planet. But it is the dominant topographic feature of the terminator and the foundation of the entire biosphere.

**Day-side (lee) slope detail:**

Average slope 0.7–1.2° = 12–21 m/km. The lee face is carved by ammonia runoff into gully/canyon systems. Between gullies, the grass-stabilized surface is intact. Lee-slope turbulence (spine): wind separates over the crest, creating recirculation, eddies, vortex shedding. The only location on the planet with non-steady, non-unidirectional wind.

Gully spacing: probably 1–5 km (set by tower spacing ~6.5 km and drainage patterns). Gully walls: 5–15° (steeper than overall slope). Gully floors: nearly flat, carrying ammonia runoff.

**Night-side face detail:**

Dynamic equilibrium with ammonia sea waves (spine). Waves are breaking-limited at 1.82g: 10× air/liquid density ratio steepens waves past breaking threshold in open ocean, energy dissipates as whitecap turbulence. Self-stabilizing: erosion at top → deposition at base → gentler submarine ramp → wave energy spread over longer gradient.

### Latitude Dependence

The cross-terminator wind component determines deposition rate. At the equator, Coriolis is zero → flow is purely radial → all wind crosses the terminator → maximum deposition. At higher latitudes, Coriolis deflects flow along the terminator → less cross-terminator transport → thinner mound.

Rossby number at latitude φ: Ro(φ) = v/(2Ω sin φ × R_planet) = 0.121/sin φ

Cross-terminator flow scales as ~min(1, Ro). Mound height ∝ cross-terminator flow:

| Latitude | Ro | Cross-terminator fraction | Mound height (est.) |
|---|---|---|---|
| 0° (equator) | ∞ | 1.0 | ~2 km |
| 10° | 0.70 | 0.70 | ~1.4 km |
| 15° | 0.47 | 0.47 | ~0.9 km |
| 20° | 0.35 | 0.35 | ~0.7 km |
| 30° | 0.24 | 0.24 | ~0.5 km |
| 45° | 0.17 | 0.17 | ~0.35 km |
| 60° | 0.14 | 0.14 | ~0.28 km |
| 80° | 0.12 | 0.12 | ~0.24 km |

**Half-height latitude (mound drops to 1 km): ~14° from equator.**

The mound is a prominent feature (>1 km) only within ±15° latitude of the equatorial terminator. Beyond ±30°, it's a gentle rise of a few hundred meters. The polar gateway (minimal mound, ammonia passes to nightside freely) begins at ~±30–40° latitude.

Prominent mound coverage: ±15° = ~30° of latitude on each side → roughly 1/6 of total terminator circumference (~10,000 km). The remaining ~52,000 km has a thin/absent mound.

### Implications

- The tower network's natural habitat is a band ~300 km wide and ~10,000 km long at the equatorial terminator — not the full 62,000 km circumference.
- Higher-latitude terminator zones (±15° to ±40°) have progressively thinner mounds, less rain, calmer conditions — the "polar gateway" ecology.
- Pre-biotic mound is inevitable even without biology (rain scrubbing delivers sediment). Biology amplifies by ~3–5× in height.
- The mound-base/mudflat transition is where pool genesis operates (spine: shallow ammonia film, continuous replenishment, metal-bearing sediment).

### Uncertainties

- Mound height: ±50% (1–3 km range, spine). Depends on sediment supply rate, compaction, erosion history.
- Latitude scaling: the linear Ro-based model is simplified. Ekman pumping, boundary layer effects, and equatorial convergence enhancement modify the profile.
- Pre-biotic equilibrium slope: depends on sediment grain size and cohesion, poorly constrained.

---

## 4. Mudflat Band

### Assumptions

1. Ammonia evaporates where surface temperature exceeds ~240K.
2. Runoff from the day-side mound slope delivers liquid NH₃ to the mound base.
3. Evaporation rate scales with vapor pressure deficit (Clausius-Clapeyron).
4. Mass transfer coefficient: C_E ≈ 0.001 (Dalton number for turbulent flow over flat surface).

### Derivation

**Angular position:**

The mound base (day side) sits at the reference terrain level where T ≈ 240–242K (the NH₃ dew point). This is at θ ≈ 89° from substellar (the mound crest at θ ≈ 90° sits 2 km above this, at 230K).

The mudflat extends day-ward from the mound base until all ammonia has evaporated.

**Liquid delivery to the mudflat:**

Total rainfall on the day slope: ~10–20 mm/hr average over ~150 km width.

The day slope surface temperature ranges from 230K (crest) to 241K (base). Nearly the entire slope is below 240K (NH₃ dew point), so evaporation on the slope itself is minimal (~10–20% in the bottom 10–20 km). The bulk of rainfall reaches the mound base as liquid.

Flow per unit length of terminator circumference reaching the base:

> Q_base ≈ 0.8 × rainfall_rate × slope_width / ρ_NH₃

> = 0.8 × (0.01/3600 m/s) × 660 × 150,000 / 660 ≈ 0.33 m²/s per meter of circumference

(Here "10 mm/hr" = 10⁻²/3600 m/s of liquid, × ρ to get mass flux, × slope width, then ÷ ρ for volume; the 0.8 factor accounts for 20% re-evaporation on the warm lower slope.)

**Evaporation rate as a function of distance:**

Temperature increases day-ward at ~6 mK/km (from T(θ) gradient near terminator: ~1 K per 169 km). NH₃ saturation pressure:

> P_sat(T) ≈ 1.0 × exp(0.052 × (T − 240)) bar [Clausius-Clapeyron with ΔH_vap/R ≈ 3000K]

Mass transfer rate:

> E(T) = C_E × ρ_air × v × Δw / ρ_NH₃ [m/s of liquid depth]

where Δw = (P_sat − P_amb)/P_total × (M_NH₃/M_air)

| Distance from base (km) | T (K) | P_sat (bar) | ΔP (bar) | E (mm/hr) |
|---|---|---|---|---|
| 0 | 241 | 1.05 | 0.05 | ~2 |
| 50 | 241.3 | 1.07 | 0.07 | ~3 |
| 200 | 242.2 | 1.12 | 0.12 | ~5 |
| 500 | 244 | 1.23 | 0.23 | ~9 |
| 1000 | 247 | 1.44 | 0.44 | ~17 |
| 2000 | 253 | 1.93 | 0.93 | ~36 |
| 3000 | 259 | 2.68 | 1.68 | ~65 |

Integrating evaporation over distance until cumulative evaporation equals Q_base ≈ 0.33 m²/s:

The integral ∫₀ᴸ E(x)dx reaches 0.33 m²/s at approximately **L ≈ 150–300 km**.

**Mudflat width: ~100–300 km** (grading from actively wet to damp)

This is a broad, gently sloping zone — NOT a thin strip. The character transitions across it:

| Sub-zone | Distance from base | NH₃ depth | Character |
|---|---|---|---|
| Active gully mouths | 0–10 km | 5–10 cm | Turbulent, sediment-churning (spine: "punching a pillow") |
| Wet mudflat | 10–50 km | 1–5 cm | Broad sheet flow, slow, continuous deposition |
| Damp mudflat | 50–150 km | 1–5 mm film | Intermittent, evaporites forming on surface |
| Dry edge | 150–300 km | None (damp substrate) | Crust-forming, grades into dry deposition zone |

**Ammonia film depth on the mudflat:**

The spine says ~10 cm sheet flow at the terminator (mound crest). On the mudflat, the flow is MUCH shallower because:
1. The mudflat is nearly flat (slope < 0.01°) → flow velocity ~0.01–0.1 m/s
2. Flow spreads from gully mouths into broad sheets
3. Continuous evaporation thins the flow

Depth decreases from ~5 cm at gully mouths to <1 mm at the dry edge.

**Character:**

The wet mudflat (inner ~50 km) is continuously wet — sustained by permanent rainfall on the mound slope. The damp zone (50–300 km) is intermittently wet — fluctuations in rainfall intensity create pulses. The dry edge forms mineral crusts (deposited sediment from evaporating ammonia).

⚠ **This is the primary genesis environment** (spine). Shallow ammonia film over reworked sediment, continuously replenished, wrapping the entire terminator. Organisms ≤100 μm need only a wet surface. The wet mudflat provides: liquid ammonia (solvent), atmospheric SiH₄ contact (maximum surface-to-volume), metal-bearing sediment, lightning from the terminator storm front.

### Distinction: Mudflat vs Deposition Zone

| Feature | Mudflat band | Deposition zone |
|---|---|---|
| Angular position | θ ≈ 87.5–89° | θ ≈ 50–87° |
| Width | ~100–300 km | ~3,400–6,800 km |
| Surface state | Wet (liquid NH₃) to damp | Dry |
| Sediment source | Runoff-carried mound material | Wind-transported atmospheric fines |
| Sediment depth | Shallow, reworked | Deep (km scale over Gyr) |
| Ecology | Genesis zone, microbial | Sparse (too dry for pool biology, too far for tower) |

### Implications

- The mudflat is a narrow but extremely significant feature — the planet-wide genesis environment.
- Its width (~100–300 km) is sufficient for robust abiogenesis experiments at planetary scale.
- The damp/wet character ensures continuous SiH₄-ammonia contact for organosilicon chemistry.
- The mudflat grades smoothly into the dry deposition zone. No sharp boundary — just progressively drying sediment.

### Uncertainties

- Mudflat width: ±factor of 2 (depends on rainfall rate, evaporation efficiency, flow dynamics).
- The transition from "wet" to "damp" to "dry" is gradual and probably fluctuating.
- Mass transfer coefficient (C_E) is uncertain by ±50% for this exotic atmosphere.

---

## 5. Night-Side Ammonia Distribution

### Assumptions

1. Night-side surface temperature: 215–240K (below dew point everywhere).
2. Night-side seas: 50–200 m depth in basins, NOT hemisphere-spanning (spine).
3. 5–20% of volcanic NH₃ crosses the mound to the nightside (spine).
4. Katabatic wind: night→day, accelerating from 0 m/s (antistellar) to ~9.5 m/s (terminator).

### Derivation

**Sea extent:**

Night-side seas occupy topographic basins — not a continuous ocean. Basin types:
- Volcanic calderas (rare — dark side geologically quiescent)
- Rift basins along terminator flexure zone (chronic cracking)
- Impact craters (ancient, Gyr old, common on stable dark-side crust)
- Tower-scoured basins (near terminator — towers are the only significant roughness element)

Nightside sea depth is uniform across basins (hydrostatic equilibrium, spine). Depth: 50–200 m (narrative knob). The seas are shallow and ancient.

**Ammonia delivery pathway:**

Primary: polar gateway. At latitudes >30–40°, the mound is thin/absent (§3). Atmospheric NH₃ passes to the nightside without significant mound obstruction. The ~5–20% figure is the fraction of terminator rain that crosses the equatorial mound crest; at polar latitudes, the fraction is much higher.

Secondary: residual rain crossing the equatorial mound crest (5–20% of local rainfall).

The nightside receives ammonia as:
1. Rain on the night slope (diminishing, see §2) — feeds coastal/shore zones
2. Atmospheric vapor crossing the terminator at altitude — condenses on the cold night side
3. Katabatic wind carrying NH₃-saturated air from the terminator region

**Transition from mound slope to sea:**

The night-side mound face grades into the ammonia sea. Profile:
1. **Mound face above waterline** (top ~1.5 km): steep (2–3°), wave-eroded, bare sediment/grass
2. **Splash/surf zone** (~0–10 m elevation): wave action, turbulent, rich ecology
3. **Shore/intertidal** (0 to −5 m): most biologically productive marine zone (spine: "primary nutrient delivery")
4. **Submarine ramp** (−5 to −100 m): gentle slope (0.5–1°), extending 3–10 km from shore
5. **Basin floor** (−100 to −200 m): flat, glass fossil pavement, barren

**Shore deposition zone:**

Where katabatic wind (night→day, 2–8 m/s depending on distance from antistellar) meets the ammonia sea surface:
- Wave roughness trips boundary layer from aerodynamically smooth (over peneplain) to turbulent
- Wind carrying capacity drops → particulate falls out
- Width of active deposition: ~0.5–5 km (depends on wind speed and wave state)
- Deposited material: SiC grit, volcanic fines, dead-bug plume debris (catalytic metals, library fragments, SiC plates)

This shore deposition zone is the nutrient delivery system for marine ecology (spine: "primary reason shore/intertidal is the richest marine zone").

### Result: Night-Side Ammonia Zones

| Zone | Distance from terminator | T (K) | Ammonia state |
|---|---|---|---|
| Night mound slope | 0–75 km past crest | 235–240 | Rain diminishing, bare slope |
| Night shore | 75–80 km | ~234 | Surf zone, rich ecology |
| Shallow sea | 80–90 km | ~233 | 0–50 m depth, submarine ramp |
| Basin floor | 90+ km (varies) | 215–233 | 50–200 m, flat, sparse life |
| Dry peneplain | Most of nightside | 215–233 | No liquid (polished bedrock) |
| Antistellar cap | >170° | ~215 | Stagnation, minimal moisture, calm |

### Implications

- Night-side seas are scattered, shallow, ancient. Not a unified ocean.
- Shore ecology is the richest marine zone — nutrient delivery via atmospheric particulate deposition.
- The polar gateway creates an asymmetry: equatorial nightside is more ammonia-starved than polar nightside.
- Dark-side tower basins (tower-scoured depressions) are the primary sea-maintenance mechanism.

---

## 6. Ammonia Availability Zone Map (Summary)

Synthesizing all derivations:

| Zone | θ range | T range (K) | NH₃ state | Width (km) | Character |
|---|---|---|---|---|---|
| **Substellar chimney** | 0–12° | 264–265 | Vapor only | ~2,000 | Volcanic, dry, thermal updraft |
| **Inner day side** | 12–50° | 261–265 | Vapor only, no rain | ~6,400 | Volcanic terrain, wind erosion |
| **Outer day side** | 50–65° | 257–261 | Upper condensation begins (virga) | ~2,500 | Condensation floor descends |
| **Rain onset (aloft)** | 65–78° | 249–257 | Rain aloft, virga at surface | ~2,200 | Superstream rain evaporates in warm lower atmosphere |
| **Surface rain onset** | 78–85° | 245–249 | Light rain reaching surface | ~1,200 | Wetting begins, intermittent |
| **Heavy rain / day slope** | 85–90° | 230–245 | Heavy rain, surface runoff | ~850 | Mound lee face, gullies, continuous rain |
| **Mound crest** | ~90° | ~230 (elevated) | Saturated, peak rain (50–80 mm/hr) | ~40 (plateau) | Tower forest, maximum deposition |
| **Night slope rain** | 90–95° | 230–236 | Rain diminishing | ~850 | Mound windward face, NH₃ depleting |
| **Night shore** | 95–100° | 232–236 | Sea + saturated atm, light rain | ~850 | Shore deposition, marine ecology |
| **Night basins** | 100–170° | 216–232 | Liquid seas in basins, dry elsewhere | ~11,800 | Polished peneplain + shallow seas |
| **Antistellar cap** | 170–180° | 215–216 | Stagnation, minimal moisture | ~1,700 | Polished peneplain, calm, dust cap |

### Key boundaries:

| Boundary | θ | T (K) | Distance from substellar (km) | Significance |
|---|---|---|---|---|
| Upper-level rain onset | ~60° | ~261 | ~10,200 | Superstream rain begins (virga) |
| Surface rain onset | ~80° | ~249 | ~13,500 | First rain reaches ground |
| Mound crest | ~90° | ~230 (elev.) | ~15,200 | Peak rain, tower forest |
| Day-side mound base / mudflat | ~89° | ~241 | ~15,000 | Evaporation boundary, genesis zone |
| Night-side shore | ~95° | ~236 | ~16,000 | Ammonia sea begins |
| Rain cessation | ~105° | ~228 | ~17,700 | Atmosphere wrung dry |

---

## Summary Table of Derived Numbers

| Parameter | Value | Uncertainty | Section |
|---|---|---|---|
| **Temperature profile** | T(θ) = asymmetric tanh, k_d=3.5 / k_n=2.5 | k: ±30% | §1 |
| Day-side gradient at terminator | 0.97 K/° = 5.7 mK/km | ±30% | §1 |
| Night-side gradient at terminator | 0.69 K/° = 4.1 mK/km | ±30% | §1 |
| 240K band width (±5K) | ~10° = 1,700 km | ±3° | §1 |
| Mound crest T (at 2 km elevation) | ~230K | ±5K | §1 |
| **Rain onset (surface)** | θ ≈ 78–82° | ±5° | §2 |
| Rain peak (mound crest) | θ ≈ 90° | Fixed | §2 |
| Rain cessation (night) | θ ≈ 100–105° | ±5° | §2 |
| Average rainfall rate | ~10–20 mm/hr NH₃ | ×2–3 | §2 |
| Peak rainfall (crest) | ~50–80 mm/hr NH₃ | ×2 | §2 |
| Rain column height (crest) | ~18 km | ±3 km | §2 |
| **Mound height (equatorial, biotic)** | ~2 km (range 1.5–3) | ±50% | §3 |
| Mound height (pre-biotic) | ~0.3–0.8 km | ±50% | §3 |
| Mound width (base to base) | ~250–400 km | ±30% | §3 |
| Day-side slope | 0.7–1.2° average | ±0.3° | §3 |
| Night-side slope | 1.5–2° average above water | ±0.5° | §3 |
| Crest plateau width | ~30–50 km | ±20 km | §3 |
| Half-height latitude | ~14° from equator | ±5° | §3 |
| Prominent mound zone | ±15° latitude (~10,000 km) | — | §3 |
| **Mudflat width (wet)** | ~100–300 km | ×2 | §4 |
| Mudflat angular position | θ ≈ 87.5–89° (day-ward of crest) | ±1° | §4 |
| Mudflat NH₃ depth | 5 cm (gully mouths) to <1 mm (dry edge) | — | §4 |
| **Nightside sea depth** | 50–200 m (spine) | Narrative knob | §5 |
| Night-side rain extent | ~10–15° past crest | ±5° | §2, §5 |
| Shore deposition zone width | 0.5–5 km | ±5× | §5 |

---

## Open Questions

### □ Rainfall rate precision
The energy budget gives 10–20 mm/hr average; the peak at the crest is 50–80 mm/hr. These could be refined with a 1D atmospheric column model, but are currently order-of-magnitude only. The main uncertainty is the energy partition between latent heat, sensible heat, and radiation at the terminator.

### □ Mound height quantification
The 2 km central estimate fits the spine's "1–3 km headroom" constraint, but the actual height depends on Gyr of sediment supply vs erosion history. A sediment budget analysis (volcanic ash production rate × delivery fraction × geological time − erosion losses) would tighten this.

### □ Mudflat flow dynamics
The mudflat width calculation assumes simple evaporation from a spreading sheet flow. In reality, the flow is channelized near the mound base (gully mouths), then spreads. The detailed hydrodynamics of the gully-to-sheet transition affect the mudflat character. The spine's description ("punching a pillow") suggests rapid energy dissipation — consistent with a narrow active zone and a broad passive evaporation zone.

### □ Latitude-dependent mound: polar gateway quantification
The mound drops to half height by ±14° latitude (Ro scaling), but the actual transition depends on Ekman pumping and equatorial convergence enhancement. The polar gateway's effective width determines how much ammonia reaches the nightside — this sets the nightside sea volume.

### ✓ Mound crest temperature and tower ecology — RESOLVED
Crest at ~230K (2 km elevation, moist lapse rate ~5 K/km). Local pressure ~5.6 bar, P_NH₃ ~0.69 bar, local dew point ~233K — supersaturated by ~3K (not 10K; pressure drop lowers dew point). Chemistry ~2–3× slower; petrification ~3–7× slower (higher Ea). Net: improved defense/attack ratio. Internal tower gradient: 240K base to 230K apex. Propagated to spine.

### □ Night-side rain zone extent
My estimate of ~10–15° past the crest is rough. The actual extent depends on how much NH₃ remains after the day-slope rain-out and on the supersaturation/condensation dynamics of the cold night-side air. A more careful analysis of the post-crest atmospheric NH₃ budget would constrain the night-side rain cessation point.

### □ Pre-biotic vs biotic mound transition
The pre-biotic mound (0.3–0.8 km) and biotic mound (1.5–3 km) bracket the range, but the transition timescale is interesting. How quickly does the biotic mound grow after grass/towers establish? If the biological amplification factor is ~3–5×, and the deposition rate is ~0.1 mm/yr, the timescale is ~10 Myr — geologically fast.

### □ Deposition zone depth profile
The "20–40° day-ward" deposition zone (spine) accumulates wind-transported sediment over Gyr. At ~0.1 mm/yr deposition rate and 4 Gyr: 400 m of sediment. This may be a significant geological feature — a planet-wide sedimentary basin between the mound and the volcanic day side.

---

*The mound holds. The rain falls. The mudflat waits.*
