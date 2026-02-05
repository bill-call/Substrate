# Substrate Tower Forest Simulation — Project Brief

## Context

You are helping build a simulation of tower forest evolution on a fictional tidally locked super-earth. This is worldbuilding for a science fiction project called **Substrate**. The world has silicon-based life, a hydrogen-methane-silane atmosphere, and kilometer-tall mineral tower structures that are biological organisms (colonial symbiotes depositing conductive mineral, analogous to coral reefs). 

The attached documents contain the full worldbuilding. Read all of them before starting. The physics is load-bearing — every mechanism described is derived from first principles and the simulation must respect the established constraints.

**Attached documents you must read first:**
- `substrate_bible_v2_1.docx` — The master reference. All established parameters.
- `substrate_marching_towers.docx` — Detailed expansion on wind, erosion, tower migration, and planetary geography.
- `substrate_tower_lifecycle.docx` — Addendum correcting and extending the tower documents. **This supersedes conflicting information in the other two documents.** Key corrections: dark-side migration direction is day-ward (not poleward); deposition zone is directionally fed and particle-sorted; ant logistics is a unified root-network adaptation.

## What the Simulation Must Model

The tower forest evolves over billions of years on the surface of this planet. Towers are biological structures that grow, migrate, reproduce (nucleate new towers), and die. The simulation should produce a map of tower positions, sizes, shapes, ages, and connectivity that can be visualized and used to inform the fiction.

### Core Variables

**Wind field** (the driver of everything):
- Permanent katabatic circulation: cold dense air flows from the anti-stellar pole across the dark side, through the terminator, and onto the day side where it warms, rises, and returns at altitude.
- Anti-stellar pole: ~0 m/s surface wind.
- Dark side (pole to terminator): 5–30 m/s, accelerating toward the terminator. Steady, laminar.
- Terminator: 50–80 m/s sustained. Permanent hurricane. Maximum turbulence.
- Day side past terminator: rapid deceleration. 15–25 m/s in the deposition zone (20–40° day-ward), dropping to 5–10 m/s deeper, near-calm at substellar point.
- Wind direction is unidirectional: dark-to-day everywhere on the surface.

**Atmospheric density**: 0.9 kg/m³ at terminator (270 K). Varies with temperature: 0.69 at substellar (350 K), 1.35 at anti-stellar (180 K). Substantial up to tower heights — 63% of surface density at 10 km altitude. Scale height 21.8 km.

**Erosion — the aerogel self-recycling model**:
- **CRITICAL UPDATE**: The tower lattice is a mineral aerogel — nanoscale to microscale semiconductor foam. Mostly void by volume. This changes the erosion model fundamentally.
- Wind hitting the porous aerogel surface shatters individual struts, liberating dust-sized mineral fragments.
- At the stagnation point (dead center of windward face, wind hits perpendicular): fragments are blown straight back into the porous matrix and reembedded. Symbiotes metabolize the reembedded material. Recapture is near-perfect. Net erosion approaches zero.
- As the angle of incidence increases around the circumference toward the flanks: the local airflow becomes increasingly tangential. Fragments liberated from the surface are carried *along* the surface rather than back into it. Recapture efficiency drops. Net erosion increases.
- Maximum net erosion likely occurs at an intermediate angle (45–60° from stagnation) where there is still enough normal force to shatter the surface but the tangential flow is strong enough to carry fragments away.
- At the true flanks (90° from stagnation): very little normal force, very little shattering, but zero recapture. Low erosion, but any erosion that occurs is total loss.
- The NET erosion rate is a tiny fraction of the gross shattering rate, because most shattered material is recaptured. Migration is much slower than the original sand-dune model predicted.
- Erosion threshold still exists: below a minimum wind speed, the wind cannot shatter aerogel struts. This still defines the deposition zone boundary.

**Tower biology — the aerogel model (supersedes coral/sacrificial-crust model)**:
- The tower is mineral aerogel throughout. Symbiotes live within the material at every point — the matrix is open at their scale. Gas diffuses through the aerogel like air through a sponge.
- Photovoltaic capture and silane metabolism happen throughout the volume, not just at a surface layer.
- The windward face is the tower's primary feeding surface: wind pressure pushes atmosphere and particulates into the porous matrix. The tower eats through its windward face.
- No sacrificial crust. No subsurface living layer. The entire structure is alive and functional at every point. The windward surface is self-recycling (see erosion model above), not a dead ablation shield.
- The self-recycling equilibrium is razor-thin and absolutely stable because the tidally locked planet provides zero environmental variation. Symbiotes have had billions of years to tune their metabolic rate to exactly match local erosion. No seasons, no storms, no variation. Every day is the same day.
- Diameter constraint still applies: gas diffusion path length limits maximum cross-section width. But the constraint is gentler than previously assumed because the aerogel is porous throughout, not dependent on surface-to-interior diffusion alone.
- Towers do not die of old age. Mineral persists indefinitely in the reducing atmosphere.

