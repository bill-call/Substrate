# Session Prompt: Terminator Mound, Mudflat, and Rain Zone Geometry

## Context

You are working on **Substrate**, a hard-SF world-building project set on a tidally locked super-Earth. This session's goal is to derive the **physical characteristics and spatial extents** of the terminator mound, the day-side mudflat band, and the rain/condensation zone — the three most important surface features for understanding the planet's ecology and civilization.

**Why this matters:** The tower network's natural geometry is a ring along the terminator mound crest. How far the network can extend day-ward or night-ward, whether organisms can survive off the mound, and where civilizational frontiers form all depend on the mound's dimensions, the rain zone's width, and the mudflat band's extent. These are currently under-constrained.

---

## Load Order

1. This prompt (read fully before starting).
2. `substrate_spine.md` — hard constraints. Trust everything in it.
3. `substrate_planetary_geology_hub.md` — mantle model, volcanism, sediment processes.
4. If needed for cross-reference: `substrate_silicon_chemistry_hub.md` (PCS chemistry), `substrate_bible.md` (full reference, large — use for targeted lookups only).

---

## Planetary Parameters (from spine — do not re-derive)

### Star & Orbit
- M3V red dwarf, 0.36 M☉, 3400 K, 0.015 L☉
- Planet at 0.12 AU, tidally locked 1:1, 18-day period
- No precession, no obliquity, no seasons

### Planet
- 4.2 M⊕, 1.52 R⊕ (R_planet ≈ 9,700 km)
- Surface gravity: 17.85 m/s² (1.82g)
- Circumference at equator: ~61,000 km

### Atmosphere
- 8 bar total pressure
- Composition: N₂ 55%, H₂ 15%, NH₃ 12.5%, CH₄ 10%, He+Ar ~7%, SiH₄ 0.3%
- Mean molecular weight: 20.5 g/mol
- Scale height: 5.5 km
- cp: 1,450 J/(kg·K); volumetric heat capacity ~10× Earth
- Air density at terminator (240K): 8.2 kg/m³
- Albedo: ~0.45

### Temperature Profile
| Location | Temperature | Angular distance from substellar |
|---|---|---|
| Substellar point | 265K | 0° |
| Terminator | 240K | 90° |
| Antistellar point | 215K | 180° |
| Total ΔT | 50K | — |

The 50K gradient is suppressed by the massive atmosphere + NH₃ latent heat cycle. The temperature profile is NOT linear with angle — the day side is warmer and more uniform (strong mixing), the gradient steepens near the terminator (latent heat release), and the night side is cold and more uniform (stable stratification). Derive or adopt a physically motivated T(θ) profile.

### Vertical Structure
- Dry adiabatic lapse rate: ~12.3 K/km
- Moist adiabatic lapse rate: ~5 K/km (NH₃ latent heat 1374 kJ/kg at 12.5% mixing ratio)
- Condensation floor (day side): rises with T_surf — 4.6 km at 280K, 2.4 km at 260K, 1.2 km at 250K, reaches surface at 240K (terminator)
- Tropopause / superstream: ~12–16 km altitude
- Superstream PASSES THROUGH the NH₃ condensation zone (surface to ~18 km at terminator). Rain scavenging begins well dayside of the mound crest.

### Wind
- Surface wind: unidirectional night→day everywhere
- Anti-stellar: ~0 m/s (stagnation)
- Dark side: 2–8 m/s accelerating toward terminator
- Terminator: ~9.5 m/s sustained
- Day side: decelerating toward substellar, then ~17 m/s thermal chimney near substellar
- v(θ) = v_term × (sin θ)^(−1/4) for θ ≈ 12°–90° from substellar

### Key Constraints
- NH₃ condensation/dew point at 1.0 bar partial pressure ≈ 240K = terminator temperature
- NH₃ boiling point at 8 bar total: ~293K (well above substellar 265K, so liquid NH₃ never boils on the surface — it evaporates into unsaturated air)
- NH₃ freezing: 196K (below antistellar 215K — no surface ice anywhere)
- SiH₄ is a permanent gas (bp 161K) — passes through the rain column unaffected. Available planet-wide.
- H₂O is a trace oxidizer, not a solvent. Biological poison (causes petrification).

---

## What to Derive

### 1. Temperature Gradient Map: T(θ)
Derive a physically motivated surface temperature profile as a function of angular distance θ from the substellar point. Account for:
- Stellar flux: goes as cos(θ) on the day side, zero on the night side
- Atmospheric heat transport: single planet-wide overturning cell, enormous heat capacity (10× Earth), 8 bar
- NH₃ latent heat buffering at the terminator (condensation releases heat on night side, evaporation absorbs on day side)
- The known anchor points: 265K (substellar), 240K (terminator), 215K (antistellar)

Deliverable: T(θ) curve or piecewise function. Identify the angular width of the 240K isotherm band (how wide is "the terminator" in temperature terms?).

### 2. Rain Zone Geometry
Where does ammonia rain fall? The superstream (upper-level return flow, day→night) carries warm, NH₃-laden air from the day side. As it cools through the dew point, condensation begins. The spine says rain scavenging begins "well dayside of the mound crest."

Derive:
- **Rain onset**: how far day-ward of the terminator does significant rainfall begin? (Angular distance from substellar where upper-level air first reaches dew point.)
- **Rain peak**: where is rainfall heaviest? (Probably near the mound crest where the full column is at or below dew point.)
- **Rain cessation on the night side**: how far past the terminator does rain continue before the atmosphere is wrung dry?
- **Rain column height at the terminator**: the condensation zone extends from the surface (240K) to ~18 km. How does this vary with position?
- **Rainfall rate estimate**: order-of-magnitude, in mm/hr equivalent or kg/m²/hr. The NH₃ latent heat cycle is intense (12.5% mixing ratio, 1374 kJ/kg latent heat).

