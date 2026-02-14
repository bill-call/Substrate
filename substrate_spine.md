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
| Ammonia seas | Terminator basins (rain-fed, marginally stable) and night-side basins (stable, growing). Condensation line = terminator. Persist only where towers stabilize them (H₂O ratchet). | ~660 kg/m³. Amorphs sink. |
| Hydrocarbon lakes | Deep dark side. Ethane/propane. | ~450–550 kg/m³ |

## GEOLOGY

**✓** Stagnant lid. No plate tectonics, no subduction. Heat escapes via mantle plumes.

**✓** Hemispheric asymmetry: day-side lid thinner/warmer, plumes breach preferentially. Dark-side lid thick/cold/stable.

| Zone | Description |
|---|---|
| Day side | Volcanically active. 10–30 provinces simultaneously. ~100 Myr resurfacing. Continuous, not episodic. Source of SiH₄ + H₂O outgassing. |
| Dark side | Geologically quiescent. Ancient stable crust. Minimal volcanism. |
| Terminator | Lithospheric flexure zone. Chronic cracking/faulting. Primary fracture networks. |
| Fracture networks | Discontinuous. Each isolated system hosts independent deep-rock system. |
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

## SURFACE GEOMORPHOLOGY

**✓** Atmospheric particulate conveyor: closed loop. Day-side volcanism → surface winds carry particulate to substellar chimney → chimney lofts fines into superstream → superstream carries to anti-stellar downdraft (velocity increases toward anti-stellar via spherical convergence — anything carried past the terminator goes the full distance) → deposition → katabatic surface winds re-entrain and carry back toward terminator/day side. Chimney acts as grain-size filter: only material light enough to be lofted enters the loop. Katabatic wind can re-entrain everything the chimney admitted. No net accumulation on the dark side (exception: anti-stellar stagnation cap — katabatic wind starts at ~0 m/s, local accumulation of finest fraction possible; minor, self-limiting, not geologically significant).

**✓** Dark-side peneplain: SiC-polished bedrock. Pre-biotic volcanic SiC (~9 Tg/yr, ~0.08% of conveyor particulate) smooths silicate terrain at ~600 mm/Myr before biology exists — smooth but not polished. Dead-bug plume later adds massive biological SiC, producing the mirror-polish (geological marker of biosphere onset). Dead-bug plume feeds SiC particulate (Mohs 9.5) into the atmospheric conveyor. SiC abrading silicate bedrock (Mohs 6-7) over billions of years produces mirror-smooth surface. No constructive geology (no volcanism, no tectonics) to rebuild. Two distinct laminar/turbulent regimes: (1) free-stream flow IS laminar (stably stratified atmosphere, no convection, no weather systems, no turbulence sources); (2) surface boundary layer is aerodynamically smooth turbulent (Re ~10¹², but surface roughness < viscous sublayer ~50 μm — no roughness-driven eddies). Both regimes → same consequence: only towers generate significant turbulence at any scale. Deep dark side is polished bedrock plain to the horizon.

**✓** Day-side geomorphology: active volcanic terrain. Continuous plume volcanism builds shield volcanoes and flood basalt provinces. Wind erosion sculpts but cannot overcome construction rate near substellar. Gradient from volcanic construction-dominated (substellar) to erosion-dominated (toward terminator). Yardangs, ventifacts, streamlined ridges oriented radially toward substellar.

**✓** Ammonia seas are tower-dependent features (modern). Towers are the only self-repairing roughness element on the planet. Tower breaks aerodynamically smooth boundary layer → turbulence → scour basins and depositional features → topographic complexity that holds liquid ammonia. Kill the tower, turbulence stops, basin fills with aeolian sediment, peneplain reclaims it. Without towers, ammonia seas cannot persist — any depression is a sediment trap (everything sinks in ammonia, atmospheric fallout fills it).

**✓** Shore deposition zones: where katabatic wind meets ammonia surface, waves create roughness, boundary layer trips to turbulent, wind carrying capacity drops, particulate falls out. Shorelines are the ONE place on the dark side where material accumulates. SiC grit, volcanic fines, dead-bug plume debris (catalytic metals, library fragments, SiC plates). Shore = nutrient delivery system connecting atmospheric and marine cycles. Primary reason shore/intertidal is the richest marine zone.