**Tower migration — revised mechanism**:
- NOT the sand dune mechanism. Material is not transported over the crest.
- Windward face: net erosion from the small fraction of dust that escapes recapture (primarily from the flanks and intermediate angles where tangential flow prevents reembedding).
- Leeward face: net accretion from atmospheric particulates trapped in the porous matrix from the wind shadow.
- Center of mass moves day-ward due to the differential, but the rate is much slower than the original estimate because windward self-recycling recaptures most eroded material.
- Migration rate is a function of: wind speed, incidence-angle-dependent recapture efficiency, particulate flux, and biological repair rate. The simulation should explore a wide range.
- Migration stops when wind drops below the aerogel-shattering threshold.
- ALL migration is day-ward.

**Tower nucleation**:
- New towers nucleate from the living surface root network when signal latency (round-trip ping) between the advancing root edge and the nearest existing tower crosses a critical threshold.
- The root network is alive — symbiotes along its length, concentrated at advancing edges.
- Mobile middle-kingdom organisms ("ants") transport material from established towers along the root to the growth front, accelerating root extension and early tower growth.
- Nucleation trigger is purely local: the symbiotes at the latency threshold begin vertical accretion because a growing heap improves local signal conditions.
- Two formation types:
  - **First-generation**: deep-rock colony reaches surface through geological fracture. No prior surface infrastructure.
  - **Network-generation**: surface root network extends to latency threshold from existing tower. Has full logistics support from day one. Grows dramatically faster.

**Tower spacing — wind-modified Fibonacci**:
- Each tower creates a latency inhibition zone around itself (the area within its ping threshold where no nucleation occurs).
- New towers nucleate where coverage is weakest (farthest from existing towers).
- This is mathematically equivalent to Fibonacci phyllotaxis. Packing tends toward hexagonal.
- Wind breaks radial symmetry: root extension is faster day-ward, slower crosswind. Inhibition zones are ellipses elongated downwind.
- Result: Fibonacci packing compressed crosswind, stretched downwind.
- Spacing varies by region based on root mineral conductivity and network latency tolerance.

**Sheltering and local wind modification**:
- Towers in a forest shelter each other. Upwind towers create wind shadows on downwind neighbors.
- Sheltering reduces local erosion on sheltered faces and modifies the incidence-angle distribution around the cross-section.
- Non-uniform sheltering causes tower warping over geological time. Towers in dense forests develop asymmetric profiles shaped by their neighbors' wind shadows.
- The deposition zone boundary is pushed outward by the wind shadow of existing stopped towers. New arrivals stop further out than previous generations, creating chronological banding.

**Tower cross-section shape — a key simulation target**:
- The equilibrium cross-section is NOT circular. Self-recycling efficiency varies with incidence angle around the circumference (see erosion model). The center of the windward face holds; the flanks erode. The shape elongates in the wind direction.
- For steady-state migration without distortion, every point on the windward surface must recede at the same rate in the wind direction. The recession rate normal to the surface at angle θ from stagnation must equal the migration velocity × cos(θ). This is a free-boundary problem.
- Qualitative prediction: "bullet" or "rounded wedge" profile. Blunt convex windward face (where self-recycling is most efficient), tapering flanks (where tangential flow prevents recapture), accreting leeward face.
- The exact profile depends on the functional relationship between incidence angle and recapture efficiency, which depends on the aerodynamics of flow around the current shape — a coupled problem that likely requires numerical solution.
- **This cross-section shape problem should be the FIRST thing simulated.** It is a 2D problem (wind direction × crosswind) that can be solved for a single tower in isolation before tackling the full forest simulation. Get the equilibrium cross-section right, then use it as the tower primitive for the larger simulations.

**Deposition zone dynamics**:
- Particulate deposition is directional — material arrives on the katabatic flow from the terminator.
- Sorting by particle mass and cross-section: heavy particles drop first (leading edge), fine particles carry further (deeper in zone).
- Front-row towers intercept airborne particulates, shadowing towers behind them. Compounding advantage for front row.
- Shadowed towers are fed by ant logistics carrying ground-level sedimentary material upward.
- The deposition zone's material wealth may be largely fossil — accumulated when the migration corridor was less crowded.