The spine notes that ~80–95% of rainfall lands on the dayside slope of the mound. Only ~5–20% crosses the crest to the nightside.

### 3. Mound Dimensions
The terminator mound is an accretional sediment wedge built by atmospheric deposition over geological time, amplified by tower biology. It wraps the entire terminator circumference (~62,000 km at equator, shorter near poles).

Derive or constrain:
- **Mound crest height above surrounding terrain**: the mound is built from deposited particulate (volcanic ash, atmospheric fines scrubbed by rain, biological debris). What limits its height? Consider: isostatic compensation (1.82g), sediment compaction, erosion equilibrium between rain runoff (day-side face) and wave action (night-side face).
- **Day-side (lee) slope**: carved by ammonia runoff. Gully/canyon systems. What angle? How far does it extend before reaching ambient terrain level?
- **Night-side (windward) slope**: dynamic equilibrium with ammonia sea waves. Self-stabilizing beach profile. What angle?
- **Mound width at base**: sum of both slopes.
- **Latitude dependence**: at the equatorial terminator, the superstream converges head-on (radial flow, Coriolis zero at equator) → maximum deposition, thickest mound. At polar terminator, flow is deflected along the terminator (strongly geostrophic) → thin or absent mound, "polar gateway" for ammonia to pass to nightside. Derive or estimate how mound height varies with latitude.
- **Pre-biotic vs biotic mound**: pre-biotic equilibrium is shallower (no grass stabilization, no tower breakwaters). Biology amplifies height and steepness. Estimate both profiles if possible.

### 4. Mudflat Band
The day-side slope terminates in the **mudflat band** — a planet-wide zone where ammonia runoff evaporates, depositing carried sediment.

Derive:
- **Angular position**: the mudflat forms at the ~240K isotherm on the day-side slope (where ammonia evaporates). How far day-ward of the terminator is this?
- **Width**: how wide is the mudflat band? (From active runoff zone to fully dry terrain.)
- **Depth of ammonia film**: the spine says ~10 cm sheet flow at the terminator. What about on the mudflat (lower flow rate, evaporating)?
- **Character**: continuously wet? Intermittently wet? Crust-forming?

### 5. Night-Side Ammonia Distribution
- **Sea extent**: the spine says nightside seas are "50–200 m depth in basins" and "NOT hemisphere-spanning." Most nightside terrain is dry peneplain. Where are the seas? (Topographic lows — volcanic calderas, rift basins, terminator flexure depressions.)
- **Transition from mound slope to sea**: the night-side face of the mound grades into the ammonia sea. What does this transition look like?
- **Shore deposition zone**: where katabatic wind meets ammonia surface, boundary layer trips turbulent, particulate deposits. Width and character of this zone?

### 6. Ammonia Availability Zones (Summary Map)
Synthesize all of the above into a zone map from substellar to antistellar:

| Zone | Angular range (from substellar) | T range | Ammonia state | Character |
|---|---|---|---|---|
| Substellar chimney | 0–12° | ~265K | Vapor only | Volcanic, dry, thermal updraft |
| Inner day side | 12–50° | 260–265K | Vapor only, no rain | Volcanic terrain, wind erosion |
| Outer day side | 50–?° | 250–260K | Rain onset aloft, dry surface | Upper-level condensation begins |
| Rain zone (day slope) | ?–90° | 240–250K | Rain reaching surface | Mound lee slope, gullies, runoff |
| Mound crest | ~90° | ~240K | Saturated, heavy rain | Tower forest, maximum deposition |
| Rain zone (night slope) | 90–?° | 235–240K | Rain diminishing | Mound windward slope, shore |
| Night-side shore | ?–?° | 230–235K | Sea + atmosphere saturated | Shore deposition, marine ecology |
| Night-side basins | ?–170° | 215–230K | Liquid seas in basins, dry elsewhere | Peneplain + shallow seas |
| Anti-stellar cap | 170–180° | ~215K | Stagnation, minimal moisture | Polished peneplain, calm |

Fill in the `?` values with your derived numbers. Adjust zone boundaries as the physics dictates.

---

## Methodology Notes

- This is a physics derivation exercise, not creative writing. Show your work. State assumptions explicitly.
- Use order-of-magnitude estimates where precision is impossible. Flag uncertainties.
- The 8-bar, high-heat-capacity atmosphere is doing enormous work to suppress temperature gradients. Don't underestimate atmospheric heat transport.
- The NH₃ latent heat cycle is the dominant weather driver. 12.5% mixing ratio × 1374 kJ/kg = massive energy flux at the condensation boundary.
- Gravity is 1.82g. This affects: sediment compaction, slope stability, wave dynamics, atmospheric scale height, rainfall terminal velocity.
- The mound is a SEDIMENT feature, not bedrock. It compacts, erodes, and can be reshaped by biological activity.
- Latitude matters. Equatorial terminator ≠ polar terminator. Derive the equatorial case first, then discuss how it varies with latitude.

---

## Output Format

Structured sections matching the 6 questions above. Each section should include:
1. Key assumptions
2. Derivation (show work)
3. Result (with uncertainties)
4. Implications for ecology/civilization (brief)

Final summary table of all derived numbers.