**✓** Genesis environment: proto-tower-base ammonia pools at the terminator. Proto-tower = deep-rock system's surface SiC outcrop (Mohs 9.5, differential erosion ratio ~100,000:1 vs silicate terrain). Survives pre-biotic erosion: volcanic SiC is only ~0.08% of conveyor particulate; silicate abrasive (Mohs 6-7) cannot scratch SiC. Pre-biotic silicate terrain erodes at ~600 mm/Myr; monadnock erosion ~0.006 mm/Myr.

**✓** Proto-tower seven force multipliers (for tower-adjacent pools): (1) geothermal SiH₄ venting through fractures (bypasses atmospheric dissolution bottleneck), (2) metal-enriched fracture fluids (all four biometals — Ni, Fe, Co, Ti — via hydrothermal circulation), (3) lightning rod effect (tallest object concentrates Miller-Urey products into adjacent pools), (4) warm fluids (+5–20K geothermal), (5) N-doped SiC semiconductor substrate (catalytic surfaces, electrochemical gradients), (6) flow-through hydrology (drainage maintains <1 ppm H₂O, delivers fresh inputs, creates chemical gradients), (7) micro-pool multiplication (rough lattice topography → many parallel experiments per monadnock). **⚠ NOTE:** Fracture-connected pools fill too fast for genesis (geyser-cone construction fills pools in years to decades; genesis requires My-scale). Force multipliers enhance tower construction and indirectly benefit neighboring non-connected pools via ejecta seeding.

**✓** Pool genesis is INDEPENDENT of void genesis. Both operate on the same planet, driven by mostly independent variables. Pool genesis requires: stable terminator ammonia pools + atmospheric SiH₄ + lightning + some metal source. Monadnock/tower proximity helps (lightning rod, nutrient rain, metal delivery) but is not required. If pool genesis is possible at all, it does not require tight coupling to the deep-rock fracture system.

**✓** Tower as evolutionary engine: void genesis (→ towers) inadvertently drives pool genesis forward. (1) Geyser ejecta provides chronic fine catalytic dust to all terminator pools = **nutrient rain** (metal micronutrient capsules — small fragments passivate fast, release metals as ammine complexes). (2) Rare critical-mass fragments reach distant pools with enough catalytic activity to locally disrupt pool chemistry = **punctuated disturbance** (competes for SiH₄, deposits PCS, forces displacement). Size-dependent migration is the filter: smallest fragments travel farthest, passivate fastest, pose least threat. Large dangerous fragments stay near cone. The disturbance tempo is tunable (geyser energy, fracture density, pool spacing — all geological variables that vary along the 62,000 km terminator).

**✓** Chelation origin: evolves as metal-MINING from catalytic PCS fragments, not as immune defense. Silazane chemistry naturally coordinates transition metals (N lone-pair donation). Coacervates contacting fragment surfaces → non-specific metal uptake → selection for better extraction → proto-chelation enzymes → organisms that passivate fragments on contact (neutralize threat + harvest metals). Later exaptation: chelation aimed at other organisms' metalloenzymes → immune kill mode → calibrated toll mode → symbiote authentication. Chelation is the foundational biological metal economy.

**✓** Preadaptation gradient: organisms in tower-active terminator zones accumulate tower-contact experience across generations. Repeated displacement by catalytic fragments + proximity to tower chemistry → SiC-surface familiarity, metal-profile compatibility, signal exposure tolerance. Selection history, not birthright. Tower doesn't manufacture symbiotes — tower byproducts create the selection regime that produces organisms pre-adapted for eventual symbiosis.

