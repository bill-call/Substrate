# SESSION PROMPT: Amorph Capability Gap Analysis

## Session Goal

Systematic audit of **what we don't know** about amorph biology, ecology, and physical capabilities — specifically the gaps that block building out the technology tree and pre-industrial / industrial economics. The output is a prioritized gap list with dependency chains: what must be resolved first, what can wait, and what is a narrative knob vs a physics constraint.

## Context

Load: CLAUDE.md → spine (`substrate_spine.md`) → this prompt.

Load on-demand as questions arise:
- Chemistry Hub (`substrate_silicon_chemistry_hub (10).md`) — metabolism, materials, catalysis
- Pool Genesis Hub (`substrate_pool_genesis_hub.md`) — lineage origins, energy budget at small scale
- Fauna Structural Hub (`substrate_fauna_structural_hub.md`) — body mechanics, materials, guilds
- Geology Hub (`substrate_planetary_geology_hub.md`) — SiH₄ budget, petrification, crisis
- Bible (`_temp_bible.md`) — full reference when needed

Current version: **v2.3** (February 2026). All documents synchronized.

## What the Technology Tree Requires

A technology tree is a dependency graph: each capability requires prior capabilities plus physical prerequisites. For the amorphs, the tree's *roots* are biological capabilities. We cannot build the tree until we know what the roots are. This session audits those roots.

### Category 1: Energy and Metabolism

**What we have:** SiH₄ is the primary energy source. Atmospheric intake. 34.3 kJ/mol. Geothermal for deep-rock. Photovoltaic and piezoelectric supplement for tower symbiotes. Pool organisms are diffusion-limited (≤100 μm in liquid).

**What we need:**

- [ ] **Reference energy budget for a large land amorph.** Pick a reference mass (e.g., 100 kg). What is resting metabolic rate? Active rate? Peak output for short bursts? Express in watts. Compare to Earth mammals at similar mass.
- [ ] **Energy storage.** What is the silicon-biochemistry analog of fat/glycogen? How much reserve can a 100 kg amorph carry? How long can it fast? This determines: foraging radius, travel range between towers, ability to do sustained heavy work, crisis resilience. *Candidate: polysilane itself? SiH₄ dissolved in silazane oil? Metallosilazane catalyst reserves?*
- [ ] **Gas intake mechanics.** How does a land amorph breathe? Passive diffusion through porous body? Active pumping? What sets the intake rate — surface area, internal transport, or catalytic processing? This determines body-plan constraints at large scale.
- [ ] **Heat dissipation.** Metabolism generates waste heat. At 240K ambient and 8 bar atmosphere, how fast can an amorph dump heat? Is overheating a constraint on peak power output or sustained activity? (Dense atmosphere = good convection, but also good insulation.)
- [ ] **Scaling laws.** How does metabolic rate scale with mass? If it's surface-limited (gas intake), it scales as M^(2/3) — metabolic rate per kg drops with size. If it's volume-limited (catalyst density), it scales as M^1. This has enormous implications for optimal body size and whether bigger = better or bigger = slower.

### Category 2: Cognition and Neural Architecture

**What we have:** Electronic-speed processing. Semiconductor junctions. Native arithmetic/Bayesian. Signal speed 100–2000× Earth neurons. Merge transfers experiential memory.

**What we need:**

- [ ] **Mass-to-brainpower curve.** How does cognitive capacity scale with body mass? In Earth animals, brain size scales as M^0.75 (Kleiber), but cognitive *capability* scales sublinearly with brain size. For amorphs: is neural tissue distributed throughout the body? Is there a central processing mass? Does a 200 kg amorph think twice as well as a 100 kg one, or √2× as well, or barely better? This determines: whether bigger amorphs are smarter, whether there's an optimal size for intellectual work, whether a society of small specialists might outcompete large generalists.
- [ ] **Working memory and attention.** Electronic speed gives fast processing. But how many simultaneous threads? What's the bottleneck — interconnect bandwidth, power supply, noise floor? Can an amorph genuinely multitask, or does electronic speed just mean it serial-processes very fast?
- [ ] **Cognitive cost of body management.** A reconfigurable body requires real-time coordination. How much processing is consumed by proprioception, locomotion, and body-state management? Does this scale with body size? (An octopus devotes significant neural resources to arm coordination.)
- [ ] **Merge bandwidth and latency.** When two amorphs merge, how fast does information transfer? Is it limited by physical contact area? By interface chemistry? By cognitive processing of incoming data? This determines: whether merge is a brief handshake or an extended process, whether partial merge (share one topic) is possible, meeting/conference dynamics.

