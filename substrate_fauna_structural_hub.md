# SUBSTRATE — FAUNA STRUCTURAL ENGINEERING HUB

**v2.4 — February 2026**

**Load with:** Spine (required). Silicon Chemistry Hub §6 (carbosilane pathway) and §8 (catalysis) recommended. Pool Genesis Hub §4 (lineage fork) for evolutionary context.

This hub covers structural materials, body plans, and mechanical engineering of mobile life. Both lineages — sexual (exoskeletal, rigid body plan) and amorph (gel, reconfigurable) — are treated, with emphasis on the sexual lineage where structural constraints are most demanding.

---

## 1. THE STRUCTURAL PROBLEM

Mobile organisms on Substrate face three constraints absent on Earth:

| Constraint | Value | Consequence |
|-----------|-------|-------------|
| Surface gravity | 1.82g (17.85 m/s²) | Square-cube law bites harder. Structural mass fraction must be higher. |
| No calcium carbonate | Reducing atm, no CO₂/O₂ cycle | Earth's two dominant biominerals (CaCO₃, Ca₃(PO₄)₂) unavailable |
| No collagen/keratin | No amino acids, no peptide bonds | Earth's structural proteins absent. Must use organosilicon equivalents. |

Available structural chemistries, ranked by specific strength:

| Material | Density (kg/m³) | Compressive strength | Tensile strength | Biological availability |
|----------|----------------|---------------------|-----------------|------------------------|
| SiC ceramic (bulk) | 3,210 | ~3,900 MPa | ~400 MPa (brittle) | ✓ Carbosilane pathway endpoint (Chemistry Hub §6.4) |
| SiC fiber composite (CMC) | 1,800–2,200 | Variable (layup-dependent) | ~2,000 MPa (fiber direction) | ✓ Carbosilane pathway stages 2–3 (Chemistry Hub §6.2–6.3) |
| Polycarbosilane (uncured) | ~1,100 | Low (plastic) | Moderate | ✓ Carbosilane pathway stage 2, extrudable |
| Amorphous metal silicide | 4,500–5,500 | ~1,000–2,000 MPa | Moderate (ductile) | ✓ Metallosilazane enzyme byproduct |
| Graphene / graphite | 2,200 (graphite) | — | ~130,000 MPa (graphene) | ⚠ Requires pure carbon deposition; energy-expensive |
| Silazane gel (body matrix) | ~1,050 | Negligible | Negligible | ✓ Default body material |

**✓ SiC fiber composite is the dominant structural material.** It combines the best available strength-to-weight ratio with biological manufacturability. Bulk SiC is reserved for wear surfaces and lattice mineral. Amorphous metal silicides fill the ductile-joint niche. Graphene is exotic specialization.

---

## 2. SEXUAL LINEAGE — EXOSKELETAL ARCHITECTURE

### 2.1 Why Exoskeleton, Not Endoskeleton

The sexual lineage descends from amphiphile-coated coacervate droplets that evolved SiC shell reinforcement (Pool Genesis Hub §4.2–4.3). The evolutionary sequence is:

```
Amphiphile monolayer → carbosilane cross-links → SiC deposition → rigid shell
```

This is an outside-in pathway. The shell forms at the boundary first and thickens inward. There is no evolutionary path from "soft interior with hard coat" to endoskeleton without first losing the coat — which removes the defense against parasitic merge that drove shell evolution in the first place. Endoskeletons require a different evolutionary origin (soft-bodied ancestor that mineralizes internal supports), and no such pathway exists here.

**✓ Exoskeleton is the only available architecture for the sexual lineage.**

At the spine's stated size range (mm to low-cm), exoskeleton is mechanically adequate. Earth arthropods demonstrate exoskeletal success up to ~30 cm (coconut crab, 3.3 kg in 1g). In 1.82g, the equivalent limit is lower but comfortably above the cm scale.

### 2.2 Shell Composition — SiC CMC

The shell is a **ceramic matrix composite (CMC)**: SiC fibers in a polycarbosilane/silazane matrix, partially ceramified.

| Shell layer | Composition | Function |
|------------|-------------|----------|
| Outer surface | Fully ceramified SiC (β-SiC, 3C polytype) | Abrasion resistance, chemical inertness |
| Structural wall | SiC fiber in polycarbosilane matrix, 40–70% ceramified | Load-bearing. Fiber orientation controls anisotropy |
| Inner surface | Uncured polycarbosilane + silazane gel | Growth face. Living tissue interface |

Fiber orientation is biologically controlled (Chemistry Hub §6.3 — analogous to spider silk extrusion). Organisms can lay circumferential hoops (resist internal pressure), longitudinal fibers (resist bending), or cross-ply laminates (isotropic strength).