**Surface root trails ("slime trails")**:
- Migrating towers leave permanent mineralized trails — conductive biomineral deposited at the base, abandoned as the tower moves day-ward.
- Trails persist indefinitely in the reducing atmosphere (no corrosion).
- At the terminator, wind erosion degrades older trail sections. Persistence is centuries to millennia.
- In the deposition zone, trails persist permanently. Dense fossil archive.
- Overlapping trails from successive towers merge into broad conductive bands (migration corridors).
- Trails provide network connectivity (low bandwidth — single thin trace vs. dense lateral mesh).

**Ant logistics**:
- Mobile middle-kingdom organisms follow EM field gradients and free electron flow through the lattice. Tropism-level response. No cognition.
- EM fields and free electrons function as pheromone trails: stronger signal → more ants → more material delivered → healthier lattice → stronger signal. Positive feedback.
- Self-pruning: dead paths lose signal, ants stop coming, resources redirect automatically.
- Same adaptation serves all lifecycle phases: root extension, tower nucleation, tower growth, deposition-zone feeding.

**Death**:
- Pre-atmospheric-crisis: death only by catastrophe. Volcanic events are the primary threat (see below).
- Atmospheric crisis: silane depletion + oxidizer accumulation kills symbiote colonies that can't adapt. Accretion stops. Erosion wins. Tower shrinks.
- Network cascade failure during crisis: the network's automatic wound-healing response (divert resources to struggling neighbors) becomes the collapse vector when resources are globally scarce. Helping kills. Thin zones fail first; rescue response drains surrounding regions; collapse propagates outward.

**Volcanic events**:
- Magma surges from below destroy deep-rock colony fracture networks.
- Spectrum: minor incursion (bandwidth dip, centuries to recover) → major surge, surface intact (deep network killed, slow reseeding from towers, millions of years) → caldera collapse (surface breached, towers fall, cascade structural damage).
- Volcanic scars persist as "thin zones" — bandwidth-starved, culturally distinct regions that are the leading edge of failure during the atmospheric crisis.
- Day side is volcanically active (thin lithosphere). Dark side is quiescent (thick, cold lid). Terminator is a flexure zone with chronic faulting.

### Simulation Scope

**Phase 0: Cross-section equilibrium (2D, single tower, HIGHEST PRIORITY):**
- A 2D cross-section perpendicular to the tower's vertical axis.
- Uniform wind from one direction.
- Model the aerogel surface as a boundary that erodes and accretes.
- Erosion model: at each point on the windward surface, compute the local wind incidence angle. Shattering rate depends on normal component of wind. Recapture probability depends on the ratio of normal-to-tangential flow — high recapture at near-perpendicular incidence, dropping toward zero at tangential incidence. The functional form of this relationship is the key unknown — explore linear, cosine, and threshold models.
- Accretion model: leeward surface traps particulates from the wind shadow. Rate depends on particulate flux and local turbulence.
- Biological repair: symbiotes metabolize reembedded material and fresh particulates. Repair rate is tuned to match local erosion (the red-dwarf equilibrium). Model as a rate-limited process that consumes available material.
- Start from a circular cross-section. Run until the shape reaches steady state (migrating without distorting).
- Output: the equilibrium cross-section profile at various wind speeds. How does the shape change from gentle dark-side winds to terminator gales? How "bullet-like" is it?
- Sensitivity analysis: vary the recapture-efficiency function and see how the profile responds. Which parameter matters most?

**Phase 1: 1D transect (minimum viable forest simulation):**
- A 1D transect along the wind direction, from anti-stellar pole to substellar point.
- Towers as objects with: position, height, cross-section width (using the equilibrium profile from Phase 0), age, migration rate, root connections.
- Wind as a 1D field: speed as a function of position along the transect, modified by local sheltering from neighboring towers.
- Each timestep (suggest 1,000–10,000 year increments):
  1. Calculate local wind at each tower (base wind field minus sheltering from upwind neighbors).
  2. Compute net erosion using the aerogel self-recycling model: gross shattering minus recapture, yielding a small net loss from the windward face. Rate depends on wind speed and the recapture-efficiency function from Phase 0.
  3. Accrete leeward faces proportional to particulate flux and silane access + ant-delivered material.
  4. Update tower position (center of mass shift from differential erosion/accretion).
  5. Grow roots day-ward from each tower. Check ping latency. Nucleate new tower if threshold crossed.
  6. Deposit particulates: carry particulate load in the wind, drop proportional to wind deceleration. Track where material accumulates (deposition zone sorting).
  7. Age and grow stopped towers (accretion without erosion, rate depending on available material).
- Run for ~1 million steps at 1,000 years = 1 billion years.
- Output: tower positions, sizes, ages, density profile along the transect. Visualize the deposition zone structure.