**✓** Void genesis (→ towers) is the expected outcome of any suitable planet's chemistry. Pool genesis (→ mobile life) is a rare conjunction requiring stable terminator ammonia + atmospheric SiH₄ + lightning + metal sources + sufficient time. Tower activity provides the punctuated disturbance regime that drives evolution via catalytic ejecta. Most tower-bearing planets never produce mobile life. Pool genesis only needs to succeed once — wind dispersal populates all towers. The two genesis pathways are synergistic: towers build structure, pool genesis builds life, tower byproducts are the evolutionary engine of pool life.

**✓** One-way door: pre-biotic volcanic SiC already erodes silicate terrain at ~600 mm/Myr. After pool genesis → symbiotes → dead-bug plume, biological SiC dramatically accelerates peneplain formation. Genesis conditions erased. Abiogenesis unrepeatable.

**✓** Proto-tower construction — geyser-built volcanic cone: when deep-rock reaction front reaches pool floor via fracture, vent opens. Throat zone narrows (PCS deposition in gas phase), seals (PCS membrane forms), back-pressure builds, membrane fractures — geyser burst ejects PCS debris + gas + ammonia into pool. Ejecta deposits in rings around vent (circular debris field). Inner ring cements fastest (highest SiH₄ flux). Cone grows upward through pool as rings stack. Vent channel stays clear (scoured by each burst). Cone breaches pool surface → lightning rod → first strike ceramifies tip → conductive N:SiC → proto-tower established. Miniature volcanic cone morphology.

**✓** Geyser ejecta dynamics: catalytically active PCS fragments (embedded Ni, Fe, Ti, Co nanoparticles) ejected in rings around vent. Size-dependent behavior: large fragments (mm+) stay near cone, cement rapidly (high SiH₄ flux), become part of proto-tower base. Small fragments (10–100 μm) travel far, have few metal centers, passivate fast in ammonia (surface aminolysis + metal leaching as ammine complexes, days to weeks). Critical-mass fragments (intermediate, stochastic) occasionally reach distant pools with enough catalytic activity to disrupt local chemistry before passivating. Fracture-connected pools fill in years to decades (geyser + catalytic exterior growth + ejecta welding). **Genesis does NOT occur in fracture-connected pools** — they fill too fast (My-scale needed).

**⚠** Cone-wall dimorphism (DOWNGRADED — secondary effect at most): if protolife predates the tower arrival at a given pool (independent genesis model), the volcanic cone is a bulldozer that displaces existing protolife, not a nursery that creates it. Cone may still impose spatial selection on ALREADY-FORKED lineages during displacement, but is not the cause of the fork. The lineage fork (coacervation → amorphs, amphiphile assembly → sexuals) operates in open pools independent of cone geometry (Pool Genesis Hub §4).

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

**✓** Multiple independent systems in isolated fracture networks. Different protocols, different metabolic quirks.

**✓** Each system independently evolves towers when reaching surface. Convergent — physics dictates. Gross morphology identical, signals incompatible.

**✓** Surface roots evolve to manage megafauna; secondarily bridge geological gaps between systems, triggering network wars.

**✓** Network expansion: root network spreads from mature towers. Network ping rules determine when a new tower buds FROM the root. Bud creates a voltage/signal gradient. Tower-coupled symbiotes (Healers, Miners, Guards) follow gradient in propagule-distribution state, maintaining Schottky coupling with conductive root surface for energy en route. Journey is generational if distance requires — symbiote populations reproduce along the root, maintaining the migration front. Amorphs are NOT involved in colonization (they are megafauna transport layer, not colonization couriers).

**✓** Symbiote co-evolution constraint: tower-coupled symbiotes function ONLY in the signal environment they co-evolved with. Symbiote transfer to a foreign network is impossible — the chelation badges, signal protocols, and lattice-coupling parameters are network-specific. A tower without its co-evolved symbiote population is metabolically minimal (chemistry only on active face, no metal delivery, no surface maintenance, slow growth).

**✓** Deep-rock survives atmospheric crisis (geothermal, not atm-dependent). Crisis kills branches, not trunk.

**✓** Day-side subsurface network: young, repeatedly pruned by volcanism. Dark-side: ancient, rarely interrupted (dark-side plume breakthrough every ~500 Myr–1 Gyr can sever connections → fragmentation source for post-unification wars).