**✓ Real-world validation:** Industrial SiC/SiC CMCs (e.g., GE's CMC turbine blades) use exactly this architecture. Density 1,800–2,200 kg/m³, operating temperature >1,300°C, fracture toughness 15–25 MPa√m. The biological version trades peak temperature performance for ambient-temperature self-repair and continuous growth.

### 2.3 Growth Mechanism — Continuous Apposition

**✓ No molting.** SiC shell grows by two distinct processes:

**Marginal growth (volume increase):** New shell material is deposited at growth margins — uncured polycarbosilane strips between existing shell plates (see §3.3). The margin advances outward, enlarging the shell's enclosed volume. This is how the organism gets bigger.

**Inner-surface apposition (wall thickening):** Living tissue at the inner shell face secretes polycarbosilane precursor, spun into oriented fibers against the existing wall. Fe-catalyzed ceramification (Chemistry Hub §8.2) converts outer fiber layers to SiC. The wall thickens from inside. Outer surface erodes (weathering) or is maintained by surface deposition.

This dual growth pattern parallels bivalve mollusks: marginal growth at the aperture edge for volume, nacre deposition on the inner surface for strength. No ecdysis required. The organism never has a soft-shell vulnerable period.

**Growth rate vs. body growth:** The shell constrains maximum growth rate. If the organism grows faster than shell can thicken, structural safety margin drops. Prediction: sexual lineage grows slowly compared to amorphs. Juvenile mortality is from mechanical failure (shell too thin for body mass), not starvation.

### 2.4 Shell Geometry — Voronoi Optimization

At the low-cm scale, a uniform shell wastes material on low-stress regions. Biological optimization produces:

- **Voronoi tessellation**: thick ridges (structural ribs) surrounding thin panels (mass-saving)
- Ridge nodes at stress concentration points (attachment sites, limb bases)
- Panel thickness tuned to local loading — thickest near attachment point and toward predator-exposed faces, thinnest on lattice-contact surface (protected by lattice itself)

This is the geometry described in the spine as "Voronoi armor" for grazers. It arises from the same optimization principle as trabeculae in mammalian bone and diatom frustule geometry: material placed where stress demands it, removed where it doesn't.

The Voronoi geometry also serves an aerodynamic function: ribs act as boundary-layer features (vortex generators) on the dorsal shell surface, and the thin panels between ribs are the substrate for actuatable surface elements (see §10).

---

## 3. JOINTS AND ARTICULATION

### 3.1 The Joint Problem

SiC ceramic is brittle. Fiber composite is tough but stiff. Neither flexes. Every joint in an exoskeletal organism requires a different material — something that deforms without fracturing under cyclic loading.

### 3.2 Amorphous Metal Silicide

**✓ RESOLVED: Amorphous (glassy) transition metal silicides as biological joint material.**

| Property | TiSi₂ (amorphous) | FeSi₂ (amorphous) | Notes |
|----------|-------------------|-------------------|-------|
| Density | ~4,500 kg/m³ | ~4,900 kg/m³ | Heavier than CMC shell; joints are small |
| Character | Metallic glass | Metallic glass | Amorphous = no grain boundaries = no crack propagation |
| Ductility | Good | Good | Elastic strain >2% (vs. <0.1% for crystalline ceramic) |
| Hardness | ~12 GPa | ~10 GPa | Harder than steel, softer than SiC |
| Biological source | Ti-centered metallosilazane enzymes | Fe-centered metallosilazane enzymes | Same metal inventory as catalytic system (Chemistry Hub §8) |
| Deposition | Local enzyme secretion at joint surfaces | Local enzyme secretion at joint surfaces | Analogous to arthropod resilin deposition |

**Formation chemistry:**

```
Metal-silazane precursor complex → amorphous MSi₂ + NH₃ + H₂
(where M = Ti, Fe; precursor is purpose-synthesized, not a catalytic enzyme)
```

Organisms synthesize dedicated metal-silazane precursor complexes (same chemistry class as catalytic enzymes, but simpler — no active-site geometry needed) and secrete them at joint surfaces. The precursors thermally decompose to amorphous MSi₂ via localized resistive heating through the shell. The catalytic enzymes themselves are never consumed for structure.

### 3.3 Joint Architecture

| Joint type | Materials | Application |
|-----------|-----------|-------------|
| Hinge | Amorphous FeSi₂ bearing surfaces, polycarbosilane ligaments | Limb articulation |
| Ball-and-socket | TiSi₂ ball in SiC CMC socket, silazane gel lubricant | Multi-axis joints (mouthparts, grasping) |
| Flexible seam | Uncured polycarbosilane strip between shell plates | Body flexion (segmented forms) |
| Growth margin | Silazane gel + sparse fiber | Expansion zone; ceramifies as organism grows |

Polycarbosilane ligaments (uncured, fiber-reinforced but not ceramified) provide tension resistance at joints. These are the tendons of the system — flexible organosilicon cables connecting rigid shell segments.

---

## 4. INTERNAL BRACING — THE APODEME SYSTEM

### 4.1 Why Internal Structure Is Needed

At the mm scale, the shell alone suffices. A 1 mm SiC CMC sphere with 50 μm walls has a wall-to-diameter ratio of 1:20 — structurally overbuilt.

At the cm scale, unsupported shell panels buckle. The shell needs internal bracing. Earth arthropods solve this with **apodemes** — internal projections of the exoskeleton that serve as muscle attachment points and structural stiffeners.

### 4.2 SiC Foam and Fiber Struts

| Internal structure | Composition | Function |
|-------------------|-------------|----------|
| Apodemes | SiC CMC extensions from inner shell wall | Muscle (gel-actuator) attachment; structural stiffeners |
| Foam partitions | Open-cell node-reinforced PCS/SiC foam | Lightweight space-filling structure; prevents shell buckling; gas-permeable for internal SiH₄ metabolism |
| Fiber struts | Oriented SiC fiber bundles spanning shell interior | Tension ties between opposing shell walls |

**SiC foam** is real: manufactured industrially by foaming polycarbosilane precursor, then ceramifying. Biologically produced by H₂ gas-blowing during PCS secretion at the inner growth face (§2.3).

✓ **RESOLVED: Node-reinforced polymer foam. Partial ceramification only.**

**Manufacturing pathway:**

1. PCS precursor extruded at growth face, loaded with Fe catalyst particles. Metabolic H₂ injected as blowing agent.
2. Bubbles expand; PCS cross-links around them. Open-cell structure forms as thin membranes rupture between adjacent bubbles.
3. Fe particles concentrate at strut junctions (Plateau borders) during foaming — surface tension and drainage in the wet foam naturally sweep particles toward nodes. No biological control needed; physics does it.
4. Lattice current flows through the foam (shell → foam struts → opposing shell). Nodes are hottest (current from multiple struts converges) and have highest Fe catalyst concentration → ceramify first.
5. Structural gradient: foam nearest the shell gets most current → most ceramified. Deeper foam remains mostly PCS.

**End product:**

| Component | Material | Role |
|-----------|----------|------|
| Nodes (strut junctions) | SiC ceramic (Fe-catalyzed, ~10–15% of foam mass) | Primary load-bearing |
| Strut cores | Partially ceramified PCS | Tension ties between nodes |
| Cell membranes | Cross-linked PCS (uncured) | Gas-permeable partitions. Minimal structural role. |

Open-cell is required — the organism needs internal gas permeation for SiH₄ metabolism. The foam is a structural lung. Density 200–600 kg/m³, tuned by H₂ injection rate (gas fraction) and ceramification current (node stiffness). High-stress regions (limb bases, apodeme anchors) get dense, heavily ceramified foam. Low-stress fill zones get light, mostly-PCS foam. Energy cost ~1/10th of full-wall ceramification.

Foam partitions create a sandwich-panel structure: dense outer shells with lightweight foam core. This is the optimal architecture for resisting bending and buckling loads — identical in principle to aircraft honeycomb panels and bird bone pneumatization.

### 4.3 Gel Actuators

No muscles. The sexual lineage inherited gel-based actuation from coacervate ancestors (Pool Genesis Hub §3.4):

- Silazane gel regions between apodemes contract/expand under applied electric fields (electroactive polymer response)
- Polysilazane has polarizable Si-N bonds; field-induced conformational changes drive volume change
- Command signal is electronic throughout — no ionic transduction step. Consistent with spine's all-electronic neural motif.
- Response speed: faster than Earth muscle (~100–2,000× neural signal speed; spine §Biochemistry)
- Force output: limited by gel dielectric response and apodeme attachment area

✓ **RESOLVED: Gel actuator stress ~2–7 kPa (central estimate ~5 kPa). ~50× below Earth muscle. Adequate for slow locomotion; fast actions require springs.**

**Force physics:** Two contributions under applied electric field:

| Mechanism | Stress | Notes |
|-----------|--------|-------|
| Maxwell stress (ε₀ × ε_r × E²) | ~1.5 kPa | ε_r ≈ 6 for polysilazane. |
| Electrostrictive (M × E² × modulus) | ~0.5–5 kPa | Polar Si-N bonds, non-ferroelectric. Considerable uncertainty in M. |
| **Total** | **~2–7 kPa** | Central estimate ~5 kPa |

Voltage source: series-stacked SiC semiconductor junctions (~2.7–3V each). 100 junctions in series (alternating p/n doped regions, each μm-scale, total stack <1 mm) = ~270V. Over 50 μm gel layer: E ≈ 5.4 MV/m. Well below breakdown.

**Performance by application:**

| Application | Calculation | Result | Adequate? |
|------------|-------------|--------|-----------|
| **Locomotion** | 5 kPa × 0.2 mm² per limb = 1.0 mN; body weight = 1.4 mN; 8 limbs total = 5.6× weight | ~0.5–2 cm/s scaffold crawling | ✓ Slow but sufficient. Armor not evasion. |
| **Spring reload (Guards)** | 5 mm³ gel, 75 J/m³/cycle, 20 Hz → 7.5 μW into 3.75 mJ spring | ~8 min between strikes | ✓ Ambush-compatible. One-shot doctrine — miss and wait. Intense selection for target discrimination. |
| **MEMS surface** | 5 kPa × 0.01 mm², 1 μg scale, 5 μm travel | ~70 Hz per scale, ~15 ms full surface reconfiguration | ✓ Adequate for turbulent flow adaptation (~1–100 Hz). |
| **Fast voluntary movement** | Not possible | — | Spring mechanisms required (§9.3). |

The organisms are slow and weak by Earth standards. The tower ecology doesn't require speed or power — it requires grip, armor, and electronic intelligence. Electronic neural speed (100–2,000× Earth) means fast perception and decision; gel actuation means slow, deliberate movement. Think fast, act carefully.

### 4.4 Electroactive Silazane Actuators (ESA) [NEW V2.5]

ESA is gel actuation with organized electrode/dielectric layering — the same relationship as smooth muscle to striated muscle on Earth. Same base chemistry (silazane + SiC), but organized into thin dielectric films between SiC electrode layers at the actuator site. Maxwell stress at high field (80 MV/m) in the thin organized layer yields ~100–230 kPa — 20–45× gel stress.

| Property | Gel (smooth) | ESA (striated) |
|---|---|---|
| Stress | ~5 kPa | ~100–230 kPa |
| Organization | Bulk, unstructured | Layered electrode/dielectric |
| Cycle rate | ~1 Hz | 5–100+ Hz |
| Power density | ~0.7 W/kg | ~100–200 W/kg |
| Evolved for | Internal processes, peristalsis | Joint actuation, fast locomotion |

ESA is a general capability of silicon biochemistry — all middle-kingdom organisms have the raw materials. The evolutionary step is organizing them into actuator geometry at joint sites (genomically encoded structural arrangement, not new chemistry). ESA enables active walking beyond the 5–8 cm gel ceiling, pushing the size regime to ~25 cm (atmospheric power) or ~50+ cm (day-side with solar supplement). Energy-limited, not stress-limited. Binding constraint shifts from actuator force to charge budget.

**Key ecological consequence:** ESA enables middle-kingdom runners — fast, legged organisms that outrun amorph prey. Daystriders (40–60 kg, 8 m/s sprint) and ESA-powered subwoofer packs (1–2 m/s sustained pursuit) are the primary examples. See Daysider Mount Hub §1–4.

---

## 5. AMORPH STRUCTURAL ENGINEERING

### 5.1 The Default State: Gel

Amorphs are coacervate descendants that never evolved a permanent shell (Pool Genesis Hub §4.3). The body is silazane gel at ~1,050 kg/m³. No fixed body plan.

### 5.2 Variable Rigidity

The spine states: "Rigidity: Variable: soft gel → full SiC composite, real-time, regional."

Mechanism:

| Rigidity level | Chemistry | Timescale | Reversibility |
|---------------|-----------|-----------|---------------|
| Soft gel | Silazane gel, no reinforcement | Default | — |
| Stiffened gel | Silazane gel with suspended SiC particles/short fibers | Seconds (redistribute existing stock) | ✓ Fully reversible |
| Rigid composite | Oriented SiC fiber in gel matrix, partially ceramified | Minutes–hours (spin + partial cure) | ⚠ Partially reversible (can resorb uncured polymer; ceramic permanent) |
| Full ceramic | SiC plate or composite, fully ceramified | Hours–days | ✗ Irreversible (SiC is the thermodynamic endpoint) |

Amorphs carry a dispersed inventory of SiC fibers and particles within their gel body. Regional stiffening = concentrating existing stock into a local zone and aligning fibers. This is seconds-fast and fully reversible. Growing new ceramic is slow and committed.

### 5.3 Post-Revolution Composite

After the carbosilane revolution (Chemistry Hub §6, spine §Civilization), amorphs manufacture SiC fiber composite from atmospheric feedstocks. Pre-revolution, they scavenge SiC from dead grazers and tower detritus (shell economy). The revolution doesn't change the structural engineering — it changes the supply chain.

### 5.4 Scale Advantage

Amorphs become megafauna only after the pool-to-land transition (Pool Genesis Hub §6), which removes the diffusion-limited energy bottleneck. At megafauna scale, the gel body's reconfigurability is a decisive advantage: no fixed body plan means no structural commitment. An amorph can be a flat sheet (maximum surface area for gas exchange), a sphere (minimum surface area for heat retention), or a spiked mass (defensive) as the situation demands.

Fixed exoskeletons cannot do this. The sexual lineage's architectural commitment to rigid body plans locks them into the middle kingdom. Amorphs' structural flexibility is why they alone become megafauna.

### 5.5 Sensory Systems — Vision [NEW IN V2.4]

Amorphs are primarily electromagnetic and acoustic beings. Their membrane is photosensitive but they have not developed eyes with lenses. Vision is a secondary sense, not the primary world-model input.

**Sexual lineage (fixed exoskeleton):** Pit eye — a concavity in the shell lined with photosensitive membrane. Pinhole-camera principle. Low resolution, fixed geometry. Adequate for light/dark discrimination, crude motion detection, basic shape recognition. Insect-level at best.

**Amorph lineage (reconfigurable):** Parabolic reflector eye — a concave body surface (polished SiC coating or polished gel), with an extruded stalk bearing a photosensitive membrane patch at the focal point. A reflecting telescope as a body part.

| Property | Detail |
|---|---|
| Aperture | Reconfigurable; limited by body budget. 10–20 cm practical. |
| Focal length | Limited by stalk structural integrity in 1.82g. Short focal lengths preferred. |
| Image construction | Single focal-point sensor + electronic signal processing. Spatial model built computationally, not optically. |
| Reconfigurability | Change aperture, focal length, pointing direction. Retract when not needed. |
| Gravity constraint | 1.82g limits stalk length. Larger apertures (longer focal lengths) require proportionally stronger stalks. Practical ceiling on biological reflector size. |

The signal processing required to construct spatial models from focal-point data is a **meme** — developed once (hard, requires significant cognitive investment), then transferable to any amorph instantly. Post-meme-transfer, any amorph can reshape into a reflector and "see." Vision is a skill you install, not an organ you grow.

**No vision defects.** A reconfigurable reflector has no concept of nearsightedness or astigmatism. Blurry image = asymmetric mirror = reshape it. The human tradition of corrective optics is a non-sequitur for a creature with adjustable biological optics.

**Industrial optics [LATE TECH TREE]:** Manufactured SiC parabolic mirrors produced by CVD deposition onto precision-shaped mandrels (EDM-machined metal). Coupled with bred organic photosensor arrays and existing signal-processing memes. Pure reflecting optics — no lenses required. No lens grinding — mirrors grown by vapor deposition, the same process used for everything else. Lenses are a niche technology at best (microscopy, spectroscopy). See Heavy Industry Hub §9.1.

### 5.6 Overpressure Tolerance — Thunder-Skin and Blast Resistance [NEW IN V2.4]

The terminator has continuous lightning in an 8-bar atmosphere. Thunder at 8 bar is a shockwave, not merely sound — the lightning channel expands into 8× Earth air density, producing overpressure pulses physically damaging at ranges where Earth thunder is merely loud. The terminator soundscape is a permanent barrage of overlapping shockwaves (Geology Hub §8).

**Size-selective coupling.** Thunder's dominant energy is at 20–500 Hz. At ~366 m/s sound speed, the corresponding wavelengths (0.7–18 m) are far longer than middle-kingdom organisms (mm–cm). A pressure wave must be ≥0.1λ relative to body size to create damaging differential stress. Tower symbiotes are effectively immune — the wave washes over them as uniform compression. Amorphs (0.1–2+ m) are in the coupling regime. The larger the amorph, the deeper into thunder's peak energy spectrum it reaches. Megafauna are broadband thunder antennas.

**Thunder-skin meme.** The countermeasure is ancient — billions of years old, refined to a one-step deployment, carried by every amorph lineage. All amorphs originate at the terminator; the meme predates dark-side colonization.

Mechanism: the amorph textures its outer membrane into an acoustic impedance baffle. Gas-pocket sub-membrane layer (compressible buffer absorbs/reflects acoustic energy before it reaches the gel body) plus cm-scale Helmholtz cavity pitting (resonant absorption at dominant thunder frequencies, tunable by reshaping cavity geometry). The effect: break the smooth impedance match between atmosphere and gel, scattering and absorbing incoming shockwave energy at the surface.

Trade-off: baffled membrane sacrifices some sensing acuity and gas-exchange efficiency. Amorphs switch between "listening" configuration (smooth, sensitive) and "sheltering" configuration (textured, baffled) as conditions demand.

**Exoskeleton as blast shield.** Sexual-lineage SiC CMC exoskeletons provide inherent overpressure protection. The sealed shell distributes pressure loads across the entire surface. Joint seals are the vulnerability — the same amorphous metal silicide joints that are the structural weak point (§2.3) are also the acoustic weak point.

**Tower interior as shelter.** The porous lattice structure baffles and attenuates shockwaves. Deeper interior = more attenuation. This is a selection pressure on tower-dwelling: organisms that live deeper in the lattice experience less acoustic stress. The depth gradient (§4) maps to an acoustic gradient — windward face is loudest, deep interior is quietest.

**Dark-side populations.** Dark-side amorphs (monks, contemplatives) carry the thunder-skin meme and can deploy it. They are not physically fragile at the terminator. However, the aggregate sensory environment of the terminator (continuous EM from lightning, dense network chatter, industrial noise, population density, wind, lattice hum, managed thunder) overwhelms cognitive filters tuned for dark-side silence. The barrier is sensory recalibration, not acoustic vulnerability. (Narrative Notes §XIV.)

**Warfare implication.** Electrohydraulic blast weapons (Heavy Industry Hub §3.8, Warfare Hub §3.1) must exceed the protection provided by thunder-skin — which is specifically tuned for *thunder* frequencies. A weapon that delivers energy at different frequencies, or at intensities beyond the baffle's absorption capacity, bypasses the evolved defense. Blast weapons are an arms race against a known countermeasure.

---

## 6. MATERIALS BUDGET — METABOLIC COST

All structural materials derive from atmospheric SiH₄ and CH₄ via the carbosilane pathway (Chemistry Hub §6). Energy costs:

| Material | Pathway | Energy cost per kg | Notes |
|----------|---------|-------------------|-------|
| Polycarbosilane (uncured) | SiH₄ + CH₄ → methylsilane → polymer | ⚠ Low | Catalytic, ambient temperature |
| SiC fiber (oriented) | Polycarbosilane + extrusion | ⚠ Moderate | Mechanical work of extrusion + alignment |
| SiC ceramic (ceramified) | Fiber + Fe-catalyzed heating | ⚠ High | Requires localized heating to >400°C. Dominant energy cost. |
| Amorphous metal silicide | Metal-silazane precursor + local heating | ⚠ Moderate | Opportunistic; small volumes at joints only |
| Graphene | CH₄ → C (pure carbon deposition) | ⚠ Very high | Requires stripping all H from carbon; no biological shortcut |

**⚠ Ceramification is the bottleneck.** Growing uncured polycarbosilane is cheap. Converting it to SiC is energy-intensive. Organisms manage this by ceramifying only where needed — wear surfaces, structural ribs, apodeme attachments — and leaving non-critical regions as uncured polymer. A fully ceramified organism would be structurally overbuilt and energetically bankrupt.

**Graphene** requires depositing pure carbon with no silicon or nitrogen contamination. This demands a metabolic pathway orthogonal to the main carbosilane route. Only organisms with extreme selective pressure for tensile strength (e.g., ballooning tethers, railgun projectile components) would evolve it. It is never the default.

---

## 7. SIZE-STRUCTURE SCALING

How structural requirements change with body size across the three-tier architecture:

| Tier | Size range | Dominant structure | Limiting factor |
|------|-----------|-------------------|----------------|
| Microbial | <100 μm | None (gel cohesion sufficient) | Surface tension, not mechanics |
| Small middle kingdom | 100 μm – 2 mm | Thin SiC CMC shell, no internal bracing | Shell production rate vs. growth rate |
| Large middle kingdom (tower-coupled) | 2 mm – 2 cm | SiC CMC shell + apodemes + foam partitions | **Energy extraction** via Schottky contacts (scales R²) vs metabolism (scales R^2.55). Crossover ~2 cm. |
| Large middle kingdom (free-living, gel-only mobile) | 2 cm – 8 cm | SiC CMC shell + extensive internal bracing | **Gel actuator force/weight** drops below 1 for active walking at ~5–8 cm. |
| Large middle kingdom (free-living, ESA mobile) | 8 cm – 50+ cm | SiC CMC shell + ESA actuators at joints | **[NEW V2.5]** Energy budget, not stress. ESA (§4.4) provides 20–45× gel stress. Largest on day side (solar supplement). Daystriders, large subwoofer runners. See Daysider Mount Hub §2. |
| Large middle kingdom (free-living, anchored) | 5 cm – 30 cm | Shell as armor; foam/strut internal bracing carries majority of structural load | Internal bracing complexity. Wind-anchored, limpet-style locomotion. Not walkers. |
| Megafauna (amorph) | 10 cm – 2 m+ | Variable: gel with redistributable SiC stock | Energy budget (gas-phase SiH₄ diffusion) |

**The 2 cm wall — SCOPED TO TOWER SYMBIOTES:** [CORRECTED V2.4] The ~2 cm ceiling applies to **tower-coupled** organisms whose energy intake is limited by Schottky contact extraction from the lattice. This is a metabolic limit, not a structural one. SiC CMC has ~15–30× the specific strength of chitin; the structural limit for an SiC exoskeleton in 1.82g is well over a meter and is never the binding constraint at biological scales.

**Free-living sexual organisms (gel-only)** face different ceilings depending on their locomotion strategy. Atmospheric SiH₄ metabolism in gas phase provides ~13 W for a 15 cm organism (~3× metabolic need), removing the tower energy bottleneck entirely. The binding constraint becomes the gel actuator: at ~5 kPa (50× weaker than Earth muscle), force-to-weight drops below 1 around 5–8 cm for active walking. Above this, gel-only organisms must adopt anchored/semi-sessile body plans — wind downforce supplements actuator force, enabling ambush predation at 10–30 cm (e.g., subwoofers, Fauna Hub §6).

**[REVISED V2.5] Free-living sexual organisms (ESA-powered)** break the gel ceiling. ESA actuators (§4.4) provide 20–45× gel stress, enabling active walking and running well beyond 8 cm. Energy budget replaces actuator stress as the binding constraint. On the day side (solar + atmospheric + thorn-flora charging), ESA organisms reach 40–60 kg (Daystriders). At the terminator (no solar, no thorn-flora), ESA organisms are smaller but still significant (subwoofer pack runners at 15–25 cm). The ~30 cm soft ceiling for sexual organisms remains approximately valid at the terminator but is broken on the energy-rich day side.

Amorphs bypass structural limits because they have no committed structural mass. Every gram of SiC is redistributable. The cost is paid in versatility: an amorph at 50 cm is less mechanically efficient than a dedicated exoskeletal form would be at 2 cm, but above ~30 cm amorphs still dominate numerically (cognitive advantages, reconfigurability). ESA exceptions are ecologically significant but confined to high-energy environments with strong speed-selection pressure.

---

## 8. TOWER-SYMBIOTE INTERFACE — MUTUALISM, NOT PARASITISM

The spine describes the middle kingdom as "tower-locked electrical parasites." This is the naive view — energy flows from tower to organism. The full picture is mutualistic. The tower tolerates (and the network actively manages) the middle kingdom because the middle kingdom provides services the tower cannot perform alone. A pure parasite population would be starved out by network energy-gradient modulation in geological time.

### 8.1 What the Tower Gets

| Service | Provider | Mechanism |
|---------|----------|-----------|
| **Surface maintenance** | Healers (sessile + mobile) | Capture wind-blown grit, volcanic ash, and biological fouling. Incorporate mineral material into own shell and deposit excess as tower surface repair. Fouling consumed as food — immune defense is a side effect of surface processing, not a separate behavior. Sessile Healers armor the surface in life and donate shell as permanent lattice on death. |
| **Catalytic metal delivery** | Miners (mobile) | Transport metals from exterior surface through pore network to living layer reaction sites (see §8.5). Critical — without miners, the living layer exhausts local rock metal sources. |
| **Population quality control** | Guards (mobile) | Cull damaged, slow, or structurally compromised Healers and Miners. Ambush predation removes organisms that consume tower energy without delivering adequate service. |

### 8.2 Attachment

**Sessile majority** (spine: "most tower fauna fixed in place for life"). Attachment = SiC-to-SiC ceramification weld:

- Organism secretes polycarbosilane at contact surface
- Ceramification welds organism's shell to tower lattice
- Bond is permanent. Organism cannot detach without breaking shell.
- Lattice position is a one-time, irreversible commitment.

**Mobile minority** (mobile Healers, Miners, Guards). Attachment = mechanical grip, NOT ceramification:

- SiC hooks, claws, or friction pads engage lattice pore geometry
- No permanent bond. Organism traverses lattice surface.
- Trade-off: mobile fauna sacrifice the low-resistance electrical contact of a ceramification weld. Energy extraction is less efficient (Schottky contact via claw tips rather than broad ohmic weld). Compensated by ability to relocate.

### 8.3 Electrical Contact

Energy extraction requires Schottky/ohmic junction at shell-lattice interface (Pool Genesis Hub §8). The organism's ventral shell surface is enriched in Ti-centered metallosilazane — the same contact chemistry as semiconductor industry ohmic contacts to SiC. The structural shell doubles as the electrical interface.

### 8.4 Orientation (Sessile Forms)

Sessile organisms orient with ventral surface against lattice (electrical contact), dorsal surface facing lattice interior (gas exchange, predator exposure). Shell geometry reflects this asymmetry:

- Ventral: flat, thin, Ti-enriched (broad ohmic electrical contact)
- Dorsal: convex, thick, Voronoi-ribbed (structural + defensive)
- Lateral: growth margins (expansion zones)

Mobile forms lack this fixed asymmetry. Shell is more symmetrical; electrical contact is through limb tips rather than a dedicated ventral surface.

### 8.5 The Mining Guild — Catalytic Metal Delivery

✓ **RESOLVED: Miners transport metals from exterior surface to living layer via chelation exchange.**

**The tower's problem:** The living layer is subsurface (mm-cm below exterior). It needs catalytic metals (Ni, Fe, Ti, Co) for its metallosilazane enzymes. Wind-deposited minerals land on the outermost lattice surface. Solid SiC lattice sits between. Metals don't diffuse through ceramic. The tower has a metal logistics bottleneck.

**The miners:** A mobile guild specialized for metal transport.

1. Miner forages on exterior lattice surface — scrapes mineral grit, consumes dead organisms' metal-rich remains, ingests wind-deposited volcanic ash
2. Metals incorporated into excess metallosilazane complexes (carried beyond own metabolic needs — dedicated storage inventory)
3. Miner follows energy gradient inward (network makes subsurface zones energy-rich, surface zones energy-poor)
4. At the living layer interface, the living layer extracts metals from the miner using **chelation chemistry** — the same mechanism as the immune system, run cooperatively
5. Miner is left alive, metal-depleted, paid in lattice energy
6. Energy gradient now points outward (miner is depleted, surface has higher marginal value) → miner returns to surface for another load

The miner doesn't "decide" to deliver metals. It follows energy gradients. The network optimizes the delivery pipeline by shaping the energy landscape. Blindsight logistics.

**Storage and population economics:** Miners carry ~5–10% body mass as surplus metallosilazane cargo complexes (same chemistry class as catalytic enzymes, simpler structure — designed to be surrendered at chelation toll). Net metal per trip: ~0.5–1% of body mass. Delivery is distributed along depth transects — each run crosses ~450 strut layers through the living zone (~2.25 m at 5 mm pore spacing), with chelation toll extracting a fraction at each crossing. A mature tower (~450,000 m² face × ~900:1 surface amplification from lattice porosity ≈ 400 million m² living layer) requires ~10 million miners. This is a negligible fraction of total tower population (billions) and an insignificant draw on tower energy budget. Miner body size optimizes around 3–8 mm (cargo scales with volume; structural cost and lattice traversal efficiency set the ceiling).

### 8.6 Chelation: Immune Weapon and Mutualistic Toll

✓ **RESOLVED: Immune system evolved first. Mutualistic tolerance is the derived state.**

**Evolutionary sequence:**

| Stage | Chelation behavior | Effect |
|-------|-------------------|--------|
| 1. Ancestral | Indiscriminate metal stripping — kill everything contacting living layer | Pure immune defense. All organisms destroyed. |
| 2. Resistance | Some organisms evolve sacrificial metallosilazane decoys — core enzymes protected, excess metals stripped | Organisms survive contact. Not welcome; hard to kill. |
| 3. Net benefit | Living layer variants that tolerate resistant organisms get repeated metal deliveries (many visits > one kill) | Selection for tolerance. Proto-mutualism. |
| 4. Authentication | Molecular handshake distinguishes mutualist from invader. Correct surface chemistry → toll (gentle extraction). Wrong chemistry → kill (full stripping). | Mature mutualism with immune exclusion. |

**The immune system IS the mutualism mechanism.** Same chelation chemistry, different calibration, gated by molecular authentication. An organism without the correct handshake — foreign tower lineage, novel species, damaged/mutant — triggers the kill response.

### 8.9 Authentication Chemistry — Biological Public-Key Infrastructure

✓ **RESOLVED: Static chemical badge read by chelation effector binding specificity. [v2.4+ reframe:] This IS cryptographic — biological public-key authentication. MHC is crypto.**

The middle kingdom organism is an insect. It cannot compute a challenge-response. But the authentication is asymmetric: the badge (public key) is easy to verify (Guard binding-site recognition, constant time) and hard to forge (requires the correct metabolic machinery — the private key — not just surface replication). Network wars drove key complexity to extreme levels. The adversarial ratchet's forgery/forgery-detection arms race is a cryptographic arms race.

**The badge:** A characteristic ventral-surface metallosilazane pattern — specific metal centers (from the Ni/Fe/Ti/Co inventory), specific ligand geometries, specific spatial arrangement on the contact face. Set during larval bootstrap (§9.6 steps 6–7) when the ventral ceramification plate forms. Inherited via library recipes. Does not change after shell closure.

**The read:** Chelation effectors in the living layer have binding sites shaped by co-evolution with the local middle kingdom. Effector binds the expected pattern → conformational shift → toll mode (partial, gentle metal extraction). Effector fails to bind → default kill mode (full stripping). The decision happens during molecular contact. No signal exchange. No EM resonance channel. No tower-issued key.

**Fourth speciation axis.** Badge compatibility joins hook-lattice geometry, cognitive protocol, and library addressing as independent axes of reproductive/ecological isolation. An organism with correct hooks and library addressing but the wrong ventral badge still dies at the living layer interface.

**Anti-forgery defenses:**

| Defense | Mechanism |
|---------|-----------|
| Pattern complexity | High-dimensional metallosilazane space — multiple metal centers × ligand geometries × spatial arrangement. Partial match insufficient. |
| Lethal default | Kill mode is the default. Failed forgery = death, not rejection. Heavy selection against bad attempts. |
| Network-side rotation | Network controls chelation effector expression. Can shift accepted patterns on generational timescale. Organisms carrying the new pattern survive; others selected out. |
| Delivery-contingent reward | Badge passes the kill/toll gate. But energy reward is contingent on actual metal delivery. A forger with the right badge but no metals survives but earns nothing — unprofitable parasitism. Two filters in series. |

**✓ Spine updated:** Three-Tier Architecture now reads "tower-locked mutualists" with services listed. Biochemistry §Immune system now describes both kill and toll modes with molecular handshake gating.

### 8.7 Three Guilds — Healers, Miners, Guards

| Guild | Ecological role | Body plan specialization | Tower benefit | Mobility |
|-------|----------------|------------------------|---------------|----------|
| **Healers** | Primary tower construction AND demolition. Surface maintenance, structural accretion, lattice renovation, chimney/chamber excavation | Robust windward-adapted shell, scraping/processing mouthparts, concave ventral shroud with field-emitter array for arc-CVD | Construction (arc + CVD = deposit SiCN) + destruction (arc without CVD = vaporize SiC at ~2700°C). Same tool, two modes. Healer genomes encode architectural behavior selected over Gyr via energy-gradient tropism. Symbiote genomes = tower construction program. | Both sessile and mobile forms. Sessile = permanent armor + chemical fill. Mobile = targeted arc-CVD construction/demolition. |
| **Miners** | Transport metals exterior → living layer | Metal storage capacity (large metallosilazane inventory), deep lattice traversal | Catalytic metal delivery | Mobile only. Depth-transect cycling. |
| **Guards** | Cull damaged/inefficient Healers and Miners | Spring-loaded strike apparatus (§9.3), ambush morphology | Population quality control — remove organisms consuming energy without delivering adequate service | Mobile only. Patrol + ambush. |

All mobile guild members are 8-limbed scaffold-climbers (§9.4). Differentiation is in mouthparts, storage capacity, shell robustness, and behavioral response to energy gradients — not gross body architecture. Healers additionally span the sessile/mobile divide: sessile Healers are the "most tower fauna fixed in place for life" (spine §Ecology), while mobile Healers range across exterior surfaces.

### 8.8 Healer Repair Mechanisms

✓ **RESOLVED: Two repair modes — chemical fill (shallow damage) and arc-CVD (deep/precision repair). Both tower-powered.**

**Mode 1 — Chemical fill.** For shallow, wide erosion damage (grit abrasion, surface weathering). The Healer metabolizes captured grit into polycarbosilane precursor and secretes PCS onto the lattice surface through its ventral contact zone. PCS infiltrates pits and shallow cracks. Ceramification follows via resistive contact heating — current from the lattice flows through the organism's ventral plate, heating the PCS at the interface. Same positive-feedback mechanism as larval bootstrapping (§9.6). Low energy cost, continuous, adequate for routine surface maintenance.

**Mode 2 — Flow-through arc-CVD.** For deep cracks, complex defect geometries, and precision repair. The Healer positions over the defect as a **flow-concentrating shroud**, not a sealed chamber.

**Why not sealed:** A sealed mm-scale cavity at 0.3% SiH₄ contains ~47 ng of depositable SiC — less than one atomic layer over the repair area. Feedstock exhausts instantly. Exhaust gases (H₂) accumulate and dilute. A sealed batch reactor does not work at this SiH₄ concentration.

**Flow-through mechanism:** The organism's concave ventral surface creates a restricted channel over the defect. Wind-driven atmospheric flow (continuous in the lattice) enters from one edge, passes through the arc zone at the throat, and depleted gas + H₂ exhaust exits the opposite edge. The atmosphere IS the continuous feedstock supply, driven by the ever-present wind. The organism charges from the lattice, then discharges through sharp SiC field-emitter structures into the flowing gas. The arc ionizes SiH₄ + CH₄; radicals deposit SiCN on the defect surface (closest cold surface to the plasma).

| Feature | Detail |
|---------|--------|
| Energy source | Tower lattice (not organism metabolism). The Healer is a power tool the tower energizes. |
| Feedstock | Atmospheric SiH₄ (0.3%) + CH₄ (10%), continuously replenished by lattice wind flow. No metabolic synthesis needed. |
| Deposit composition | SiCN (silicon carbonitride), not pure SiC. NH₃ (12.5% atm) incorporates nitrogen. SiCN is a legitimate engineering ceramic — hardness comparable to SiC. Chemically consistent with nitrogen-rich silazane biology. |
| Gravity independence | Depositing radicals have thermal KE ~5×10⁻²¹ J; gravitational PE over 1 mm gap ~3×10⁻²⁸ J. Gravity is 7 orders of magnitude below thermal energy. Deposition is conformal regardless of surface orientation. |
| Field emission | Sharp SiC tips on ventral shell. SiC is an established field-emission material. Field enhancement at tips lowers required voltage to semiconductor-junction range. |
| Exhaust | H₂ + depleted gas swept out by flow. No accumulation. |
| H₂ in atmosphere | 15% H₂ is beneficial — hydrogen plasma etches weak bonds, improves film density. |

**Deposition rate (flow-through, conservative):**

| Parameter | Value |
|-----------|-------|
| Cavity gap | ~0.1 mm × ~1 mm |
| Flow velocity | ~1 m/s (restricted from lattice flow) |
| SiH₄ conversion efficiency | ~10% |
| SiCN deposition rate | ~480 ng/s |
| Film thickness over 1 mm² | ~0.15 μm/s |

| Repair depth | Time |
|-------------|------|
| 1 μm (surface restoration) | ~7 s |
| 10 μm (shallow crack) | ~70 s |
| 100 μm (deep structural repair) | ~12 min |

Practical repair in minutes. Rate scales with organism size, lattice flow speed (venturi amplification in pores), and conversion efficiency.

**Ventral shell geometry:** Concave shroud with inlet/outlet channels. Not a flat contact surface — a miniature wind tunnel with the field-emitter array at the throat. The organism's body converts the wind (the same force driving erosion) into the feedstock supply for repair. **[V2.5] Dual function: liquid excluder.** On the ammonia-streaming mound crest windward face, the concave shroud pressed against a strut displaces liquid ammonia from the repair zone, creating a de facto gas pocket at the work face. This is not a secondary adaptation — the crest environment is continuously wet, so the shroud geometry is ALWAYS functioning as both flow concentrator and liquid excluder simultaneously. This makes the ventral shroud a pre-adaptation for shallow submersion (mudflat root construction in 1–10 cm liquid NH₃) and ultimately the Gill-Healer's diving-bell gas pocket (see bible §5.4).

**Evolutionary pathway — chemical fill to flow-through arc-CVD:**

| Stage | Mechanism | Selection pressure |
|-------|-----------|-------------------|
| 1. Basal | Sessile organism secretes PCS at ventral contact. Lattice current ceramifies it. Chemical fill only. | Attachment weld chemistry repurposed for surface repair. No new morphology. |
| 2. Current increase | Organisms drawing more current for faster ceramification get micro-arcs at asperities (sharp shell features concentrating current). Atmospheric SiH₄ decomposes in arc zone, depositing trace SiCN. | Unintentional arcs. No new morphology — just higher current. |
| 3. Network reward | Arc-deposited SiCN measurably improves local lattice conductivity. Network detects cleaner signal → automatically increases local lattice potential. Organism gets more energy. | **The network's reward function IS the selection pressure.** Better lattice = better signal = more current to that region. Blindsight-compatible — no intention, no evaluation. |
| 4. Ventral differentiation | Selection for sharper ventral features → more productive arcs. Ventral surface differentiates: smooth Ti-enriched zones (energy extraction) and rough SiC field-emitter patches (repair arcs). | Morphological: two functional zones on one face. |
| 5. Flow channeling | Organisms whose body shape channels atmospheric flow across the arc zone get higher feedstock delivery → more productive deposition. Selection for concave ventral geometry with inlet/outlet gaps. | Behavioral: orient to flow. Morphological: shroud geometry replaces flat-seal geometry. |
| 6. Full flow-through arc-CVD | Charge-accumulate-discharge cycle. Dedicated field-emitter arrays. Optimized shroud geometry. Mobile Healers seek damage and deploy arc repair. | Full specialization. Chemical fill retained for routine maintenance. |

**Network reward mechanism:** The network doesn't decide to reward repair. It can't help it. Signal quality improves → local potential rises → organism on that site gets more energy. Real-time during repair: each successful arc pulse improves conductivity incrementally, network responds with incrementally more energy. Operant conditioning at the most primitive level — the Healer experiences increasing power return as it works. Sessile Healers get continuous reward for lifetime conductivity improvement. Mobile Healers get paid during each repair session.

**Mode selection:** Chemical fill for routine surface maintenance (most of the time, low energy, metabolically sourced PCS). Flow-through arc-CVD for structural damage detected via MEMS piezoelectric feedback (§10.3) from adjacent organisms or the Healer's own sensor array. Mobile Healers preferentially deploy arc-CVD — they seek out damage sites the network flags via energy-gradient modulation (§9.5). The wind that drives erosion also supplies the repair feedstock.

---

## 9. LOCOMOTION

### 9.1 The Lattice as 3D Scaffold

The tower is a porous SiC lung. Pore sizes are mm to low-cm — comparable to the organisms themselves. The middle kingdom does not walk ON a surface. It moves THROUGH a 3D scaffold of struts and pore spaces. Every "step" is a reach from one strut to another across a gap that may be the organism's own body length. This is arboreal locomotion, not terrestrial.

### 9.2 Lattice-Powered Locomotion

✓ **RESOLVED: Energy continuity is the primary locomotion constraint, not fall damage.**

Mobile fauna extract energy from the lattice through Schottky contacts at limb tips (§8.1). Every gripping contact with the lattice is also an energy-tapping contact. Losing contact means losing power — gel actuators go dead, the organism is inert until re-contact. Falling doesn't necessarily injure (the dense 8.2 kg/m³ atmosphere provides significant drag, especially for organisms with evolved high-drag geometry), but it causes **power blackout** and risks ejection from the tower.

Fall damage is size- and geometry-dependent. Terminal velocity scales as √r (for body radius r). Small middle kingdom organisms (mm scale, high surface-to-mass ratio) reach low terminal velocities and are protected by atmospheric drag. Large forms (cm scale) reach higher terminal velocities where impact on SiC lattice struts becomes structurally dangerous. Evolved body geometry (flat, spread, high-drag profiles) shifts the danger threshold upward — these organisms are shaped by eons of selection to maximize drag-to-weight, not spherical approximations.

Both pressures — energy continuity and impact survival — converge on the same solution: maintain continuous lattice contact during locomotion.

### 9.3 Locomotion Modes

**Strut-crawling (basal).** Segmented body with flexible polycarbosilane seams between rigid shell plates. Body conforms to strut surface; undulatory movement along the strut axis. No true limbs. Grip via body curvature and SiC-on-SiC friction. Limited to 1D paths along individual struts. Smallest mobile forms only (mm scale).

**Scaffold-climbing (derived, dominant).** Limbed forms that traverse the 3D lattice. SiC hook tips engage lattice pore edges by mechanical interlock. Alternating gait with guaranteed contact overlap — the new stance set engages before the old releases, ensuring continuous lattice contact for power. See §9.4 for limb count.

**Spring-loaded strike (predator specialization).** Gel actuators are too weak for fast movement (§4.3). Ambush predators use slow gel contraction to pre-stress a SiC composite spring element (Young's modulus ~300 GPa, elastic strain ~0.5%). A latch holds the stored energy; mechanical trigger releases. A 1 mm³ spring element stores ~3.75 mJ — sufficient to accelerate a 0.1 g appendage to ~8.7 m/s. At contact distances of a few mm, the strike arrives before aerodynamic braking matters. Predation is exclusively ambush, never pursuit. Prey defense is armor (Voronoi shell), not evasion.

### 9.4 Limb Count and Gait

✓ **RESOLVED: 8 limbs as base plan.**

The critical requirement is continuous lattice contact for energy. A 4+4 alternating gait (two quartets, each taking turns as stance/swing) guarantees overlap: the new quartet hooks in before the old releases. This prevents any zero-contact moment during locomotion.

6 limbs (alternating tripod) would work mechanically but creates a brief zero-overlap window during gait transitions — acceptable for small forms where power interruption is survivable, risky for larger forms where actuator restart delay could cause a fall.

Limb tips: SiC hooks sized to the local lattice pore geometry. **Hook-lattice mechanical compatibility is a speciation constraint** — organisms adapted to one tower lineage's pore geometry cannot efficiently traverse a tower with different lattice architecture. This is a third speciation axis alongside cognitive protocol and library addressing compatibility.

### 9.5 Network Control via Energy Gradients

The spine states: "Network manages middle kingdom via crude EM field modulation (tropism)."

If the network modulates local lattice potential — making some regions energy-rich, others energy-poor — mobile organisms naturally migrate toward higher-energy regions. No signal comprehension required. No cognitive interface. The organism follows the energy gradient the way a plant root follows moisture. The network herds the middle kingdom by reshaping its energy landscape.

For sessile organisms, the network shapes recruitment indirectly: energy-rich lattice zones produce faster larval bootstrapping and higher survival (§9.6). The network doesn't manage larvae — it manages the energy landscape that filters them.

### 9.6 Larval Bootstrapping

✓ **RESOLVED: Self-catalyzing bootstrap. Ventral-first shell growth. Pure r-selection.**

**Gametes:** 10–50 μm. Cross-linked polycarbosilane (PCS) coat loaded with dispersed SiC particles (particle-reinforced composite — abrasion-resistant). Recognition patches (cyclic trisilazane end-caps, Pool Genesis Hub §10) exposed through the coat for fusion. Minimal metal catalyst inventory: Ni (SiH₄ metabolism), Fe (ceramification). Broadcast into wind. No parental investment beyond the gamete package.

**Fusion:** On lattice surfaces or in-flight. Two gametes recognize at patches, fuse, merge library contents. Zygote: 20–100 μm, mostly cross-linked PCS surface with a soft seam at fusion site. First act: seal the fusion seam.

**Settlement:** Uncontrolled. Most zygotes die — wrong position, wrong orientation, grit-blasted, eaten, energy-starved. Survival is filtered by settlement physics:

| Position | Grit exposure | Energy access | Survival |
|----------|--------------|---------------|----------|
| Windward strut face, shallow | Maximum — direct grit impact at 370 Pa | High | ✗ Abraded before bootstrap completes |
| Windward strut face, deep interior | Reduced — lattice filters large grit | High | ⚠ Marginal |
| Leeward strut face, deep interior | Minimum — wake-sheltered + grit-filtered | Adequate | ✓ Favorable |
| Junction pocket / recirculation zone | Very low — sheltered dead zone | Low | ⚠ Slow bootstrap, long vulnerable window |

The lattice is a **grit filter**: large particles (high KE, dangerous) impact outer struts and never penetrate deep. Fine particles follow the flow deeper but have low KE per particle. Leeward strut faces deep in the lattice interior are the survivable settlement sites.

**The bootstrap sequence:**

1. Zygote adheres to leeward strut face via gel stickiness
2. Metabolizes atmospheric SiH₄ using gamete-provisioned Ni enzymes (abundant energy at this size in gas phase)
3. Thickens PCS coat. **Cannot ceramify yet** — no heat source (ceramification requires >400°C, only available via lattice resistive heating)
4. PCS accumulates at ventral surface (lattice contact zone)
5. Cross-linked PCS pad forms crude Schottky contact with N-doped SiC lattice → first current trickle
6. **Positive feedback:** current → resistive heating at interface → ceramification of PCS (nucleated on pre-loaded SiC particles) → better electrical contact → more current → accelerating ceramification
7. Ventral SiC plate forms, spreads laterally, curves around margins
8. Dorsal shell closes last
9. Limbs bud from growth margins (require shell for apodeme anchoring)
10. MEMS surface scales develop on completed dorsal shell

**Two-stage shell:**

| Stage | Shell | Energy source | Duration | Threat |
|-------|-------|---------------|----------|--------|
| Pre-contact | SiC-particle-loaded cross-linked PCS (tough, not hard) | Atmospheric SiH₄ only | Long (no positive feedback) | Grit abrasion, predation, dislodgement |
| Post-contact | SiC ceramifying ventral-first (positive feedback) | Lattice power + atmosphere | Short (self-accelerating) | Predation on unfinished dorsal surface; decreasing |

The pre-contact stage is the bottleneck. The post-contact positive feedback loop closes the shell rapidly once it starts. Most larval mortality occurs pre-contact.

**Reproductive strategy:** Pure r-selection. Mass gamete broadcast, no parental care, enormous mortality, statistical recruitment. Consistent with insect-scale ecology and the lattice energy landscape as the selective filter.

### 9.7 Lattice Flow Microhabitats

✓ **RESOLVED: The lattice creates a 3D mosaic of distinct microhabitats at the organism scale.**

Pore-scale Re ≈ 31,000 (8.2 kg/m³, ~10 m/s in 5 mm pores). Fully turbulent. Vortex shedding, wake separation, and recirculation are all present. Every strut has five flow zones; depth adds a sixth gradient.

**Flow zones:**

| Zone | Flow character | Grit | SiH₄ | Dynamic pressure |
|------|---------------|------|-------|-----------------|
| Windward face | Decelerating, stagnation | Maximum — direct impact | High — fresh supply | High |
| Leeward face | Separated wake, eddies | Low — particles overshoot | Moderate — wake depleted | Low |
| Pore throat | Accelerating, venturi, max velocity | Moderate — entrained | High — rapid refresh | Maximum — dislodgement risk |
| Junction pocket | Recirculating dead zone | Accumulation — grit settles | Low — poorly ventilated | Minimal |
| Deep interior | Stagnant, attenuated by upstream strut layers | None — filtered | Depleted — consumed | None |

**Depth gradient:** Outer lattice = high velocity, high grit, high SiH₄, high danger. Each strut layer filters grit and extracts SiH₄. Velocity and feedstock decay with depth. Living zone (~2–3 m) is the gas-exchange envelope. Below: no symbiote biology, but functionally active (H₂ chimney draft, structural webbing, amorph habitat).

**Ecological niche map:**

| Zone | Primary occupant | Reason |
|------|-----------------|--------|
| Windward face, outer | Healers (sessile + mobile) | Maximum erosion = maximum repair demand. Best arc-CVD feedstock flow. |
| Windward face, deep | Sessile Healers | Pre-filtered grit, longer lifespan, steady accretion. |
| Leeward face, outer | Mobile Miners, Guards | Sheltered transit/patrol. Miners staging for depth runs. Guards with sightlines into throats. |
| Leeward face, deep | Larvae (§9.6) | Nursery. Minimum grit, protected bootstrapping. |
| Pore throat | Transit corridor | Fast, dangerous. High SiH₄ refueling. Mobile Healers do arc-CVD here (max feedstock flow). Cross quickly. |
| Junction pocket | Guard ambush, Miner foraging | Grit accumulates (mineral-rich scraping). Low flow = easy ambush station-keeping. |
| Below living zone | Chimney conduit + amorph habitat | No symbiote biology. Active H₂ chimney (buoyancy-driven draft). Structural webbing. Amorph-excavated chambers and passages. Functionally important interior. |

**Aeolian tone — the lattice hums.**

Strouhal number for ~2 mm struts at ~10 m/s: f ≈ 0.2 × 10 / 0.002 ≈ **1 kHz.** Thousands of struts at varying diameters produce a complex acoustic spectrum. Above MEMS actuation bandwidth (~70 Hz) but passively detectable by the piezoelectric sensor arrays of organisms in direct contact with the struts.

**Acoustic vs EM health readout:** The Aeolian tone is a local phenomenon — middle kingdom organisms sense it through piezoelectric contact, not atmospheric propagation. For amorphs at distance, acoustic transmission through 9.5 m/s sustained wind is noisy, directional (upwind/downwind asymmetry), and unreliable. Tower health is far more accessible via EM: an amorph can contact the nearest surface root for a clean hardwired electrical readout of network signal quality. The lattice hum is ambient environmental texture for local fauna, not a long-range diagnostic channel.

**⚠ Note on "wind-song as art":** The lattice hum is physics, not art. Aeolian tones are an automatic structural health readout. Healers incidentally modify acoustic signatures through repair, but the network optimizes for signal propagation, not aesthetics — Blindsight has no aesthetic sense. Amorphs deliberately modifying tower structure for aesthetic purposes is unlikely: the network would suppress or penalize unauthorized lattice modification. Wind-song as art more plausibly involves free-standing amorph-grown acoustic sculptures (not tower modification) or rare Monk contemplative practice on dark-side towers. **Redirect: detailed resolution of wind-song art belongs in future Civilization module, not here.** This hub establishes only the physical basis (Aeolian tone, frequency, acoustic readout).

---

## 10. AERODYNAMIC SHELL

### 10.1 Wind Forces at Organism Scale

The tower lattice has persistent wind flowing through it (the tower is a lung; spine §Towers). At the terminator, free-stream dynamic pressure is 370 Pa (spine: 9.5 m/s in 8.2 kg/m³ air). Inside the lattice, pore channeling accelerates the flow (venturi effect); if the lattice is ~50% solid, local flow velocity roughly doubles and dynamic pressure quadruples to ~1,500 Pa.

Reynolds number for a 1 cm organism at 5 m/s in this atmosphere (viscosity ~1.3×10⁻⁵ Pa·s): Re ≈ 31,000. For 1 mm: Re ≈ 3,000. Both are well above Stokes flow — aerodynamic shaping produces meaningful forces across the entire middle kingdom size range.

### 10.2 Downforce Body Plan

✓ **RESOLVED: The dorsal shell is an inverted airfoil. Wind presses the organism onto the lattice.**

For a 1 cm organism (planform area ~0.5 cm², mass ~1 g) at 370 Pa free-stream:

| Downforce coefficient C_L | Downforce (N) | Body weight in 1.82g (N) | Downforce / weight |
|--------------------------|---------------|--------------------------|-------------------|
| 0.5 | 0.009 | 0.018 | 0.5× |
| 1.0 | 0.018 | 0.018 | 1.0× |
| 1.5 | 0.028 | 0.018 | 1.5× |

In venturi-amplified pore flow (~1,500 Pa), these values multiply by ~4. An organism with even modest aerodynamic shaping generates downforce **exceeding its own weight.** The wind nails it to the surface.

Predicted body plan: flat, wide, low-profile. Cambered dorsal surface with sharp trailing edge. Flat ventral face against lattice (electrical contact). Orientation locked into prevailing flow direction. All sessile organisms on a given lattice surface face the same way.

### 10.3 Dynamic Surface — The MEMS Shell

✓ **RESOLVED: Actuatable SiC scale arrays on the dorsal shell surface.**

The organism's aerodynamic environment changes (flow variation, locomotion orientation changes, defensive needs). A fixed airfoil shape cannot optimize for all conditions. The solution: arrays of small SiC scales/flaps rooted in gel pockets that penetrate the structural shell, electronically controlled in real time.

**Architecture:** Rigid SiC scale (sub-mm) on top. Electroactive silazane gel hinge at the base, within a pocket through the shell wall. Electronic nerve fiber controlling each cluster. Same principle as arthropod setae — rigid structures articulated by soft tissue at the base — but SiC and electronically controlled.

**Materials are already in the biology:**

| Component | Material | Source |
|-----------|----------|--------|
| Scale element | SiC CMC, partially ceramified | Carbosilane pathway (Chemistry Hub §6) |
| Hinge/actuator | Electroactive silazane gel | Same as limb gel actuators (§4.3) |
| Control | Electronic nerve fiber | Semiconductor signaling (spine §Biochemistry) |
| Feedback | Piezoelectric response of SiC | Each scale is simultaneously actuator and sensor |

**✓ Real-world validation:** Industrial MEMS are built from SiC, actuated by piezoelectric elements, electronically controlled, operating at μm-to-mm feature scale. Every material and mechanism is established technology.

### 10.4 Surface Configurations

| Configuration | Surface state | Purpose |
|--------------|---------------|---------|
| Maximum downforce | Scales flat, aligned to flow, trailing edge angled | Sessile/stationary. Wind presses organism onto lattice. |
| Maximum drag | All scales raised, surface roughness maximized | Falling/dislodged. Maximizes deceleration. Parachute mode. |
| Locomotion | Continuous real-time adjustment per body region | Maintains favorable aerodynamics during orientation changes on lattice. |
| Defensive | Scales raised and locked outward | Anti-predator. Hard-to-grip surface. Obstructs strike angle. |
| Reduced profile | Scales retracted tight, minimum frontal area | Storm survival or extreme flow events. |

### 10.5 Consequences

**Neural complexity driver.** Controlling hundreds of scale clusters in turbulent, variable lattice flow is a distributed real-time computation problem — harder than any predator-prey interaction. The neural hardware that the spine attributes to the armor/penetrator arms race may have originally evolved for **aerodynamic surface control**, with predator-prey tactics as a secondary beneficiary. Organisms that computed better surface configurations survived better in variable flow.

**Inadvertent signaling.** The shell is piezoelectric and semiconducting. Changing surface geometry changes the shell's EM signature. Every aerodynamic reconfiguration is visible to EM-sensitive organisms nearby. This is co-optable as a communication channel — threat displays, mating signals, species recognition — with zero additional hardware. The MEMS surface is simultaneously an aerodynamic control surface, armor, sensor array, and display organ.

**Sessile vs mobile trade-off.** Sessile organisms can maintain a fixed, aggressively optimized downforce profile. Their dorsal shell is a dedicated airfoil. Mobile organisms need shells that work in multiple orientations relative to flow — more symmetrical, less downforce-optimized. Sessility is aerodynamically rewarded; mobility pays an aerodynamic tax compensated by the ability to relocate to better energy/flow positions.

---

## 11. SHELL REPAIR AND STRUCTURAL AGING

### 11.1 Repair Mechanisms

✓ **RESOLVED: Three repair regimes, electronically directed.**

The organism detects damage via the MEMS piezoelectric sensor array (§10.3) and directs repair via electronic signals to the growth-face tissue. Response is faster and more spatially precise than Earth's chemical-cascade wound healing.

| Damage type | Detection | Repair mechanism | Rate-limiting step | Repair quality |
|------------|-----------|-----------------|-------------------|----------------|
| Surface abrasion (routine) | Not individually detected | Continuous inner-surface apposition replaces lost exterior. Conveyor-belt: new inside, old erodes outside. | Growth rate ≥ erosion rate | Full — new laminate identical to original |
| Crack/fracture (acute) | Piezoelectric signature change in MEMS array | Electronic signal → localized PCS secretion at growth face → crack infiltration → ceramification | PCS flow into crack + resistive heating | Near-original — ceramified fill, but not fiber-oriented laminate |
| Deep puncture (catastrophic) | Pressure loss + massive piezo signal | Gel coagulation at wound margin (rapid SiC particle stiffening) → PCS plug → ceramification seal | Gel stiffening (seconds), full seal (hours–days) | Inferior — plug, not laminate. Permanent weak point. |

**Hook tip maintenance (mobile forms):** Hooks grow by continuous apposition at the root. Tips wear by SiC-on-SiC contact. Functional geometry maintained as long as root growth rate ≥ tip wear rate.

### 11.2 Structural Aging

The sexual lineage does not die of metabolic senescence. It dies of **accumulated structural debt:**

- **Repair patches:** Each deep-puncture repair is a plug, not a laminate. Each plug is a permanent weak point. Repeated punctures in the same region create overlapping weak zones.
- **Hook wear (mobile forms):** If tip wear outpaces root growth, grip degrades → power blackouts → eventual ejection from lattice.
- **MEMS degradation:** Gel hinge fatigue, piezo response decline in scale elements. Loss of MEMS function → degraded aerodynamic control → exposure to grit, suboptimal downforce.
- **Erosion debt:** If grit abrasion outpaces inner-surface apposition at any point, shell thins locally. Predator strike on a thinned region penetrates.

Death is mechanical failure: a predator strike finds a weakened patch, or hook failure causes a fatal fall, or MEMS failure leads to aerodynamic dislodgement. Not biochemical aging — structural fatigue.

This parallels tower death: towers don't die of old age (lattice is mineral), but the living layer can fail to maintain the lattice. Same principle, different scale.

---

## 12. RESOLVED DECISIONS — SUMMARY

| Item | Status | Key result |
|------|--------|------------|
| Sexual lineage body plan | ✓ | Exoskeletal. No endoskeleton pathway available. |
| Shell material | ✓ | SiC fiber composite (CMC). 1,800–2,200 kg/m³. |
| Shell growth | ✓ | Continuous apposition from inner surface. No molting. |
| Joint material | ✓ | Amorphous metal silicide (TiSi₂, FeSi₂). Metallic glass. |
| Internal bracing | ✓ | Apodemes + SiC foam + fiber struts. Required above ~2 mm. Foam is node-reinforced PCS/SiC (partial ceramification at nodes only, Fe catalyst concentrated by Plateau border drainage, ~1/10th energy cost of full ceramification). Open-cell for gas permeation. |
| Gel actuation | ✓ | Electroactive polymer, ~2–7 kPa (central ~5 kPa), ~50× below Earth muscle. Voltage from series SiC junctions (~270V). Locomotion ~0.5–2 cm/s. Guard spring reload ~8 min. MEMS ~70 Hz/scale. Fast actions require springs. Think fast, act carefully. |
| Amorph structure | ✓ | Variable rigidity via redistributable SiC stock. No fixed plan. |
| Ceramification bottleneck | ✓ | Energy-limiting step. Organisms ceramify selectively. |
| Size ceiling (sexual) | ✓ | ~2 cm in 1.82g. Structural, not metabolic, limit. |
| Graphene | ✓ | Exotic specialization only. Never default structural material. |
| Tower-symbiote relationship | ✓ | Mutualism, not parasitism. Tower provides energy; middle kingdom provides immune defense, metal delivery, structural accretion, mineral trapping. |
| Three guilds | ✓ | Healers (surface maintenance + immune defense + **dead-clearing**, sessile and mobile), Miners (metal delivery, mobile), Guards (population quality control, mobile). [NEW IN V2.4] Healer sub-caste: garbage collectors clear dead organisms from lattice to maintain airflow and conductivity. Dead material pushed to exterior → enters windstream → continuous downwind plume of dead tower fauna from every tower. |
| Healer repair mechanisms | ✓ | Two modes: chemical fill (PCS secretion + contact-weld ceramification, routine) and flow-through arc-CVD (concave ventral shroud channels wind over field-emitter array, atmospheric SiH₄/CH₄ feedstock, deposits SiCN at ~0.15 μm/s, tower-powered). NOT sealed cavity — feedstock depletion kills sealed model. Wind supplies feedstock flow. Deposit is SiCN (nitrogen from NH₃), structurally adequate. Gravity-independent (thermal KE >> gravitational PE by 7 orders). Network conductivity-reward IS the selection pressure. |
| Mining mechanism | ✓ | Miners transport metals exterior → living layer. Chelation extraction at living layer interface. Energy gradient drives cycle. |
| Chelation dual function | ✓ | Immune weapon (ancestral) → mutualistic toll (derived). Same chemistry, gated by molecular authentication. |
| Chelation authentication | ✓ | Static ventral metallosilazane badge, not cryptographic. Inherited via library. Read by chelation effector binding specificity. Fourth speciation axis. Anti-forgery: pattern complexity, lethal default, network-side rotation, delivery-contingent reward. |
| Miner storage & population | ✓ | 5–10% body mass as surplus metallosilazane cargo. ~10M miners per mature tower (~400M m² living layer). Negligible fraction of total population and energy budget. Delivery distributed along depth transects. |
| Tower attachment | ✓ | Sessile: ceramification weld. Mobile: mechanical hook grip. |
| Electrical interface | ✓ | Sessile: ventral Ti-enriched ohmic contact. Mobile: claw-tip Schottky contact. |
| Locomotion substrate | ✓ | 3D scaffold traversal, not surface walking. Arboreal, not terrestrial. |
| Energy continuity | ✓ | Primary locomotion constraint. Every contact = energy tap. Loss of contact = blackout. |
| Limb count | ✓ | 8 limbs, 4+4 alternating gait. Continuous contact overlap for power. |
| Hook-lattice compatibility | ✓ | Third speciation axis: hook geometry must match lattice pore geometry. |
| Predation mode | ✓ | Ambush only (spring-loaded strike). No pursuit. Armor vs. puncture arms race. |
| Aerodynamic downforce | ✓ | Dorsal shell = inverted airfoil. Wind-generated downforce can exceed body weight. |
| Dynamic surface | ✓ | MEMS-like actuatable SiC scale arrays. Real-time aerodynamic reconfiguration. |
| Network tropism mechanism | ✓ | Energy gradient modulation herds mobile fauna. Settlement control for sessile fauna. Optimizes mining delivery pipeline. |
| Neural complexity origin | ⚠ | Aerodynamic surface control as primary driver (proposed). Predator-prey secondary. |
| Larval bootstrapping | ✓ | SiC-particle-loaded PCS gamete coat. Broadcast, no parental care. Leeward deep-interior settlement. Self-catalyzing ventral-first ceramification via lattice current positive feedback. r-selected. |
| Larval grit survival | ✓ | Leeward strut faces + lattice grit filtering + particle-reinforced PCS coat. No new biology needed. |
| Shell repair | ✓ | Three regimes: conveyor-belt apposition (abrasion), crack infiltration (fracture), gel plug (puncture). Electronically directed via MEMS sensor array. |
| Structural aging | ✓ | Death by accumulated structural debt (repair patches, hook wear, MEMS fatigue, erosion), not biochemical senescence. Parallels tower death. |
| Lattice flow microhabitats | ✓ | 5 zones per strut + depth gradient. Re ≈ 31,000, fully turbulent. Ecological niche map: Healers on windward, larvae on deep leeward, Guards in junction pockets, throats as transit corridors. Aeolian tone ~1 kHz (local ambient, not long-range diagnostic — EM via surface roots is the primary health readout). |

---

## 13. OPEN QUESTIONS

### Resolved This Session

| Question | Resolution |
|----------|-----------|
| Locomotion modes | ✓ Three modes: strut-crawling (basal), scaffold-climbing (dominant, 8-limbed), spring-loaded strike (predator). Lattice-powered via contact energy extraction. |
| Sensory integration with shell | ✓ Subsumed by MEMS shell: every SiC scale is a piezoelectric sensor. Whole-body mechanosensation is inherent. Also serves as inadvertent EM display. |
| Larval/juvenile shell bootstrapping | ✓ SiC-particle-loaded PCS gamete coat → leeward deep-interior settlement → ventral Schottky contact → positive feedback ceramification → shell closure. r-selected broadcast, no parental care. Grit survival via leeward sheltering + lattice grit filtering + particle-reinforced coat. |
| Shell repair mechanism | ✓ Three regimes: conveyor-belt (abrasion), crack infiltration (fracture), gel plug (puncture). Electronically directed. Structural aging = accumulated repair debt, not biochemical senescence. |
| Tower-symbiote relationship | ✓ Mutualism: immune defense (grazers), catalytic metal delivery (miners), structural accretion (sessile). Chelation dual function: immune weapon (ancestral) → mutualistic toll (derived), gated by molecular authentication. |
| Chelation authentication chemistry | ✓ Static ventral metallosilazane badge (MHC analog, not cryptographic). Inherited via library. Read by chelation effector binding specificity. Fourth speciation axis. Anti-forgery: pattern complexity, lethal default, network-side rotation, delivery-contingent reward. |
| SiC foam manufacture | ✓ | Node-reinforced polymer foam. H₂-blown PCS, Fe catalyst concentrates at Plateau borders by physics, lattice current ceramifies nodes only (~10–15% of mass). Open-cell for gas permeation. Density 200–600 kg/m³, tunable. ~1/10th energy cost of full ceramification. |
| Gel actuator force budget | ✓ | ~2–7 kPa (central ~5 kPa). Maxwell stress + electrostriction of polar Si-N bonds. Voltage from series SiC junctions (~270V over 50 μm). Locomotion ~0.5–2 cm/s. Guard spring reload ~8 min. MEMS ~70 Hz. Adequate for ecology (armor not evasion; ambush not pursuit; electronic perception compensates for slow movement). |
| Lattice flow characterization | ✓ | 5 flow zones per strut (windward, leeward, throat, junction pocket, deep interior) + depth gradient. Re ≈ 31,000 — fully turbulent. Niche map: Healers on windward faces, larvae on deep leeward, Guards in junction pockets, throats as transit corridors. Aeolian tone ~1 kHz — lattice hums, readable as structural health acoustic. |

### Open

All original open questions resolved. No remaining items.

---

*The shell found wind and began to fly.*