**Phase 2: 2.5D forest simulation:**
- 2D surface (wind-parallel and crosswind axes).
- Towers as objects with position (x, y), height, cross-section profile (from Phase 0, potentially modified by local sheltering).
- Wind as a 2D vector field (primarily unidirectional but with local perturbation from tower shadows).
- Shadow-casting for wind sheltering: ray-march from wind direction, compute sheltered zones behind each tower.
- Fibonacci spacing should emerge naturally from the ping-latency nucleation mechanism — verify this.
- Tower warping from non-uniform sheltering: track how neighbors' wind shadows distort the equilibrium cross-section. Towers in dense forests develop asymmetric profiles.

**Phase 3: Dream simulation (3D):**
- Full 3D aerogel structure. Airflow modeled around porous bodies. Erosion and recapture at the matrix level. This is probably unnecessary for worldbuilding purposes but would produce stunning visualizations and definitively answer the cross-section shape question.

### Key Questions the Simulation Should Answer

1. **What is the equilibrium cross-section shape?** (Phase 0, highest priority.) Given the angle-dependent self-recycling efficiency of an aerogel surface in steady wind, what profile does a single tower converge to? How does it vary with wind speed? Is it a "bullet"? A "rounded wedge"? How elongated? This determines the visual appearance of every tower on the planet.

2. **Does the deposition zone form orderly chronological bands, or something messier?** The hypothesis is that wind-shadow from existing stopped towers pushes the stopping point outward for each generation of arrivals, producing ranked layers. Does this hold?

3. **What does the tower density gradient look like along the wind direction?** From sparse dark-side towers through the terminator factory to the dense deposition zone — what's the actual profile?

4. **Does Fibonacci spacing emerge from the ping-latency nucleation mechanism?** It should. Verify, and characterize the wind-modified distortion.

5. **How badly do towers warp in a forest?** In a dense forest with complex sheltering patterns, how does the equilibrium cross-section (from Q1) get distorted by neighbors' wind shadows?

6. **What is the actual migration rate under the aerogel self-recycling model?** The original 1 mm/year estimate assumed conventional erosion. With most shattered material being recaptured, the net rate could be orders of magnitude slower. What range of recapture-efficiency functions produce migration rates consistent with the narrative (towers must migrate from terminator to deposition zone within the planet's geological history)?

7. **How does the particulate shadowing evolve over time?** Do front-row deposition-zone towers really starve the back row? How steep is the gradient?

8. **What happens when a volcanic event removes a cluster of towers?** How quickly does the network fill the gap (network-generation nucleation with ant logistics)? What does the scar look like after various recovery periods?

9. **Does the system reach a steady state, or is it always evolving?** Is there an equilibrium tower density for each wind-speed zone, or does the forest keep getting denser forever?

### Technical Notes

- The simulation does not need to model individual symbiotes or ants. These are implicit in the growth and logistics rules.
- **The aerogel self-recycling model is the current accepted physics.** Earlier documents may reference a "sacrificial crust" or "sand dune mechanism" — these are superseded. The simulation should use the aerogel model: angle-dependent erosion, self-recapture of shattered dust, and biological repair tuned to match local erosion rate.
- The key free parameter is the recapture-efficiency function: how does the probability of a shattered dust particle being recaptured vary with the wind incidence angle at the point it was liberated? This function determines the cross-section shape, the migration rate, and the energy budget. Explore multiple functional forms.
- Gravity is 1.82x Earth. This affects structural limits (maximum tower height from compressive self-weight of aerogel) but not the migration/nucleation mechanics directly.
- The tower material is aerogel — mostly void by volume, strong in compression, shockingly light. The compressive limit for a kilometer-tall aerogel column in 1.82g is a constraint the simulation should check but probably does not violate.
- The atmosphere is reducing (no free oxygen). Nothing corrodes. Nothing burns. Mineral persists indefinitely unless physically eroded.
- Temperature varies across the surface: 350 K (substellar) to 180 K (anti-stellar). This affects atmospheric density and therefore wind dynamics, but the primary driver is the thermal gradient creating the katabatic circulation.
- The planet rotates once per 18 days. Coriolis effects are nearly negligible (Rossby number > 1 above ~30 m/s at planetary scale). The wind is thermally direct, not geostrophically balanced.

### Output Goals

The ultimate deliverable is a set of visualizations and data that can inform the fiction:
- A map of tower positions, sizes, and ages across the planet surface (or a representative transect).
- The structure of the deposition zone in detail.
- Tower morphology: what do individual towers look like after billions of years of growth in a forest?
- Time-lapse of the forest's evolution: how does the pattern change from first colonization to maturity?
- Sensitivity analysis: which parameters matter most for the large-scale geography?

The author needs to be able to describe what a character sees when they look at the tower forest from various locations on the planet. The simulation provides that visual ground truth.