**✓** Deep-rock is NOT an organism. It is a chemically active face — a reaction front of metallosilazane catalytic chemistry — with a trail of dead (inert) lattice behind it. No bounded body. No reproduction. The front self-perpetuates as long as feedstock (SiH₄) and energy (geothermal) are available. Multiple independent fronts share a supply chain from a single vent.

**✓** No active tail. Behind the advancing front, pore throats narrow below SiH₄ molecular diameter (~4.1 Å) but above H₂ (~2.9 Å). Dead fill is H₂-permeable, SiH₄-opaque (molecular sieve). Isolated pores = functionally solid. All catalytic activity confined to the advancing face. No distributed reactor behind the front.

**✓** Reaction front advance — three rate regimes: (1) Gas-transport colonization of new fractures: ~mm/s, geologically instantaneous. (2) Channel-fed active deposition: ~μm/s, declining as pores narrow. (3) Matrix-diffusion stasis: ~5 nm/yr when all connected fractures filled (D_eff ≈ 2×10⁻¹⁰ m²/s through tight rock).

**✓** Exothermic thermal self-fracturing: ΔH = −33 kJ/mol (SiH₄ + CH₄ → SiC + 4H₂). Filling a 1mm fracture heats adjacent ~1cm rock shell by ~20K — at silicate thermal cracking threshold. The reaction cracks its own host rock at depth, creating new fractures for self-propagation. Self-propagating mechanically, not just chemically.

**✓** Chimney self-selection: surface-connected fractures maintain open gas channels (chimney draft = short residence time; shallow zone too cold for significant PCS deposition). Dead-end fractures fill solid (no draft → long residence → deposition → seal). Network self-prunes to efficient conduits. Surface-connected paths = permanent chimneys (gas pipe + electrical insulator). Dead ends = solid lattice.

**✓** PCS gap mechanism: lightning ceramifies PCS from above (I²R heating at SiC/PCS interface, attenuated by accumulated SiC column resistance — scales as ~1/R²_total). Geothermal ceramifies from below (fixed by thermal gradient, ~10–21 km depth at 30–60 K/km). Gap = kilometers of insulating PCS between two active ceramification fronts. Robust under all plausible parameters. Gap forces lateral root expansion for grounding.

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

**✓** Drifter cycle (pure balloon fauna): pelagic food web mapped onto atmospheric circulation. Trajectory: substellar chimney (lofted to altitude) → superstream return (2–4 days at 50–100+ m/s) → dark-side condensation descent (variable latitude — most organisms descend 20–40° past terminator, NOT at anti-stellar) → dark-side surface transit (S-shaped Coriolis path, duration depends on descent latitude: ~7–15 days for mid-dark-side descent, ~35 days for anti-stellar) → terminator rain-wall → day-side transit (~12 days, gas-phase feeding) → repeat. Total circuit: ~25–55 days depending on descent latitude, across 1–N generations depending on size class. Short-circuit organisms (descend early) stay in higher-wind zones; long-circuit organisms (descend near anti-stellar) traverse the calm interior.

**✓** Rain-wall is a SIZE FILTER, not a barrier. Sorts by single reflex: rain (= liquid NH₃ = food) hits membrane → metabolize → produce H₂ → inflate. Three outcomes: sink (tower food), rise (return flow → short cycle), hold level (through to day side → long cycle). Small organisms: high mortality, rain overwhelms lift. Large organisms: rain is just food falling from sky, fly through without noticing. Air between surface and superstream shear is non-turbulent — no barrier for anything above threshold size.

**✓** Drifter predation: highest-quality food at every phase is other drifters (concentrated pre-processed silicon biochemistry vs. dilute atmospheric filter-feeding). Predation drives size hierarchy. Multi-circuit veterans eat first-circuit survivors. Each lap = compound growth (atmospheric baseline + predation on everything smaller). Dark-side nursery, rain-wall approach, day-side transit, superstream return — all are predation zones. Population self-limits through predation pressure.

