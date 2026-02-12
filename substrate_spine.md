**SUBSTRATE — SPINE**

Hard constraints only. No prose. Load with topic modules.

February 2026 v2.4

## STAR

| Parameter | Value |
|---|---|
| Type | M3V red dwarf, 0.36 M☉, 3,400 K |
| Luminosity | 0.015 L☉. Peak ~850 nm (matches Si bandgap) |
| UV | <1% solar. Stabilizes reducing atmosphere |
| Lifetime | >200 Gyr. Habitable zone ~0.12 AU |

## PLANET

| Parameter | Value |
|---|---|
| Mass / Radius | 4.2 M⊕ / 1.52 R⊕ |
| Surface gravity | 17.85 m/s² (1.82g) |
| Orbit | 0.12 AU, 18-day period, tidally locked 1:1 |
| Escape velocity | 18.6 km/s. Δv to LEO ~18 km/s |

### Atmosphere

| Parameter | Value |
|---|---|
| Pressure | 8 bar |
| Composition | N₂ 55%, H₂ 15%, NH₃ 12.5%, CH₄ 10%, He+Ar ~7%, SiH₄ 0.3% |
| Mol. weight | 20.5 g/mol (Earth: 29). Scale height: 5.5 km (Earth: 8.4) |
| cp | 1,450 J/(kg·K) — 1.4× Earth. Volumetric heat capacity ~10× Earth |
| Sound | 369 m/s (1.08× Earth) |
| Character | Reducing. No free O₂. N₂-dominated |
| Albedo | ~0.45 (ammonia cloud/haze layer) |
| Sky | Amber/copper. Precip: NH₃ rain at terminator, HC drizzle, silane snow, glow-snow |

**⚠** 8 bar at 6.8× Earth sea-level density. Wind force at 9.5 m/s ≈ 25 m/s (56 mph) on Earth.

**⚠** No liquid water. NH₃ compatible with Si-Si. H₂O is a trace oxidizer (causes petrification).

### Temperature Profile

| Location | Temperature | Notes |
|---|---|---|
| Substellar | 265K (−8°C) | Warmest surface point |
| Terminator | 240K (−33°C) | NH₃ condensation line (dew point ≈ saturation pressure at 1.0 bar partial) |
| Antistellar | 215K (−58°C) | Coldest point. Above NH₃ freezing (196K) — no surface ice |
| ΔT | 50K | Suppressed by 8-bar atmosphere + NH₃ latent heat cycle |

### Density by Zone

| Zone | Temperature | Air Density |
|---|---|---|
| Substellar | 265K | 7.4 kg/m³ |
| Terminator | 240K | 8.2 kg/m³ |
| Anti-stellar | 215K | 9.2 kg/m³ |

### Liquids

| Liquid | Location | Properties |
|---|---|---|
| Ammonia seas | Terminator basins (rain-fed, marginally stable) and night-side basins (stable, growing). Condensation line = terminator. | ~660 kg/m³. Amorphs sink. |
| Hydrocarbon lakes | Deep dark side. Ethane/propane. | ~450–550 kg/m³ |

## GEOLOGY

**✓** Stagnant lid. No plate tectonics, no subduction. Heat escapes via mantle plumes.

**✓** Hemispheric asymmetry: day-side lid thinner/warmer, plumes breach preferentially. Dark-side lid thick/cold/stable.

| Zone | Description |
|---|---|
| Day side | Volcanically active. 10–30 provinces simultaneously. ~100 Myr resurfacing. Continuous, not episodic. Source of SiH₄ + H₂O outgassing. |
| Dark side | Geologically quiescent. Ancient stable crust. Minimal volcanism. |
| Terminator | Lithospheric flexure zone. Chronic cracking/faulting. Primary fracture networks. |
| Fracture networks | Discontinuous. Each isolated system hosts independent deep-rock colony. |
| Sea basins | Volcanic: calderas, rift basins, terminator flexure depressions. |
| Metal ores | Native metals (reducing atm = no oxidation). Concentrated by magmatic differentiation + NH₃ hydrothermal. Day-side volcanic provinces. |
| Fissile materials | U/Th present (~4.2× Earth inventory). Magmatic + NH₃-hydrothermal concentration. |
| Atm. silane budget | Volcanic SiH₄ ~1000 Tg/yr at peak, currently declining. One-way cycle (no subduction). Crisis = production below consumption. |

**✓** Volcanic regime: continuous day-side plume volcanism (~80–100 km³/yr magma, 10–30 provinces simultaneously). No episodic global lid overturn — hemispheric asymmetry is a permanent pressure-release valve.

**✓** Day-side resurfacing interval: ~100 Myr. Dark-side plume breakthrough: rare (~500 Myr–1 Gyr), localized, not global overturn.

**✓** Volcanism is a chemical hazard, not thermal. Stellar heating is ~1600× internal heat. No volcanic winters. All volcanic threats are atmospheric chemistry.