### Category 3: Senses and Perception

**What we have:** EM sensitivity, IR vision (850 nm matches star peak), piezoelectric vibration sensing.

**What we need:**

- [ ] **EM sensitivity — quantified.** What frequencies? What resolution? What range? Is this a dedicated organ or a whole-body property? Can they resolve direction, or just intensity? Is it passive only, or can they actively probe (radar)? At what power?
- [ ] **Visual system.** IR "vision" at 850 nm — but through what optics? Amorphs have no fixed body plan, so no permanent eyes. Temporary lensing? Distributed photosensitive surface? What spatial resolution? Can they see color (multiple wavelength bands), or is it monochromatic IR?
- [ ] **Acoustic/vibration sensing.** Piezoelectric sensing of vibration — what frequency range? What sensitivity? Can they echolocate in 8-bar atmosphere (sound speed 369 m/s, dense medium = good acoustic coupling)?
- [ ] **Chemical sensing.** Can they "smell"? Taste? Analyze chemical composition of surfaces/atmosphere? If silazane oil is the matrix, dissolved species in the oil could be sensed. Range? Specificity?
- [ ] **Magnetic/electric field sensing.** Semiconductor body in a planetary magnetic field — any useful sensing mode? Could they sense the tower network's EM emissions at range?
- [ ] **Sensory range and resolution envelope.** Combine all senses into a perceptual envelope. At what range can an amorph detect: another amorph? A tower? A predator? A resource? This determines: foraging strategy, social group size, territorial behavior, predator evasion, navigation.

### Category 4: Communication

**What we have:** Modulated EM emission/reception. Radio. Range ∝ power.

**What we need:**

- [ ] **Bandwidth.** How much information per second? Is it comparable to speech (tens of bits/s for semantics), or to broadband (megabits/s for raw experiential data)? Determines: language structure, coordination capacity, group cognition.
- [ ] **Encoding.** Analog or digital? Frequency modulation, amplitude modulation, pulse coding? Can they encrypt (frequency-hop, spread-spectrum)? Privacy in broadcast medium?
- [ ] **Range at various power levels.** Quiet conversation (1m? 10m? 100m?). Shout (1 km?). Full-power broadcast (10 km? 100 km?). How does 8-bar atmosphere affect propagation at relevant frequencies?
- [ ] **Directional vs omnidirectional.** Can they beam a signal at one recipient, or is all communication broadcast? This has massive social implications (private conversation vs everything public).
- [ ] **Interference and noise floor.** In a crowd, can they pick out one voice? What's the equivalent of a cocktail-party problem for EM communicators? Does tower EM emission create background noise?
- [ ] **Non-EM communication channels.** Physical contact (merge without full merge — data handshake?). Chemical signaling (pheromone analog via silazane volatiles?). Acoustic (vibration through ground/air)?

### Category 5: Manipulation and Physical Capability

**What we have:** Pseudopods, arbitrarily reconfigurable. Gel actuators ~5 kPa. Variable rigidity (soft gel → SiC composite). Peristaltic locomotion.

**What we need:**

- [ ] **Force output.** What force can a pseudopod exert? Lifting capacity? Grip strength? Crushing force? Compare to human hand, human arm, industrial robot. Determines: what materials they can work, what tools they need.
- [ ] **Precision.** Finest manipulation scale? Can they do μm-precision work (watchmaking)? mm-precision (carpentry)? cm-precision (masonry)? Determines: whether they need tools for fine work, or ARE the tools.
- [ ] **Speed of reconfiguration.** How fast can the body change shape? Milliseconds (combat-relevant)? Seconds (manipulation-relevant)? Minutes (strategic posture change)?
- [ ] **Sustained vs burst output.** Can they sustain high force output, or is it burst-limited (like an octopus jet)? Linked to energy storage.
- [ ] **Tool use prerequisites.** What can they do bare-bodied that Earth tool-users need tools for? What REQUIRES external tools? This is the foundation of the tech tree — the line between "biology can do this" and "technology is needed."