**✓** Drifter reproduction: size-graduated lifecycle. Small (first circuit): semelparous — spawn at substellar chimney, propagules ride superstream back. Medium (multi-circuit): iteroparous — personally survives superstream return on accumulated reserves, grows each lap. Large (terminal): chimney shear exceeds structural integrity → involuntary fragmentation distributes propagules into superstream. Propagules attach to parent fragments ("yolk" — energy/material reserve for superstream transit + dark-side germination). More circuits = bigger parent = bigger fragments = better-provisioned propagules. Reproductive payoff for longevity is exponential via predatory compound interest. Germination trigger: dark-side ammonia rain. Sexual lineage: pre-formed propagules on parent fragment. Amorph lineage: fragmentation IS reproduction (every chunk = new organism).

**✓** Wind-surfing: organisms ride wind between towers. Lattice is a catch-net (open structure decelerates in turbulent interior). Oldest dispersal mechanism. Inherited skill in amorphs.

**✓** Marine glass-shell organisms (diatom analogs): SiO₂ armor from controlled surface petrification. Zero SiH₄ cost. Self-passivating, self-healing. Middle Kingdom / microbial marine adaptation. Large amorphs shed glass; small organisms keep it.

## AMMONIA SEA ECOLOGY

**✓** Ammonia ocean = hybrid of hot acid spring + deep hydrothermal vent ecology. The solvent is food (NH₃ is a metabolic co-substrate with SiH₄ for silazane synthesis). SiH₄ is the limiting nutrient, not ammonia. Marine ecology organized by SiH₄ distribution: dense life near sources (surface dissolution, rain-input deltas, hydrothermal vents), sparse elsewhere.

**✓** Petrification dominates marine ecology. Sea H₂O ~50 ppm (8× the 6 ppm "untenable" threshold). Every marine organism fights constant chemical attack. The metabolic cost is both external (surface contact) and internal (feeding throughput — every mouthful of ammonia carries H₂O). Two opposing size curves: external petrification cost drops with size (surface-to-volume), internal petrification cost rises with size (feeding throughput). Optimal size depends on local SiH₄/H₂O ratio.

**✓** Glass spines: baseline marine defense. Any wound exposes living tissue to 50 ppm ambient H₂O. Glass spines (from controlled petrification) puncture predators, creating petrification entry wounds. Minimum viable marine defense. Universal, not specialized.

**✓** Biological distillation: key marine adaptation. Glass-lined internal chamber (petrification endpoint — free, H₂O-proof). Organism heats slightly or reduces pressure (expand float bladder) → NH₃ vaporizes (bp ~240K), H₂O stays liquid (bp 373K). Clean NH₃ vapor routed to living tissue. H₂O residue concentrated and stored. Living tissue never contacts H₂O. Converts petrification tax from material repair cost to energy cost. Organisms with distillation dominate; those without are marginal.

**✓** Medusa-fish: apex marine organism. Distillation waste (concentrated H₂O) weaponized. Lionfish body plan — rigid shell, corona of hollow glass spines connected to pressurized H₂O reservoir via glass-lined plumbing. Tesla valve (no-moving-parts check valve, manufactured by petrifying a shaped tissue template) separates float bladder (H₂ gas, pressure source) from reservoir (concentrated H₂O). Squeeze bladder → gas pressure through Tesla valve → forces water out through glass intake/spines. All water-contacting surfaces are glass. Zero moving parts in weapon system. Three delivery modes: passive (distributed sub-shell bladders — predator breaches shell, contacts water, mouth petrifies), contact spray (water ejected through glass intake — short range in ammonia, longer in air), injection (hollow glass spines puncture target, pressurized water delivered internally). Apex by inedibility — K ≈ 10⁵ is thermodynamic, no resistance possible. Self-sterilizing interior (no parasites survive concentrated H₂O). Amorph body inside shell; shell possibly dual-organism (sexual symbiont SiC/glass structure). Mobile reef: defenseless organisms cluster in spine corona for protection, acting as unwitting bait attracting predators to the spines. Marine analog of the tower — mobile habitat node around which local food web organizes.