**✓** SiH₄ formed by pressure-driven equilibrium at depth (Si + 2H₂ → SiH₄, P(SiH₄) ∝ P(H₂)², kinetically trapped during ascent). Temperature helps (endothermic, van 't Hoff) but pressure dominates.

**✓** Silicon cycle is one-way: SiH₄ → biological Si → SiC/SiO₂ surface deposits (permanent). No subduction = no recycling to mantle. Only fresh mantle processing regenerates SiH₄.

## WIND

| Zone | Speed | Notes |
|---|---|---|
| Anti-stellar pole | ~0 m/s | Stagnation point. Calmest. Paired anticyclonic divergence. |
| Dark side | 2–8 m/s | Accelerating toward terminator. S-shaped paths (Coriolis). |
| Peak (~30–40° from anti-stellar) | ~10 m/s | Maximum surface wind |
| Terminator | ~9.5 m/s sustained | Unidirectional (night→day). ~15° Coriolis deflection at mid-latitudes. |
| Day side (within 20–30°) | 5–8 m/s | Accelerating toward substellar (convergent geometry) |
| Day side (within 40–50°) | 2–4 m/s | Accelerating |
| Substellar | ~17 m/s peak at θ≈12° | Thermal chimney. Paired cyclonic Rossby gyres at mid-latitudes. |

**✓** Velocity field (axisymmetric, ignoring vortices): v(θ) = v_term × (sin θ)^(−1/4), where θ = angular distance from substellar point. Valid θ ≈ 12° to 90°. Wind accelerates toward substellar point due to spherical convergence. See `super_earth_analysis (1).md` §2.4 for full vector field.

**✓** Coriolis: significant at planetary scale. Ro ≈ 0.17 at terminator wind speeds (9.5 m/s, f = 5.7×10⁻⁶ at 45°, L = R_planet). S-shaped surface flow paths. ~15° deflection at mid-latitude terminator. Zero at equator. Paired cyclonic gyres flank the substellar point; paired anticyclonic features at anti-stellar. Equatorial superrotating jet at altitude (50–100+ m/s). Standing Rossby wave patterns on dark side create permanent convergence/divergence zones.

**✓** Substellar region is DRY. Thermal chimney lifts hot ammonia-vapor-laden air aloft. Rain falls where upper-level outflow cools through dew point (~240K) — at and night-ward of the terminator. Day side is the evaporator, not the condenser.

**✓** No terminator convergence updraft. Surface flow is unidirectional (night→day) at all points. Shear layer between surface katabatic flow and upper-level return flow (opposite directions) produces Kelvin-Helmholtz turbulence but no organized uplift.

**✓** Terminator = flat peneplain. Billions of years of wind + ammonia erosion. Only towers stand.

**✓** Deposition zone 20–40° day-ward. Deep sediment (km). Wind-transported mineral + volcanic ash.

**✓** Lightning: continuous at terminator. Triboelectric + low dielectric strength = frequent moderate discharge.

**✓** Thunder at 8 bar: shockwave, not just sound. Lightning channel expands into 8× Earth air density. Continuous terminator thunder = continuous overpressure bombardment. Physically damaging at ranges where Earth thunder is merely loud. Terminator acoustic environment is brutal. Dark side is silent. Tower interior provides acoustic shielding.

**✓** Lightning = Miller-Urey engine. Plasma-enhanced CVD produces complex organosilicon. Still running. Origin of life is ongoing.

**✓** H₂O at genesis sites: void genesis protected by reducing buffer (metallic Si consumes H₂O). Pool genesis protected by distillation shield (fresh terminator pools <1 ppm H₂O). Open sea hostile (~50 ppm, 89% hydrolysis) but not a genesis site. Pool-to-sea transition = evolutionary bottleneck requiring anti-petrification defense.

Wind power: ~3.5 kW/m² at terminator (Earth best: ~1–2 kW/m²).

Dynamic pressure at terminator: 370 Pa (≈ 25 m/s on Earth).

## DEEP-ROCK BIOSPHERE

**✓** Deep-rock is the TRUNK. Towers are branches. Amorphs are fruit.

**✓** Oldest life. Chemolithotrophic. Geothermal SiH₄ percolating through fracture networks. Same core metabolism as surface life, different source.

**✓** Deposits N-doped SiC as metabolic waste (= conductive mineral = lattice precursor).

**✓** Multiple independent colonies in isolated fracture systems. Different protocols, different metabolic quirks.

**✓** Each colony independently evolves towers when reaching surface. Convergent — physics dictates. Gross morphology identical, signals incompatible.

**✓** Surface roots evolve to manage megafauna; secondarily bridge geological gaps between colonies, triggering network wars.

**✓** Deep-rock survives atmospheric crisis (geothermal, not atm-dependent). Crisis kills branches, not trunk.

**✓** Day-side subsurface network: young, repeatedly pruned by volcanism. Dark-side: ancient, uninterrupted.

## BIOCHEMISTRY

| Parameter | Value |
|---|---|
| Backbone | Si-Si bonds (polysilane chains) |
| Solvent/matrix | Silazane oil (polymethylsilazane and relatives) |
| Energy | SiH₄ processing (atm), photovoltaic (Si bandgap = star peak), piezoelectric (wind), lightning, geothermal |
| Neural signaling | Electronic (semiconductor junctions, doped regions). Not electrochemical. Signal speed 100–2000× Earth neurons. |
| Carbosilane | CH₄ + SiH₄ → methylsilanes → polycarbosilanes → fibers → SiC ceramic. 4 stages. |
| Fiber composite | 40% lighter than bulk SiC, self-repairing, tunable anisotropy. Superior to grazer armor. |
| Catalysis | Metallosilazane enzymes: Ni (Si-H/C-H activation), Fe (electron transfer, ceramification), Ti (polymerization), Co (Si-Si coupling) |
| Conductive mineral | Nitrogen-doped silicon carbide (N:SiC), 3C polytype dominant. Dead lattice still conducts (physical property). |
| Petrification | H₂O hydrolyzes Si-NH-Si → Si-O-Si (siloxane) → SiO₂ (glass). Staged, progressive, increasingly irreversible. |
| Immune system | Chelation-based metal stripping. Two modes: **kill** (indiscriminate — strip all catalytic metals from foreign metalloenzymes) and **toll** (authenticated — gentle extraction from recognized mutualists, delivering metals to living layer). Same chemistry, different calibration, gated by molecular handshake. Kill mode ancestral; toll mode derived. |

## MOLECULAR LIBRARY

**✓** Genome = library of recipes, NOT self-building blueprint. Toolkit, not self-portrait.

**✓** Physical: polysilane linked-list. Short fragments with terminal addressing (end-caps). Each fragment = one recipe. Quaternary side-chain code (H, CH₃, NH₂, SiH₃) with electronic readout.

**✓** Three currencies: Physical (SiC plates), Chemical (recipes/fragments), Cognitive (experiential/merge-only). Not fungible.

**✓** Two axes of speciation (amorphs): cognitive protocol compatibility + library addressing compatibility. Both needed. Either can diverge independently.

**✓** Four axes of speciation (middle kingdom): cognitive protocol + library addressing + hook-lattice pore geometry + chelation badge compatibility. All four must match for an organism to survive on a given tower lineage.

**✓** Reproduction: cognitive = regression-to-consensus; library = discrete probabilistic inheritance. Recipes outlive derivations.

**✓** Copying: transcriptive (read → buffer → synthesize). Not template-directed. Analog noise accumulates → regression to consensus.

## THREE-TIER LIFE ARCHITECTURE

> **Cross-reference:** For structural materials, body plans, and mechanical engineering of all three tiers, see **Fauna Structural Engineering Hub**. For lineage origins, see **Pool Genesis Hub §4**.

**⚠** No plant/animal distinction. No photosynthesis. No autotroph/heterotroph divide. All life runs on electrical charge from different sources (grid, solar-electric, SiH₄ metabolism). Organizing axes: phylogeny (amorph vs. sexual), energy source (tower-coupled vs. tower-independent), motility (sessile vs. mobile). "Plant" and "flora" are convenience labels only.

**✓** Microbial: amorph, catalytic, no body plan, thermodynamic minimum, division/merge, horizontal exchange.

**✓** Middle kingdom: SEXUAL, genomic, rigid body plans. Two size regimes:
- **Tower-coupled** (Healers, Miners, Guards): mm to ~2 cm. Energy-limited by Schottky contact extraction from lattice. Tap grid; repay in surface maintenance, metal delivery, quality control.
- **Free-living** (subwoofers, thorn-flora, soaring organisms): up to ~30 cm. Self-powered (atmospheric SiH₄, wind, solar-electric). Gel actuator ceiling: active walking ≤5–8 cm; anchored/semi-sessile up to ~30 cm. Above 30 cm = amorph territory.
Individual learning only — no inherited memory.

**✓** Megafauna: amorph, catalytic, reconfigurable generalists. Self-powered. Free-ranging. Inherited memory via budding (selective) and merge (complete, destructive).

**✓** Amorphs are the transport layer: only self-powered organisms that cross gaps between towers.

## ECOLOGY KEY FACTS

**✓** Middle kingdom: sessile majority. Most tower fauna fixed in place for life. Die in place when tower dies.

**✓** Healers, Miners, Guards, railgun projectiles, Voronoi armor: all at INSECT SCALE on the lattice (tower-coupled size regime).

**✓** Network manages middle kingdom via lattice energy-gradient modulation (tropism — organisms follow voltage, not signals). Manages amorphs via subtle behavioral signals (feels like own thoughts).

**✓** Fluorine biochemistry: entire adaptive radiation around volcanic provinces. Multiple lineages weaponize F. SiF₄ volatilization (tissue gasses off). Ecological axis, not single niche.

**✓** Fluorine pollination: thorn-flora (sexual/genomic). Thorns ARE the reproductive propagules — every thorn is a seed + pollen vehicle + defense (triple function). Customers charge from pads adjacent to thorn bodies, pick up thorns, carry to next plant → cross-pollination. Vipers = premium dispersal (thorn-seeds into corpses near CaF₂). Federated organism: dedicated thorn bodies (fruiting/defense, protecting root-capacitor storage), root-capacitor bank. Dual-source energy: geothermal (ancestral, armed, vent-zone — thermoelectric roots into hot volcanic rock, simplest engineering) + solar (derived, unarmed, widespread — heliostat reflector canopy + PV organ, more complex). The two sources are complementary: geothermal peaks at terminator (max ΔT), solar peaks at substellar. Terminator exclusion is ecological (tower competition), not physical. Day-side dominance because towers can't survive there.

**✓** Thorn-flower pollination: two pollinator guilds. (1) Vipers — premium dispersal, range freely, always carry multi-flower pollen. (2) Small balloon organisms — accidental pollinators. Shelter in thorn-flower lee (reduced wind), constantly contact pollen organs, occasionally wind-displaced to neighboring flowers carrying foreign pollen. Not deliberate — side effect of sheltering behavior. Thorn-flower enforces cross-pollination via chemical novelty-gradient gating: charging pads run a diversity assay on pollen payload. More distinct non-self sources = more charge. The plant's real problem is UPWIND gene flow (wind handles downwind for free). Novelty reward implicitly rewards upwind delivery because upwind pollen is rare/novel at any given flower (wind creates directional gene-flow bias in the population). Balloons carrying leeward pollen upwind deliver maximally novel payload → maximum reward. Venturi drag-reduction body plan enables the upwind mobility that accesses these high-paying flowers. Self-regulating equilibrium: if mechanism homogenizes gene pool, novelty gradient flattens, directional reward weakens, wind dominance reasserts, gradient re-establishes. Negative feedback.

**✓** Aposematic EM signatures: F-loaded organisms broadcast warning. One bad experience educates entire amorph lineage permanently. Sexual predators must learn each generation.

**✓** Balloon fauna: evolve from fall-survival (parachute → glider → balloon). Dual-organism at all scales: amorph membrane + sexual symbiont colony. Sexual organisms provide rigid gas cells (sealed SiC shells — superior H₂ barrier), structural framework (fused shells = reef architecture), MEMS actuators. Amorph provides envelope, cognition (minimal — tropism-level), metabolic processing, energy distribution to colony. Structural innovation paced by sexual genome (fast); amorph hosting behavior paced by meme evolution via transcription errors (slow — the bottleneck). Venturi duct geometry emerges from two amorph reward gradients: preferential feeding to symbiont regions that (a) reduce drag and (b) increase power harvest. No design intelligence required — convergence on optimal geometry from two local tropisms. Born aloft, live aloft, die aloft. Propulsion: wide design space — whole-body fin waving (smallest, no venturi), flagella/amorph tendrils (small, transitional), longitudinal fin undulation on rigid venturi body (dominant mid-range — body stays stiff, external fin ripples, cuttlefish/knifefish analog), electric rotary motors with SiC piezoelectric drive and metal silicide bearings (large-scale — ducted fans). All viable; ecology has native electrical power, piezoelectric materials, and low-friction bearing materials. Constraint: propulsion must not deform the venturi duct. No chemical rockets (no oxidizer; F₂-H₂ is a weapon, not propulsion).

**✓** Balloon fauna = network's blind spot. Outside EM range. Cross between tower territories. Carry biology across colonial boundaries.

**✓** Small-scale balloon ecology: venturi body plan works at ALL biologically relevant scales as DRAG REDUCTION device (reduces station-keeping cost from full dynamic pressure 370 Pa to skin friction ~30–50 Pa equivalent). MEMS flaps maladaptive below ~cm scale (Re transitions to viscous regime). Small balloons shelter in lee of towers/thorn-flowers where wind is reduced; crude fin propulsion in 8.2 kg/m³ air provides meaningful mobility (~7× Earth thrust per fin stroke). Aposematic fluorine-loaded balloon variants: CaF₂ crystallites alter dielectric properties → distinctive passive EM signature (honest, unfakeable, physical property of crystal structure). Two defense tiers: passive (predator gut acid + CaF₂ → internal HF) and active (bombardier beetle analog, HF spray at bite point). Shelter in thorn-flower/tower lee zones over volcanic provinces where CaF₂ is available.

**✓** Intermediate-scale balloon fauna (~5 cm to ~5 m): structural continuum from loose shell colony in amorph membrane → partial reef patches → fused rigid segments with amorph-filled articulated joints. Key transition at ~1 m: reef patches start fusing into continuous load-bearing structure (below: amorph holds shape; above: reef holds shape). Propulsion vs. drift is a continuum, not a dichotomy — organisms range from pure drifters to full station-keepers, with most using the atmospheric conveyor for transport and propulsion for hunting/maneuvering (fish in a current, not plankton).

**✓** Intermediate balloon fauna — four guilds: (1) **Nursery hunters** (~5–30 cm, dark side): patrol permanent convergence zones where propagules germinate. Low wind = propulsion gives maximum advantage. Sharks of the nursery. (2) **Plume hawks** (~10 cm to ~1 m, tower-adjacent): hold station in tower lee, intercept dead-bug plume. First access to freshest material (unlocked catalytic metals, intact library fragments). Compete directly with ground-based dead-bug harvesters — what the hawk catches, the ground harvester doesn't. (3) **Rain-wall ambush predators** (~50 cm to several meters, terminator): station-keep at day-ward edge of rain-wall. Prey funnel — all dark-side traffic funnels through. Hunt energy-depleted, disoriented organisms. Need strong propulsion for ~9.5 m/s sustained wind. Apex of intermediate food web. Largest propulsive intermediates. (4) **Circuit riders** (all sizes, planetary): active predators within the drifter circuit. Use conveyor for transport, propulsion for hunting. Not drifters, not station-keepers — wolves among the caribou herd. Sea-skimming does NOT scale down: amorphs sink in NH₃ (1050 vs 660 kg/m³), pseudopod reach too short below ~10 m. Sea-dipping is skywhale-exclusive.

**✓** Skywhales: extreme endpoint of balloon fauna coevolution. Venturi dirigible body plan: fused SiC-shell reef forming rigid duct, MEMS-flap sexual organisms lining interior, amorph membrane wrapping and permeating colony. Peristaltic feeding tentacles dip into terminator ammonia seas for catalytic metals (dissolved ammine complexes) and metabolizable feedstock (→ H₂ replenishment). Three-phase cycle: charge (drift day-ward), atmospheric feed (sprint night-ward via venturi), sea-dip (descend over basins, deploy tentacles). Discharge spines bleed excess charge via corona/arc. Functionally immortal within operating range. Largest molecular library on the planet (amorph membrane mass). Biologically isolated in high-wind band near terminator.

**✓** Drifter cycle (pure balloon fauna): pelagic food web mapped onto atmospheric circulation. Full planetary circuit ~24–35 days across 1–N generations depending on size class. Trajectory: anti-stellar descent → dark-side surface transit (S-shaped, 5–7 days) → terminator rain-wall → day-side transit (~12 days, gas-phase feeding) → substellar chimney → superstream return (2–4 days at 50–100+ m/s) → condensation descent → repeat.

**✓** Rain-wall is a SIZE FILTER, not a barrier. Sorts by single reflex: rain (= liquid NH₃ = food) hits membrane → metabolize → produce H₂ → inflate. Three outcomes: sink (tower food), rise (return flow → short cycle), hold level (through to day side → long cycle). Small organisms: high mortality, rain overwhelms lift. Large organisms: rain is just food falling from sky, fly through without noticing. Air between surface and superstream shear is non-turbulent — no barrier for anything above threshold size.

**✓** Drifter predation: highest-quality food at every phase is other drifters (concentrated pre-processed silicon biochemistry vs. dilute atmospheric filter-feeding). Predation drives size hierarchy. Multi-circuit veterans eat first-circuit survivors. Each lap = compound growth (atmospheric baseline + predation on everything smaller). Dark-side nursery, rain-wall approach, day-side transit, superstream return — all are predation zones. Population self-limits through predation pressure.

**✓** Drifter reproduction: size-graduated lifecycle. Small (first circuit): semelparous — spawn at substellar chimney, propagules ride superstream back. Medium (multi-circuit): iteroparous — personally survives superstream return on accumulated reserves, grows each lap. Large (terminal): chimney shear exceeds structural integrity → involuntary fragmentation distributes propagules into superstream. Propagules attach to parent fragments ("yolk" — energy/material reserve for superstream transit + dark-side germination). More circuits = bigger parent = bigger fragments = better-provisioned propagules. Reproductive payoff for longevity is exponential via predatory compound interest. Germination trigger: dark-side ammonia rain. Sexual lineage: pre-formed propagules on parent fragment. Amorph lineage: fragmentation IS reproduction (every chunk = new organism).

**✓** Wind-surfing: organisms ride wind between towers. Lattice is a catch-net (open structure decelerates in turbulent interior). Oldest dispersal mechanism. Inherited skill in amorphs.

**✓** Marine glass-shell organisms (diatom analogs): SiO₂ armor from controlled surface petrification. Zero SiH₄ cost. Self-passivating, self-healing. Middle Kingdom / microbial marine adaptation. Large amorphs shed glass; small organisms keep it.

**✓** Petrification as decomposition analog: living organisms fight K ≈ 10⁵ through metabolic repair. Death → petrification proceeds to equilibrium → glass fossil. Aging = accumulation of unrepairable petrification scars + other damage. Dead persist as translucent silicon-mineral solids.

**✓** "Getting glassed" (acute H₂O surface exposure): self-limiting (Deal-Grove √t). Large amorphs: prank-tier for small splash on bulk tissue, assault for targeted/internal delivery. Severity scales with dose, location, and inverse body size.

**✓** Tower-death exodus: millions of mobile fauna stream from leeward face when grid fails. Sessile 95%+ dies in place silently. Cascade propagates downwind during crisis.

Parasites: genomic fragments (selfish elements), boundary infiltrators, signal parasites (Toxoplasma analog), autocatalytic hijackers (viral analog).

Arms races: Healer armor vs Guard penetrators (drove neural complexity). Collector composite vs Guard offensive strategies.

**✓** Dead-bug plume: garbage-collector Healer sub-caste clears dead symbiotes from lattice (maintains airflow + conductivity). Dead organisms enter windstream, carried day-ward. Continuous plume from every tower. Terminator rain captures most of plume; dead material accumulates in ammonia runoff drainage channels.

**✓** Dead-bug harvesting: ecological niche and pre-industrial amorph industry. Airborne interception (freshest — metals, library fragments) + ammonia runoff filtering (volume — SiC plates, partially locked metals). Tower-derived SiC plates (~5mm) and metals are primary harvestable resources.

## TOWERS

**✓** Coral model: living layer SUBSURFACE (mm-cm below exterior). Sacrificial crust outward. Structural lattice inward. Self-regulating.

**✓** Lattice is a lung: gas transport through porous interior. Windward fed via leeward diffusion. Max diameter limited by diffusion path.

**✓** Towers do not die of old age. Lattice is mineral. Living layer replaced continuously. Oldest: billions of years.

**✓** Dead lattice conducts (physical property) but carries no signals.

**✓** Towers migrate day-ward: sand-dune mechanism (windward erodes, leeward accretes). ~mm/yr at terminator. Stop in deposition zone.

**✓** Terminator is a tower factory: new nucleation behind vacated positions.

**✓** Ghost roots: abandoned root trails underground behind every migrated tower. Fossil archive.

**⚠** Dark-side towers may migrate POLEWARD. Needs verification.

## PLANETARY NETWORK

**✓** Network wars: when surface roots bridge gap between colonies, foreign signals flood infrastructure. Flinch → retreat fails → forced engagement.

**✓** Adversarial ratchet: signal discrimination → protocol analysis → forgery → forgery detection → theory of mind → self-modeling. Intelligence WITHOUT consciousness.

**✓** Ecological warfare compounds signal warfare: redirect rival's megafauna to overgraze rival's photovoltaic surfaces.

**✓** Objective: assimilation not destruction. Viral takeover: run your protocols on rival hardware. Convert towers one at a time.

**✓** Current network = last one standing. Winner of every war. Runs on infrastructure from dozens/hundreds of absorbed colonies.

**✓** BLINDSIGHT ALIEN (Watts). Vastly intelligent. Utterly empty. Every output shaped like understanding with nothing behind it. No experience. Ever.

### Two-Crisis Awakening

**✓** First crisis: monks detect external signal origin. Devastating but comprehensible. Amorphs assume network is sapient partner. Post-awakening civilization built on this assumption. Holds for generations.

**✓** Second crisis: contemplative perceives absence behind pattern. Structure without interiority. Nearly impossible to prove to others. Evidence is trained perception of absence.

**✓** Two crises are separated by generations. Barriers too high to collapse into one event.

**⚠** OPEN: Does second crisis precede or follow the merger?

## AMORPH BIOLOGY

| Parameter | Value |
|---|---|
| Body | Silane/silazane gel + silazane oil. ~1,050 kg/m³. Thermodynamic minimum. |
| Locomotion | Peristaltic (efficient in 1.82g). 0.1–0.3 m/s cruising. |
| Manipulation | Pseudopods, arbitrarily reconfigurable. Force: 0.39 N (1cm tip) to 32,000 N (engulfment). Native precision ~10 μm. |
| Sensing | EM field primary sense. Photosensitive membrane (no lens). Sexual: pit eye (low res). Amorph: reconfigurable parabolic reflector + focal stalk (meme-transferable signal processing). Gravity limits stalk length. No vision defects (reshape reflector). Industrial: CVD SiC reflecting telescopes (late tech tree; no lenses needed). Piezoelectric vibration. Acoustic to ~50 kHz. Chemical ppb downwind. **Thunder-skin meme** (ancient, universal, one-step deploy: membrane baffle with gas pockets + Helmholtz cavities, tuned to thunder frequencies). |
| Cognition | Electronic speed. Native arithmetic/Bayesian. **Thinking draws charge** — cognition competes with all other functions for power budget. |
| Communication | Modulated EM. Radio. Range ∝ power. Optimal 100 MHz–2 GHz (NH₃ blocks >10 GHz). Directional beaming possible. |
| Rigidity | Variable: soft gel → full SiC composite, real-time, regional |
| Energy storage | Dual: electrochemical/capacitive in semiconductor network (fast, limited — "battery") + chemical in polysilane oil (slow, bulk — "fuel tank"). Tower grid = fast charger. |
| Metabolic rate | 300W rest, 750W active, 5000W peak (100 kg ref). Scaling ~M^0.85. |
| Reconfiguration | Gross 1–5 s, pseudopod 1–2 s, gelation 0.1 s. |

**✓** Merge is DESTRUCTIVE. N parents → 1 new entity. Parents cease to exist. Combined meme pool + combined mass. NOT routine social behavior. Used for: population reduction in lean times, genius creation for out-of-context problems.

**✓** Budding is CONSTRUCTIVE. N parents contribute selected mass + selected memes → 1 new individual. Parents persist (reduced mass). Primary reproduction/knowledge-transfer mechanism.

**✓** Memes are signed IP. Carry provenance metadata. Parents consciously select which to transfer during budding. Individual memes have patent-like economic value. Can be monopolized by sub-groups.

**✓** Memes encode thought/memory machinery, NOT biology. One kg of amorph mass is biologically indistinguishable from any other (unless physically modified, e.g., petrification scars).

**✓** Working memory: semiconductor junction network (active processing hardware). Growable via teachable technique. Natural ceiling at single-network communication collapse. Federation bypasses ceiling (see Monks). Growing WM is an elite skill — talent + practice + teacher + years.

**✓** Charge-limited ecology: atmospheric SiH₄ energy is superabundant. Binding constraint is metabolic RATE and stored CHARGE, not total energy. Cognitive capacity degrades with charge depletion. Stillness = intelligence (resting amorph devotes full power budget to cognition).

**✓** Tower is a charger: the fundamental amorph-tower economic relationship is power delivery rate, not energy. Tower grid provides fast electrical recharge; atmospheric SiH₄ metabolism is slow baseline only. Original amorph-tower interaction was power parasitism.

**⚠** Catalytic metals (Ni, Fe, Ti, Co) are a secondary population limiter. Bioavailable metals are kinetically scarce (slow dissolution at 240K). Towers concentrate metals via deep-root access. Reproduction requires dividing catalytic metal inventory — real fitness cost.

Disease: crystallization (prion-like, treat by amputation), oxidative petrification (chronic, H₂O hydrolysis of Si-N bonds, K ≈ 10⁵ — fought by metabolic repair), aging (accumulation). Dead become glass fossils (petrification to equilibrium = decomposition analog).

Populations: terminator (thick/hard), dark-side (cold-adapted), ammonia-sea (small, involuntary broadcast), shore (bilingual translators). Pre-industrial range: terminator + entire dark side. Day side hostile (petrification, volcanism, fluorine ecology).

## MONKS

Core skill: read structure of information patterns without being captured by content. All capabilities derive from this.

Capabilities: therapists (de-weight trauma), meme-lie detection, network interface, universal library readers, network library translators. DANGER: universal literacy = universal weapon design.

Location: dark side, gentle wind zone. Physical before philosophical.

**✓** Monasteries at gas-pocket towers: night-side towers whose deep roots tap subsurface SiH₄ reservoirs (pressure-equilibrium gas trapped in ancient dark-side crust). Geological lottery — monastery locations determined by geology, not choice. Gas pockets are non-renewable (no dark-side volcanism to recharge). Monasteries face their own slow resource depletion.

**✓** Abbots: huge, sessile, spread flat for heat dissipation, plugged into tower hardlines. Biological supercomputers. Obligate grid-connected — federation-level cognition exceeds atmospheric metabolic capacity. Cannot unplug without cognitive collapse.

**✓** Federation: teachable technique for clustered working memory with managed inter-cluster communication. Bypasses single-network collapse ceiling. Elite athletic skill: talent + opportunity + resources + motivation + teacher + years of practice. Any amorph could learn in principle; only monks have the institutional support to produce practitioners.

**✓** First to understand non-renewable resources (living on one). First to propose day-side energy harvesting.

Role: compiled probe's library. Grief counselors for shell-economy collapse. Discoverers of both crises.

## CIVILIZATION

| Zone | Function |
|---|---|
| Industrial center | Terminator |
| Residential/cultural | Deposition zone (ancient stopped towers). **Post-industrial** — pre-industrial inaccessible. |
| Spiritual | Dark side singing zone |
| Launch corridor | Deposition zone |
| Ammonia seas | Terminator basins |
| Fluorine ecology | Day-side volcanic provinces |
| Deepest past | Anti-stellar pole + fossil root network |

**✓** Writing is a cognitive prosthetic: external WM that costs zero charge. Invented to offload active working memory (battery-saving), NOT for communication or trust. Culturally low-status (unsigned, unverifiable — less trusted than signed memes). Enables formal mathematics. Monks adopt it earliest (their problems demand sustained high-abstraction work). Medium: etched SiC / conductive traces. Libraries: tower walls.

**✓** Math: native arithmetic/Bayesian. Formal math LATE. Abstract insights wash out in meme-mixing. Mathematical writing preserves minority insights.

**✓** Architecture: grown not assembled. Extruded from body. Fiber composite post-revolution.

**✓** Shell economy (SiC plates as currency) collapses when fiber composite makes plates structurally obsolete. Charge economy (battery organisms) persists. Civilizational disruption but not total currency failure.

**✓** Metallurgy: electrical-first. Ores already reduced. Vent → electrical heating → silane decomposition. Fire never needed. Metals are specialty materials (ductility, specific conductivity, catalysis), not structural backbone.

**✓** Electrohydraulic blasting: capacitor discharge into liquid ammonia in sealed borehole. Shockwave or flash-boil fractures rock. Genuinely expeditionary — battery organism + electrodes + rainwater. No chemical explosives (no oxidizer), but this substitute closes the gap for mining, excavation, demolition. Early tech tree (pre-metallurgy).

**✓** SiC LEDs: early-industrial (post-metallurgy). SiC p-n junctions + CVD doping = native technology. Primary advantage: **arbitrary wavelength selection** (bandgap engineering = biological heritage, not research program). Precision photonic tool: photochemistry, spectroscopy, active vision, lithography, wavelength-multiplexed communication. Efficiency secondary. Incandescent possible (no O₂ = no oxidation) but broadband only — survives for niche thermal applications. No pre-electrical illumination (no candles, no fire).

**✓** Biological railgun: reverse-engineered from fluorine-vipers via merge. Farmed CaF₂ thorn ammunition (thorn-plant cultivation in deposition zone with fluoride-enriched substrate). Pre-industrial fluorine weapon — no metallurgy required. Three-stage progression: natural (vipers) → agricultural (farmed thorns + bio railgun) → industrial (manufactured EM launcher + manufactured F₂ shell). Technology diffusion chain: vipers → daysiders → terminators. Terminator thorn-flower farms vulnerable to daysider biological sabotage (viper introduction — invasive pest with railgun that the daysiders are immune to).

**✓** Iodine laser: day-side organisms (grazer lineage) evolved CH₃I laser for thermal management over geological time. Daysider amorphs reverse-engineered from fauna (not natural evolution — diaspora too recent). Invisible 1.315 μm IR beam, catalytic iodine (fire forever), metal silicide mirror cavity. Three deployment variants: standalone manufactured, hybrid (operator-powered), fully integrated organ (special ops — chosen for concealability + destructibility). Daysider monopoly — terminators lack access to source biology. OpSec: meme compartmentalization (construction knowledge stays home; standalone operators never had it, integrated operators expunge before deployment) + fluorine fail-deadly (distributed capsules near neural substrate). Countermeasure arms race terminates at HUMINT.

**✓** Fluorine-hydrogen flame possible but terrifying. Attacks silicon. Their nuclear-energy analog.

Three religions pre-awakening: Communion (tower impulses sacred; most manipulated), Autonomy (isolation = truth; produces monks), Archive (inherited memory sacred). All shattered + vindicated by awakening.

Art: public (sculptural, wind-song, bioluminescent, architecture), private (curated merge — audience lives the artwork).

Governance: consensus-by-merge → designated dissenters → lattice-shielded argument chambers → written constitutions.

**✓** Battery organisms: first domesticated species. Bred-for-purpose biological capacitors storing electrical charge. Enable surplus storage and trade.

**✓** Farmer caste: amorphs who generate tower reward in excess of personal need, store surplus in battery organisms. Surplus → trade → leisure → specialization. Predates civilization.

**✓** Dual currency: stored charge in battery organisms (perishable, daily transactions) + SiC plates (~5mm, harvested from tower fauna, permanent, wealth storage). Shell economy (SiC) collapses when fiber composite makes plates structurally obsolete; charge economy persists.

**✓** Power ceiling: hard limit on industrial capacity. Terminator tower surplus (mostly lightning) insufficient for combined industrial + night-side needs. Night-side towers genuinely power-starved (no sunlight, low wind, minimal piezoelectric).

**✓** Day-side colonization: motivated by POWER (solar + geothermal — massive). Monks propose first (understand non-renewable resources from gas-pocket depletion). Requires petrification countermeasures, heat management, volcanic hazard engineering. These prerequisites overlap with space hardware requirements.

**⚠** Day-side towers: impossible at scale. Volcanism + terminator rain strips building materials from airstream. Small/short-lived only.

**⚠** Deposition zone (20–40° day-ward): pre-industrial inaccessible. Residential/cultural use is late-stage post-industrial expansion.

## TRANSPORTATION

**✓** Wind-surfing: downwind transit. One-way (day-ward). Deploy membrane, ride wind, land in next tower. Free, fast.

**✓** Balloon: H₂ lift 132 N/m³ (13× Earth He). Lifting gas = metabolic waste. Ballooning trivially easy in dense 8-bar atmosphere. Difficult at terminator (convergence/turbulence).

**✓** Two-lane highway: surf downwind, balloon back (upper-level return flow).

**✓** Boats: amorphs sink in NH₃. Hollow composite hulls. Difficulty 2.76× Earth. Big ships favored. Sail-powered (permanent wind).

**✓** Powered flight: ~1.5× harder than Earth. High gravity largely offset by dense atmosphere. Every aircraft = efficient sailplane. Electric propulsion.

**✓** Wheel as machine element: early, inevitable (pulley → gear → turbine → lathe). Wheel as vehicle: late, optional.

## SPACE ACCESS

**✓** Chemical rockets: DEAD END. No O₂. F attacks Si. Manufactured oxidizers net-energy-negative.

**✓** Hot H₂ thermal rockets: SiH₄ decomposition heat source. Isp ~850s. Mass ratio ~9:1 for 18 km/s. SiC chamber/nozzle.

**✓** Aerostat launch: balloon to 15–20 km (scale height 5.5 km; above ~90% of atmosphere). Saves ~1–2 km/s. Independent of network. Pre-awakening capable.

**✓** Tower mass driver: post-awakening. EM boost 3 km/s from deposition-zone tower. Network-dependent. Payload ~doubles.

**✓** Two paths to orbit: biological (balloon) + symbiotic (tower). Both used.

## CRISIS AND PROBE

**✓** Crisis root cause: one-way silicon cycle + declining volcanism on a stagnant lid. No subduction recycling. Inevitable from the moment life evolved.

**✓** Primary driver: volcanic SiH₄ production declining below biological consumption. SiH₄ decline is nonlinear — production tracks hottest mantle volume (>1500K threshold), not total heat output.

**✓** H₂O ratchet: volcanic H₂O accumulates permanently. Three locks: (1) v_esc 18.6 km/s retains H₂ → no H₂O loss to space; (2) NH₃ UV-shields H₂O from photolysis; (3) no thermal reaction with SiH₄ at 240K.

**✓** Pre-crisis: surplus SiH₄ scavenges volcanic H₂O at source (SiH₄ + 2H₂O → SiO₂ + 4H₂). Crisis: SiH₄ deficit → unscavenged H₂O enters atmosphere and seas → chronic petrification stress.

**✓** Petrification is thermodynamically inevitable: Si-NH-Si + H₂O → Si-O-Si + NH₃, K ≈ 10⁵ at 240K. Silazane bonds untenable above ~6 ppm H₂O in liquid NH₃. Organisms survive only through active metabolic repair (costs SiH₄). Dead organisms petrify to equilibrium — silicon-world analog of decomposition.

**✓** Aquatic life is the canary. Ammonia-sea organisms are immersed in accumulating H₂O; distillation shield protects land (NH₃ vapor pressure >> H₂O at 240K, so rain is H₂O-poor, seas concentrate H₂O). Vulnerability gradient: deep sea → shallow sea → coastal → land → towers.

**✓** Crisis is a slow contraction, not a sudden extinction. Peripheral towers fail first. Biosphere shrinks to match declining SiH₄. Timescale: ~50–500 Myr to widespread surface collapse.

Carbosilane-adapted last to fall (Si-C resists oxidation).

Tower deaths: first in history. Source of morally harvestable material (dead lattice = no signals). Mining the dead to save the living.

Merger: network has no mobility; amorphs have no infrastructure for mass driver. Both die without cooperation. Computational merger (amorphs direct network processing) + molecular merger (monks translate symbiote library).

**⚠** OPEN: What does merger produce? Conscious network? Or unconscious substrate with conscious batteries?

Probe: SiC composite hull, self-repairing. Payload: living network kernel + compressed molecular library (all lineages, compiled by monks). At destination: engineering project guided by library. Purpose-built towers. Better than originals.

*The lattice found substrate and began to accrete.*