### Category 6: Ecological Web

**What we have:** Three-tier architecture. Fluorine ecology. Thorn-flora pollination. Balloon fauna. Tower parasites. Wind-surfing. Arms races.

**What we need:**

- [ ] **Energy flow diagram.** Star → SiH₄/photovoltaic → primary producers → ... → apex. Who eats whom? What's the biomass at each trophic level? Where do amorphs sit? Determines: carrying capacity, population density, competition.
- [ ] **Amorph diet and foraging.** What do large land amorphs eat, specifically? Tower lattice scrapings? Free-living organisms? Atmospheric SiH₄ directly? Multiple sources? Foraging time budget?
- [ ] **Predator-prey dynamics at amorph scale.** What threatens a large amorph? Other amorphs? Specialized predators? Environmental hazards? Disease? This determines: social cooperation drivers, settlement patterns, defense technology motivation.
- [ ] **Population ecology.** Carrying capacity per unit area at terminator. Reproduction rate. Mortality rate. Age structure. Growth rate. Do they have population crises? Malthusian limits?
- [ ] **Territorial behavior.** Do amorphs hold territory? What defines it? How is it enforced? Is it individual or group? Linked to communication range and resource density.
- [ ] **Interspecific relationships beyond towers.** Amorphs interact with: towers (symbiosis/management), middle kingdom (indirectly via towers), thorn-flora (fluorine harvesting?), balloon fauna (ignoring?), sea amorphs (distant relatives). Map these.

### Category 7: Social Prerequisites for Technology

**What we need:**

- [ ] **Group size and structure.** How many amorphs cooperate naturally? What limits group size — communication range? Merge bandwidth? Cognitive load? Dunbar's number analog?
- [ ] **Division of labor.** Can amorphs specialize? What drives specialization — body size variation? Knowledge accumulation? Regional adaptation? How does merge interact with specialization (does merging with a specialist make you one)?
- [ ] **Knowledge transmission by channel.** Three currencies (spine): physical (SiC plates), chemical (library fragments/recipes), cognitive (experiential, merge-only). Technical knowledge — procedures, recipes, designs — lives in the chemical channel: discrete fragments, deliberately copied and traded, no regression. Merge transmits experiential knowledge (intuition, skill, spatial memory) indiscriminately with regression to consensus. Key question: for the tech tree, which knowledge classes require experiential transfer (merge) vs procedural transfer (fragments)? An inventor can hand you the recipe without merging. Regression to consensus is NOT a threat to accumulated technical knowledge — it only affects the experiential/intuitive layer.

## Output Format

For each gap identified:

1. **Gap name** (brief)
2. **Blocks** (what downstream capability this gap prevents)
3. **Difficulty** (is this a physics calculation? a narrative choice? an open design question?)
4. **Priority** (MUST resolve before tech tree / SHOULD resolve / NICE to have)
5. **Dependencies** (does resolving this require resolving something else first?)
6. **Candidate answers** (if obvious candidates exist, note them)

Organize into dependency chains: what must be resolved first, what can be resolved in parallel, what is blocked until predecessors are done.

## What This Session Is NOT

- Not building the tech tree itself. That's the next session.
- Not resolving all gaps. Some gaps may require their own deep-dive sessions.
- Not writing new hub documents. Output is the prioritized list.
- Not narrative work. This is engineering prerequisite analysis.

## Success Criterion

A complete, prioritized gap list where:
- Every gap is classified as physics-constrained, chemistry-constrained, or narrative knob
- Dependencies between gaps are mapped
- The critical path to "ready for tech tree" is identified
- No major category has been overlooked