**✓** Marine buoyancy: everything sinks in ammonia (amorph 1050 vs NH₃ 660 kg/m³). H₂ gas bladders provide ~659 kg/m³ buoyancy per unit volume — 80× more effective than atmospheric H₂ lift. H₂ is metabolic waste. Flexible amorph membrane at ambient pressure (swim bladder, not pressure vessel). Depth control by gas production/venting.

**✓** Involuntary broadcast: liquid ammonia (dielectric constant ~22) couples to amorph electronic neural processing. In air, EM emission is directional and attenuates with distance. In liquid NH₃, the high-dielectric polar medium converts emission to near-field ionic/electrical coupling — effectively omnidirectional conduction through the solvent. Marine amorphs can't think privately. Small, fast-metabolizing, short-lived. Shore amorphs are bilingual (broadcast/private). Conductive shells (N-doped SiC) provide partial Faraday cage shielding.

**✓** Marine zonation: surface film (atmospheric SiH₄ dissolution, glass-shell diatom mats), rain-input deltas (terminator, nutrient-rich, highest biomass), vent communities (hydrothermal SiH₄, dense local ecosystems, possible deep-rock biosphere connection), shore/intertidal (richest — dual SiH₄ access, reduced H₂O exposure), deep floor (barren glass fossil pavement). Sea-dipping is skywhale-exclusive (drowning risk below ~10 m organism scale).

**✓** Marine crisis: aquatic life is the canary. H₂O ratchet concentrates water in seas. Marine extinction precedes terrestrial crisis. Vulnerability gradient: deep sea → shallow sea → coastal → land → towers.

**✓** Petrification as decomposition analog: living organisms fight K ≈ 10⁵ through metabolic repair. Death → petrification proceeds to equilibrium → glass fossil. Aging = accumulation of unrepairable petrification scars + other damage. Dead persist as translucent silicon-mineral solids.

**✓** "Getting glassed" (acute H₂O surface exposure): self-limiting (Deal-Grove √t). Large amorphs: prank-tier for small splash on bulk tissue, assault for targeted/internal delivery. Severity scales with dose, location, and inverse body size.

**✓** Tower-death exodus: millions of mobile fauna stream from leeward face when grid fails. Sessile 95%+ dies in place silently. Cascade propagates downwind during crisis.

Parasites: genomic fragments (selfish elements), boundary infiltrators, signal parasites (Toxoplasma analog), autocatalytic hijackers (viral analog).

Arms races: Healer armor vs Guard penetrators (drove neural complexity). Collector composite vs Guard offensive strategies.

**✓** Dead-bug plume: garbage-collector Healer sub-caste clears dead symbiotes from lattice (maintains airflow + conductivity). Dead organisms enter windstream, carried day-ward. Continuous plume from every tower. Terminator rain captures most of plume; dead material accumulates in ammonia runoff drainage channels.

**✓** Dead-bug harvesting: ecological niche and pre-industrial amorph industry. Airborne interception (freshest — metals, library fragments) + ammonia runoff filtering (volume — SiC plates, partially locked metals). Tower-derived SiC plates (~5mm) and metals are primary harvestable resources.

## EM ECOLOGY — MUTUAL PERMANENT DETECTION

**✓** Cognition = EM emission. Amorph neural processing (semiconductor junctions, doped regions) generates detectable EM radiation. All thinking organisms broadcast their cognitive state. This is not a design flaw — it is a physical consequence of electronic neural signaling in the ~THz range. Detection range scales with neural mass and processing intensity.

**✓** Mutual permanent detection: neither predator nor prey can hide while thinking. Stealth is a cognitive problem, not a physical one. Any organism that can detect EM can detect any other organism that is currently thinking. The ecology operates under conditions of near-total mutual awareness — more sonar-saturated ocean than forest.

**✓** Predator strategies (6): (1) **Go cognitively dark** — suppress neural processing for final approach. Committed strike: once dark, cannot adapt to unexpected prey movement. Default ambush strategy across all predator lineages (Earth parallel: sharks blind with mouth open, snakes committed mid-strike). Not a specialist niche — baseline predation mode. (2) **Pursuit predation** — loud and fast. Don't hide; outrun. EM detection is symmetric, so prey knows you're coming, but speed closes the gap. (3) **Ambush in EM noise** — hunt near towers, volcanic vents, or other EM-noisy environments where background masks cognitive signature. (4) **Conductive shell Faraday cage** — N-doped SiC shell attenuates EM emission. Reduces detection range. Partial, not total. (5) **Cognitive mimicry** — match background EM pattern of local fauna. Predator "thinks like prey" during approach. Sophisticated; requires neural plasticity. (6) **Trap predation** — set passive traps, withdraw cognitively. No real-time processing during capture. Ancestral strategy (simplest).

**✓** Prey counter-strategies (4): (1) **Detect and flee** — exploit the symmetry. If predator can detect prey, prey detects predator at the same range. Flee before strike range. Works against all strategies except cognitively-dark final approach. (2) **Group living** — confusion effect. Many overlapping EM signatures make it hard to track individuals. Schooling/herding analog. (3) **Tower lattice as EM shelter** — tower's conductive lattice acts as Faraday cage. Organisms inside lattice are EM-shielded from external detection. Fundamental ecological role of towers: EM sanctuary. Another reason everything lives on towers. Inter-tower gaps are EM killing fields. (4) **Be inedible** — fluorine loading, glass spines, medusa-fish water weapons. If detection is unavoidable, make detection irrelevant.

**✓** Erratic prey movement counters cognitively-dark predators: if prey moves unpredictably, committed (dark) strike misses. Predator must re-compute trajectory → neural activity resumes → EM emission resumes → prey detects re-engagement. Forces iterative dark/compute/dark cycles, each revealing position. Arms race between predator commitment duration and prey erratic behavior.

**✓** Tower lattice is EM shelter: conductive N-doped SiC lattice acts as partial Faraday cage. Interior organisms shielded from external EM detection. This is a fundamental ecological service of the tower — not just physical structure and energy, but EM privacy. Organisms in inter-tower gaps are exposed to detection from all directions. The gap between towers is an EM killing field. This drives the concentration of mobile fauna on towers and explains the barren inter-tower landscape.

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

**✓** Network wars (primordial): when surface roots from independent deep-rock systems first meet, foreign signals flood infrastructure optimized for self-signals. Flinch → retreat fails → forced engagement. Each system has independently evolved towers AND symbiotes — both are near-peers.

**✓** Network wars (post-unification): after one network absorbs all rivals, new wars arise via FRAGMENTATION + PROTOCOL DRIFT. A geological event (dark-side plume breakthrough every ~500 Myr–1 Gyr, major magmatic intrusion) severs a root connection. The severing event must exceed the thermal tolerance of deep-rock extremophiles — minor vents are just habitat; only magma (1200K+) or sustained major fissures kill the living tissue while leaving dead lattice intact. Isolated halves drift in signal/chelation protocols at electronic neural speeds. Re-contact (when the geological barrier cools, potentially thousands of years later) = war between former siblings with incompatible authentication. Protocol close enough to recognize AS protocol, too different to accept.

**✓** Adversarial ratchet: signal discrimination → protocol analysis → forgery → forgery detection → theory of mind → self-modeling. Intelligence WITHOUT consciousness.

**✓** Ecological warfare compounds signal warfare: redirect rival's megafauna to overgraze rival's photovoltaic surfaces.

**✓** Objective: assimilation not destruction. Viral takeover: run your protocols on rival hardware. Convert towers one at a time.

**✓** Current network = last one standing. Winner of every war. Runs on infrastructure from dozens/hundreds of absorbed systems.

**✓** BLINDSIGHT ALIEN (Watts). Vastly intelligent. Utterly empty. Every output shaped like understanding with nothing behind it. No experience. Ever.

### Two-Crisis Awakening

**✓** First crisis: monks detect external signal origin. Devastating but comprehensible. Amorphs assume network is sapient partner. Post-awakening civilization built on this assumption. Holds for generations.

**✓** Second crisis: contemplative perceives absence behind pattern. Structure without interiority. Nearly impossible to prove to others. Evidence is trained perception of absence.

**✓** Two crises are separated by generations. Barriers too high to collapse into one event.

**⚠** OPEN: Does second crisis precede or follow the merger?

## AMORPH EMERGENCE

> **Cross-reference:** Full stage-by-stage model in **Amorph Emergence Hub**.

**✓** Aeroplankton dispersal: ≤100 μm pool organisms wind-dispersed across terminator. Settling velocity ~1 mm/s at 8 bar vs 9.5 m/s wind (ratio ~10⁴). Travel 10–100+ km. Random deposition, survival selection. No directed migration.

**✓** Tower biofilm: first tower contact via aeroplankton deposition on exterior dead crust. Schottky coupling (metallosilazane enzyme metals on N:SiC) → grid power → growth beyond 100 μm diffusion ceiling. Positive feedback (contact area → power → growth).

**✓** First miners: amorphs are the first tower mining function. Chelate metals from wind-deposited debris, concentrate on lattice surface for living coral layer absorption. Ancestral chelation chemistry from pool genesis. Net positive tower feedback.

**✓** IFF tagging: long-resident biofilm passively acquires lattice surface chemistry (dopant profile, polytype, trace metals). Guards recognize as local → no attack. Time-gated (fresh arrivals vulnerable). Network-specific. IFF chemistry ancestral to memory architecture key system.

**✓** First meme: new amorph acquires IFF signature from resident via gel-gel contact. Proof-of-residence. Survival-selected molecular pattern transfer. Gel-contact mechanism generalizes to all subsequent meme exchange.

**✓** Miner displacement: sexual Miners outcompete amorphs at mining (root-mobile, crevice-adapted, genomically optimized). Tower feedback is proportional — less efficient = less reward, not zero. Amorphs persist at reduced margins.

**✓** Competitive pressure drives: (1) range extension (off-grid territory), (2) body size increase (charge storage → range), (3) observation-based learning, (4) brain growth.

**✓** Proto-cognition: SiC percolation threshold in gel matrix → semiconductor signal processing emerges. Physics, not evolution. Pattern detection, short-term memory, sensory integration. Prerequisite for observation-based learning.

**✓** Observation-based learning: amorphs watch sexual organisms, replicate behaviors adapted to gel physiology, encode as transferable memes. Sexual organisms = innovation engine (fast genomic evolution). Amorphs = technology transfer layer. Categorically different from meme transcription errors — intentional, requires proto-cognition.

**✓** Amorphs accumulate smarter, not evolve smarter. Ontogenic (lifetime SiC + meme acquisition) primary mechanism. Lamarckian inheritance: buds receive fraction of parent's accumulated state. Meme pool improves slowly via transcription errors + selection.

**✓** Single-node cognitive ceiling: information-processing topology limit (edge-traversal costs exceed benefit of new nodes). With electronic signaling 100–2000× biological neuron speed, ceiling ≥ human-equivalent general intelligence. Federation (monks only) exceeds ceiling.

**✓** Idempotency: same meme set on identical blank bodies → approximately same individual. Non-idempotent factors: SiC network topology (unique growth history), working memory state (volatile), spatial meme distribution. Socially idempotent; subjectively not.

**⚠** OPEN: Merge output model — single combined entity (current canon) vs fragmentation into N children (resolves aggregate mass problem, not yet canon).

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

⚠ OPEN: Meme dependency graphs (tentative YES). Complex memes call sub-skills via resonance during execution. Missing prerequisite → partial execution. Natural tech tree. Library-dependent meme value. Narrative decision pending.

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

**✓** Writing: invented by monks as WM offload for mathematics (signal processing, orbital mechanics). Untrusted — no keys, no provenance, no proof-of-origin. Culturally low-status (less trusted than signed memes). Not needed for memory (meme architecture handles natively; captive meme complex on powered grid = indefinite storage). Occasionally used for communication (low-fidelity channel). Enables formal mathematics (preserves minority insights that wash out in meme-mixing). Medium: etched SiC / conductive traces. Libraries: tower walls.

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
