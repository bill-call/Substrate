# SUBSTRATE — SILICON CHEMISTRY HUB

**v2.4 — February 2026**

Hard chemistry only. Every claim grounded or flagged. Load with bible + spine.

This document audits every chemical species, reaction, and mechanism in the Substrate worldbuilding against real organosilicon chemistry. Status codes: **✓ SOUND** (real chemistry, defensible), **⚠ NEEDS REVISION** (fixable problem), **✗ PROBLEM** (breaks established chemistry). Proposed fixes included.

---

## 1. THE OXYGEN PROBLEM — HIGHEST PRIORITY CORRECTION

**⚠ NEEDS REVISION: The bible specifies "silicone oil (polydimethylsiloxane)" as the biological solvent/matrix. PDMS requires Si-O-Si bonds. There is no plausible oxygen source in a reducing H₂/CH₄/NH₃ atmosphere.**

Siloxane (Si-O-Si) is an oxygen-bridged polymer. Oxygen is a trace oxidizer on this world — the very thing that causes petrification. A biology built on siloxane bonds would be a biology built on the substance that kills it.

### The Fix: Silazane, Not Siloxane

The correct solvent for this world is **polysilazane oil** — the nitrogen analog of silicone oil.

| Property | Siloxane (PDMS) | Silazane analog |
|---|---|---|
| Backbone | —Si-O-Si-O— | —Si-NH-Si-NH— |
| Bridge atom | Oxygen | Nitrogen (via NH) |
| Feedstock atoms | Si, O, C, H | Si, N, C, H |
| Available on planet? | O is trace/harmful | N is 12.5% atmosphere (NH₃) + 55% (N₂) |
| Isoelectronic? | Yes — silazanes and siloxanes are isoelectronic pairs |
| Oil properties | Flexible, low viscosity, hydrophobic, wide liquid range | Same: flexible, variable viscosity, tunable properties |
| Thermal stability | Good to ~300°C | Good to ~300°C; superior above 400°C |

Polysilazanes are real industrial polymers (Durazane® product line, used in ceramic precursor coatings, high-temperature applications). They are synthesized from chlorosilanes + ammonia — or, in biological context, from **silane + ammonia**, both atmospheric feedstocks.

**Critical bonus:** Polysilazanes decompose on contact with water. H₂O attacks the Si-N bond, cleaving it and forming Si-O-Si (siloxane) + NH₃. This is literal, published chemistry. The pathology writes itself:

> Trace water vapor attacks Si-NH-Si bonds → converts to Si-O-Si (siloxane) → further oxidation → SiO₂ (glass). Petrification is the progressive replacement of nitrogen with oxygen in the biological matrix.

This makes petrification *chemically specific*: not vague "oxidation" but a known reaction pathway (hydrolysis of silazane to siloxane, then condensation to silica). The organism's living matrix is nitrogen-bridged; its corpse is oxygen-bridged. The dead literally become a different material.

### Proposed Terminology

| Bible term | Revised term | Notes |
|---|---|---|
| Silicone oil | **Silazane oil** or **polysilazane matrix** | Chemically correct for reducing, N-rich atmosphere |
| PDMS | **Polymethylsilazane (PMSz)** | Direct nitrogen analog of PDMS |
| Silane/siloxane polymer | **Silane/silazane polymer** | One-letter fix throughout |
| Siloxane | Reserve for *pathological* state | Siloxane = partially petrified tissue |

### Supporting Chemistry

Silazane synthesis from atmospheric feedstocks:

```
SiH₄ + NH₃ → H₃Si-NH₂ + H₂              (aminosilane formation)
2 H₃Si-NH₂ → H₃Si-NH-SiH₃ + NH₃         (condensation to disilazane)
n H₃Si-NH-SiH₃ → [-SiH₂-NH-]n + n SiH₄  (polymerization)
```

With methyl substituents (from atmospheric CH₄ incorporation):

```
CH₃SiH₃ + NH₃ → CH₃SiH₂-NH₂ + H₂
polymerization → [-Si(CH₃)H-NH-]n          (polymethylsilazane oil)
```

Petrification pathway:

```
-Si-NH-Si- + H₂O → -Si-OH + H₂N-Si-       (hydrolysis — first lesion)
-Si-OH + HO-Si- → -Si-O-Si- + H₂O          (condensation to siloxane)
-Si-O-Si- + O → -SiO₂-                       (full oxidation to glass)
```

Each stage is progressively less reversible. Early-stage hydrolysis might be repairable (re-aminate the broken bond). Late-stage silica formation is permanent. This gives petrification the chronic, progressive character described in the bible.

---

## 2. CHEMICAL SPECIES INVENTORY

Every named or implied chemical in the worldbuilding, grounded to real chemistry.

### 2.1 Atmospheric Species

| Species | Formula | Role | Real? | Notes |
|---|---|---|---|---|
| Molecular nitrogen | N₂ | Dominant atmosphere (55%) | ✓ SOUND | Primary buffer gas. Secondary nitrogen source. Dominates mean molecular mass (~20.5 g/mol). |
| Molecular hydrogen | H₂ | 15% atmosphere | ✓ SOUND | Retained by 18.6 km/s escape velocity. Metabolically inert waste product (no electron acceptor). |
| Ammonia | NH₃ | 12.5% atmosphere, nitrogen source, liquid in basins | ✓ SOUND | Liquid range at 8 bar: 196–293K. Stable and liquid at terminator 240K. Universal solvent. |
| Methane | CH₄ | 10% atmosphere, carbon source | ✓ SOUND | Stable in reducing conditions. Feedstock for carbosilane pathway. |
| Silane | SiH₄ | 0.3% atmosphere, primary energy feedstock | ✓ SOUND | Thermodynamically unstable (ΔHf = +34.3 kJ/mol). Stable kinetically in absence of O₂ and ignition sources. Decomposes to Si + 2H₂ (exothermic). The biological "oxygen" of this world. |

**✓ SOUND:** The atmosphere is thermodynamically self-consistent. In a reducing environment dominated by H₂, CH₄/NH₃/SiH₄ are the stable (or metastable) forms of C, N, and Si. No free oxygen is possible — it would be immediately consumed by H₂. This is Jupiter's atmosphere with added SiH₄ from volcanic outgassing.

### 2.2 Biological Polymers

| Species | Structure | Role | Status | Notes |
|---|---|---|---|---|
| Polysilane | —(SiR₂)n— | Backbone polymer, information storage | ✓ SOUND | Real polymers. Si-Si σ-bonds. UV-sensitive (σ→σ* transition at ~300-350 nm) but star's UV output <1% solar, so stable. Substituent R can vary: H, CH₃, longer chains. |
| Polysilazane oil | —(R₂Si-NH)n— | Biological solvent/matrix | ⚠ REVISED | Replaces siloxane (see §1). Real polymer class. Flexible, variable viscosity, tunable by substituents. |
| Polycarbosilane | —(R₂Si-CH₂)n— | Structural fiber precursor | ✓ SOUND | Real polymer. Industrial precursor to SiC fiber (Yajima process). Four-stage pathway in bible is accurate. |
| Silicon carbide (SiC) | SiC (various polytypes) | Structural material, armor, lattice mineral | ✓ SOUND | Mohs hardness 9-9.5. Semiconductor (bandgap 2.3-3.3 eV depending on polytype). Can be doped conducting. Chemically inert. |
| Methylsilanes | CH₃SiH₃, (CH₃)₂SiH₂, etc. | Carbosilane pathway intermediates | ✓ SOUND | Real compounds. First step of biological CH₄ + SiH₄ processing. |

### 2.3 Inorganic Species

| Species | Formula | Role | Status | Notes |
|---|---|---|---|---|
| Amorphous silicon | Si (a-Si) | Deposited metabolic product | ✓ SOUND | Product of SiH₄ decomposition. Semiconductor. Photovoltaic. |
| Silicon nitride | Si₃N₄ | Possible structural/insulating material | Implied | Pyrolysis of polysilazane under N₂ produces Si₃N₄. Likely present in tower lattice. |
| Silicon dioxide (silica) | SiO₂ | Petrification end-state | ✓ SOUND | Glass. Inert. The "fossil" material. |
| Silicon tetrafluoride | SiF₄ | Fluorine weapon product | ✓ SOUND | Gas (bp -86°C). Product of F₂ + Si-Si attack. This reaction is ferociously exothermic. Real semiconductor etch chemistry. |
| Metal silicides | FeSi₂, NiSi, TiSi₂ etc. | Volcanic mineral deposits, possible catalysts | ✓ SOUND | Stable in reducing conditions. Many are metallic conductors. |
| Hydrogen fluoride | HF | Fluorine-hydrogen flame product | ✓ SOUND | F₂ + H₂ → 2HF, ΔH = -542 kJ/mol. Among the most exothermic reactions known. Corrosive to Si. |
| Uranyl-ammine complexes | [UO₂(NH₃)n]²⁺ | Fissile material mobilization | ✓ SOUND | Uranium forms stable ammine complexes in liquid ammonia. Analogous to aqueous uranyl chemistry. |

---

## 3. ENERGY METABOLISM — SPECIFIC REACTIONS

The bible says "SiH₄ processing" without specifying the reaction. Here are the actual metabolic equations.

### 3.1 Primary Metabolism: Silane Respiration

```
SiH₄(g) → Si(s, deposited) + 2H₂(g)
ΔH ≈ -34.3 kJ/mol
```

**✓ SOUND.** Silane has a positive heat of formation (+34.3 kJ/mol), meaning it is thermodynamically unstable relative to silicon + hydrogen. Decomposition is spontaneous (ΔG < 0 at all relevant temperatures). On Earth, SiH₄ doesn't decompose at room temperature because the kinetic barrier is high — it needs a catalyst or >400°C. Biology provides the catalyst.

This is the foundational metabolic equation: **silane in, hydrogen out, silicon deposited.** Directly analogous to our oxygen respiration (O₂ in, CO₂ out, energy extracted). The deposited silicon is both structural material and metabolic waste. The organism literally builds itself from exhaled breath.

Energy yield: 34.3 kJ/mol is modest (glucose combustion: 2,803 kJ/mol). But silane is processed directly as a gas — no digestion, no complex catabolism. And organisms supplement with photovoltaic and piezoelectric energy. The low chemical energy per molecule is offset by continuous atmospheric intake through an enormous surface area (the lattice is a lung).

### 3.2 Carbosilane Metabolism: Combined C + Si Processing

```
SiH₄(g) + CH₄(g) → SiC(s) + 4H₂(g)
ΔH ≈ -33 kJ/mol
```

(Calculated from: ΔHf[SiC] = -73.2, ΔHf[SiH₄] = +34.3, ΔHf[CH₄] = -74.6 kJ/mol)

**✓ SOUND.** Exothermic. Produces SiC directly from atmospheric gases. This is the net equation for the carbosilane pathway; the actual biology proceeds through four intermediate stages (see §6).

### 3.3 Silazane Biosynthesis

```
SiH₄(g) + NH₃(g) → SiH₂(NH)(s/l) + 2H₂(g)
```

Produces the monomeric unit of silazane matrix. Exothermic (Si-N bond energy ~470 kJ/mol compensates Si-H and N-H bond breaking). The matrix the organism's body is made from.

### 3.4 Photovoltaic Energy

```
photon (850 nm, ~1.46 eV) + Si → electron-hole pair
```

Silicon's bandgap: 1.12 eV. Star's peak emission: ~850 nm (~1.46 eV). The photons are above the bandgap — every photon at or below ~1107 nm can be absorbed. The 850 nm peak is not a perfect match (optimal would be GaAs at 1.42 eV), but silicon absorbs it efficiently. The mismatch actually makes the system more *realistic* — it's "good enough," not suspiciously perfect.

**Note on bandgap claims in the bible:** The bible says "Silicon's bandgap (1.1 eV) matches star's peak emission (~850 nm)." This is slightly misleading. 1.1 eV corresponds to ~1107 nm, not 850 nm. What's true is that silicon *absorbs* 850 nm photons (they're above the bandgap), and the star's emission overlaps heavily with silicon's absorption range. The star doesn't need to peak *at* the bandgap — it needs to emit *above* it, which it does abundantly. Suggested rewording: "Silicon's bandgap (1.1 eV) lies within the star's peak emission range (~850 nm), enabling efficient photovoltaic absorption."

### 3.5 Deep-Rock Chemolithotrophy

```
H₂(g) + mineral-bound Si → reduced Si + H₂O or other waste
```

**⚠ NEEDS SPECIFICATION.** The bible says "geothermally mobilized hydrogen and mineral-bound silicon." The most likely specific reaction:

```
4H₂(g) + SiO₂(s) → Si(s) + 2H₂O(g) + 2H₂(g)     [too endothermic at low T]
```

Actually this doesn't work at biological temperatures. More plausible:

```
H₂(g) + metal silicate minerals → metal silicides + H₂O
```

Or better yet, the deep-rock organisms process **geothermally heated SiH₄** that percolates through fractures from deeper magmatic sources. Silane can form in deep reducing magmatic conditions (Si + 2H₂ → SiH₄ at high T/P, reversed at surface conditions). The deep-rock biosphere's energy source is the same SiH₄ → Si + 2H₂ reaction as surface life, just from geothermal silane rather than atmospheric silane.

**Proposed resolution:** Deep-rock chemolithotrophs metabolize geothermally generated silane (SiH₄) that percolates through fracture networks, supplemented by H₂ as electron donor for reducing metal-silicate minerals to conductive metal silicides. The mineral they deposit is a mix of amorphous silicon, silicon carbide (where carbon from deep CH₄ is available), and metal silicides — all conductive. This is consistent with the bible's statement that they "deposit conductive mineral as baseline metabolic waste."

---

## 4. THE CONDUCTIVE MINERAL — WHAT IS THE LATTICE MADE OF?

The bible refers to "conductive mineral" deposited by tower symbiotes and deep-rock organisms without specifying composition. This needs resolving because it determines the entire electrical ecology.

### Proposed Answer: Nitrogen-Doped Silicon Carbide

**SiC doped with nitrogen is a well-characterized semiconductor.** Nitrogen is the standard n-type dopant for SiC in real semiconductor industry. It substitutes at carbon sites in the SiC lattice.

This is the only answer that uses all available atmospheric feedstocks:

- Silicon from SiH₄ (0.3% atmosphere)
- Carbon from CH₄ (10% atmosphere)
- Nitrogen dopant from NH₃ (12.5% atmosphere)

Conductivity of N-doped SiC is tunable over many orders of magnitude depending on dopant concentration. At heavy doping levels, it approaches metallic conductivity. At light doping, it's semiconducting.

**This solves three problems at once:**

1. **What is the lattice mineral?** Nitrogen-doped SiC.
2. **Why does dead lattice still conduct?** Conductivity is a physical property of the doped mineral, not biologically maintained. (Already stated in bible — now chemically grounded.)
3. **Why do different colonies have different "mineral microstructure"?** Different metabolic quirks → different dopant concentrations, different SiC polytypes (3C, 4H, 6H — real polymorphs with different electronic properties), different trace metal inclusions. Signals propagate differently through different microstructure.

### Tower Lattice Composition (proposed)

| Component | Source | Role |
|---|---|---|
| SiC matrix (bulk) | SiH₄ + CH₄ metabolized by symbiotes | Structural + semiconductor base |
| Nitrogen dopant | NH₃ incorporated during growth | n-type conductivity for signal propagation |
| Boron dopant (local) | Volcanic mineral incorporation | p-type regions → p-n junctions where biology needs diode behavior |
| Amorphous Si regions | SiH₄ decomposition without carbon | Photovoltaic surface layer |
| Metal silicide traces | Fe, Ni from volcanic minerals | Metallic conductors at critical junctions |

The lattice is not a single material — it's a biological composite, grown layer by layer, with composition varying by region and function. The symbiotes control what they deposit, and the dopant profile determines the electrical behavior. A tower is a kilometer-tall semiconductor device grown from atmospheric gases by a living film.

---

## 5. SEMICONDUCTOR NEUROLOGY — MECHANISMS

The bible claims "electronic, not electrochemical" neural signaling via "semiconductor junctions, doped regions." This is the most speculative chemistry in the worldbuilding. Here's how to ground it.

### 5.1 Biological Doping

On Earth, organisms exercise precise control over mineral deposition: magnetotactic bacteria produce single-domain magnetite crystals with controlled size and orientation. Foraminifera build calcite shells with species-specific geometry. Bone osteoblasts deposit hydroxyapatite with nm-precision.

An amorph organism with a silicon-chemistry metabolism would deposit silicon-based semiconductors. The critical question is whether it can control dopant incorporation.

**Nitrogen (n-type):** Abundant. Present in the solvent matrix (silazane) and atmosphere (NH₃, N₂). Controlling the *exclusion* of nitrogen from a deposit would be harder than including it. N-doped silicon is the default product of any silicon deposition in this atmosphere.

**Boron (p-type):** Present in volcanic minerals (boron concentrates in late-stage melts alongside uranium and thorium). Must be actively incorporated. Biology would need boron-transport proteins (or their silicon-chemistry equivalent) to create p-type regions.

**Result:** n-type silicon/SiC is the default tissue. p-type requires active effort. A p-n junction is created wherever the organism switches from passive (nitrogen-contaminated) deposition to active boron incorporation. This is biologically plausible — it requires one controlled variable, not many.

### 5.2 Signal Propagation

In a semiconductor p-n junction, current flows easily in one direction (forward bias) and is blocked in reverse. This gives **signal directionality** — a biological diode.

A chain of p-n junctions with variable doping creates a **transistor-like amplification cascade.** The organism grows circuits the way we grow neurons — as developmental structures, not engineered artifacts.

Signal speed: Electron drift velocity in doped SiC at moderate fields (~10 V/cm) is on the order of 10⁴-10⁵ cm/s = 0.1-1 km/s. At higher fields, saturation velocity in SiC is ~2 × 10⁷ cm/s = 200 km/s. For comparison, Earth myelinated nerve conduction: ~0.1 km/s. **Silicon neural signaling is 100-2000x faster than electrochemical neurons.** The bible's claim of "electronic speed" cognition is sound.

### 5.3 What "Cognition" Looks Like

The amorph brain is not a von Neumann computer. It's a massively parallel, reconfigurable analog semiconductor network — closer to a neuromorphic chip than a digital processor. Each "neuron" is a doped region with threshold behavior. Connections are physical semiconductor pathways that can be grown, pruned, or modified by changing local chemistry. The organism literally rewires its own hardware by depositing or etching material.

"Native arithmetic/Bayesian reasoning" follows: analog semiconductor circuits naturally perform multiplication, integration, and threshold operations. Bayesian inference is a natural operation for a system that weights evidence through variable conductances. This is not anthropomorphized — it's what analog circuits do.

---

## 6. THE CARBOSILANE PATHWAY — STEP BY STEP

The bible describes four stages: "methylsilanes → polycarbosilanes → oriented fibers → catalytic conversion to SiC ceramic." Here's the specific chemistry.

### Stage 1: Methylsilane Synthesis

```
SiH₄ + CH₄ → CH₃SiH₃ + H₂     (methylsilane)
ΔH ≈ -15 to -25 kJ/mol (estimated from bond energies)
```

**Real chemistry.** Industrial route uses chlorosilanes (Müller-Rochow process), but direct hydrosilylation of methane with silane is possible with catalysis. On this planet, the catalyst is biological — likely a transition-metal-centered enzyme (see §8). Lightning also produces methylsilanes directly via plasma-enhanced CVD (stated in bible, confirmed by real plasma chemistry literature).

Further methylation possible:

```
CH₃SiH₃ + CH₄ → (CH₃)₂SiH₂ + H₂     (dimethylsilane)
```

### Stage 2: Polycarbosilane Formation

```
n CH₃SiH₃ → [-SiH(CH₃)-CH₂-]n + n H₂     (polycarbosilane)
```

**Real chemistry.** The Yajima process (1975) thermally rearranges polydimethylsilane to polycarbosilane at ~450°C. Biological route: enzymatic catalysis at lower temperature. The Si-C backbone forms through elimination of H₂ from adjacent Si-H and C-H groups, catalyzed by transition metal centers.

### Stage 3: Fiber Spinning

Polycarbosilane is extruded as oriented fibers. The organism controls fiber diameter, orientation, and cross-linking density. This is analogous to spider silk extrusion — a liquid polymer pulled through a biological spinneret, with properties determined by draw rate and chemistry.

**✓ SOUND.** Industrial SiC fibers (Nicalon, Tyranno) are made exactly this way: spin polycarbosilane fibers, then pyrolyze.

### Stage 4: Ceramification

```
[-SiH(CH₃)-CH₂-]n → SiC + volatile byproducts (H₂, CH₄)
```

At >800°C in industry. Biologically: the organism uses localized heating (electrical resistance heating through the lattice, or exothermic silane decomposition) to ceramify fibers in place. The result is β-SiC (cubic polytype) fibers in a living polycarbosilane/silazane matrix.

**The 40% lighter claim:** Bulk SiC density ~3,210 kg/m³. SiC fiber composite with polymer matrix: ~1,800-2,200 kg/m³. Ratio: 0.56-0.69. The bible's "40% lighter" claim is consistent with real fiber composite densities.

### The Carbosilane Revolution (Cultural Implications)

The revolution is not just stronger material — it's **self-manufactured** material. Before carbosilane, amorphs collect SiC from grazers (shell economy). After carbosilane, they grow it from air. The transition is from mining to agriculture, from scavenging to biosynthesis. The shell economy collapses because the currency can now be printed by anyone's body.

---

## 7. FLUORINE CHEMISTRY — DETAILED

The bible's fluorine ecology is some of the most chemically sound worldbuilding in the entire project.

### 7.1 The Attack Reaction

```
Si-Si + F₂ → SiF₂ + SiF₂ → SiF₄(g)
ΔH ≈ -850 to -1000 kJ/mol (per Si-Si bond broken — estimated)
```

More precisely, fluorine attacks silicon through radical chain mechanism:

```
F₂ → 2F•                           (homolysis)
F• + -Si-Si- → -Si• + -SiF-        (chain propagation)
-SiF- + F₂ → -SiF₂ + F•           (continued fluorination)
-SiF₂- → SiF₄(g)                  (volatilization — the wound hisses)
```

**✓ SOUND. This is industrial silicon etching chemistry.** Fluorine-based plasma etching is the primary method of patterning silicon in semiconductor fabrication. The chemistry is well-characterized and *exactly* as violent as the bible describes. SiF₄ is a gas (bp -86°C) — affected tissue literally evaporates.

The bible's description — "the wound hisses as solid flesh converts to gas" — is *precisely* what happens. This is not poetic license; it's stoichiometry.

### 7.2 Fluorine-Hydrogen Flame

```
F₂ + H₂ → 2HF
ΔH = -542 kJ/mol
```

**✓ SOUND.** One of the most exothermic reactions in chemistry. For comparison, H₂ + ½O₂ → H₂O is only -286 kJ/mol. The fluorine-hydrogen flame is almost twice as energetic as hydrogen-oxygen combustion.

HF is also a silicon etchant:

```
4HF + SiO₂ → SiF₄ + 2H₂O        (etches glass/silica)
6HF + Si → H₂SiF₆ + 2H₂          (etches silicon)
```

So the combustion product is *also* corrosive to silicon life. The flame, the product gas, everything about fluorine-hydrogen reaction is lethal. The bible's characterization as "their nuclear-weapon analog" is chemically justified.

### 7.3 Biological Fluorine Handling

How do organisms store and deploy F₂ without destroying themselves?

**Proposed mechanism:** Organisms store fluorine as metal fluorides (CaF₂, AlF₃) in ceramic-lined vesicles. The ceramic lining is SiC — which is resistant to fluorine at low temperatures (SiC etching requires plasma conditions or >400°C with F₂). Deployment: rapid enzymatic liberation of F₂ from fluoride salts within a sacrificial ceramic structure (the "thorn" that breaks off and embeds).

The thorn-flora's thorns are SiC shells containing packed CaF₂/fluoride mineral, with a biological trigger that initiates F₂ release upon mechanical fracture and contact with target tissue. Once the thorn breaks inside prey, fluoride meets catalyst → F₂ generated locally → immediate Si volatilization.

This is analogous to cnidocyst (stinging cell) chemistry in cnidarians — a pressurized payload in a structural shell, deployed by mechanical trigger.

---

## 8. CATALYSIS AND ENZYMOLOGY

Every biological reaction in the worldbuilding needs a catalyst. On Earth, metalloenzymes do most of the heavy lifting. What catalyzes silicon biochemistry?

### 8.1 Available Transition Metals

From the bible: native metals in reducing atmosphere. Day-side volcanic provinces concentrate metal deposits.

| Metal | Role in Earth biochemistry | Proposed silicon-biochemistry role |
|---|---|---|
| Iron | O₂ transport, electron transfer (cytochromes) | Electron transfer, Si-H bond activation, SiC formation catalyst |
| Nickel | Hydrogenase, urease | H₂ metabolism, silane activation (Ni is a known hydrosilylation catalyst) |
| Titanium | Rare in Earth biology | Si-C bond formation (Ti catalyzes Ziegler-Natta polymerization and hydrosilylation) |
| Platinum group | Very rare on Earth | Hydrosilylation catalysis (Pt is the standard industrial catalyst: Karstedt's, Speier's) |
| Cobalt | B₁₂ vitamin | Radical reactions, C-Si bond formation |

**Key insight:** Hydrosilylation (Si-H + C=C → Si-C) is catalyzed by Pt, Pd, Ni, Fe, Co complexes. This is the core reaction of silicon-carbon bond formation. Biological enzymes with these metal centers could catalyze every step of the carbosilane pathway at ambient temperature.

### 8.2 The "Enzyme" Concept

Silicon-world enzymes are not proteins. They are organosilicon frameworks (polysilazane or polycarbosilane scaffolds) with transition metal active sites coordinated by nitrogen donor atoms from the silazane backbone. 

This is not speculative handwaving — metal-polysilazane complexes are real, studied materials. Polysilazanes coordinate metals through their nitrogen atoms, forming catalytic sites.

The molecular library stores "recipes" — each recipe is the sequence of monomers and metal-incorporation instructions needed to fold a catalytic framework with a specific active site geometry. The library IS the enzyme specification.

---

## 9. LIGHTNING CHEMISTRY — PLASMA CVD PRODUCTS

The bible claims lightning in H₂/CH₄/SiH₄/NH₃ produces "methylsilanes, carbosilanes, complex organosilicon compounds."

**✓ SOUND.** Plasma-enhanced chemical vapor deposition (PECVD) in silane/methane/ammonia/hydrogen mixtures is a real, well-studied industrial process. Known products include:

- Amorphous silicon (a-Si) films
- Silicon carbide (SiC) films
- Silicon nitride (Si₃N₄) films
- Silicon carbonitride (SiCN) films
- Methylsilanes (CH₃SiH₃, (CH₃)₂SiH₂)
- Higher organosilicon species (carbosilanes, silazanes)
- Hydrogen cyanide (HCN) — a potential prebiotic molecule
- Amino-silanes (H₂N-SiH₃)
- Complex cross-linked organosilicon polymers

The composition depends on gas ratios, energy input, and temperature — all of which vary across the terminator storm front.

**Miller-Urey parallel:** The bible's claim that lightning is the origin-of-life engine is well-motivated. Miller-Urey (1953) produced amino acids from CH₄/NH₃/H₂/H₂O with electrical discharge. This planet runs the same experiment with SiH₄ replacing H₂O, producing organosilicon building blocks instead of amino acids. The chemistry is directly analogous. This is arguably the strongest single piece of chemistry in the entire worldbuilding.

---

## 10. AMMONIA SOLVENT CHEMISTRY

### 10.1 Physical Properties at Planetary Conditions

| Property | NH₃ at ~1.0 bar partial pressure, 240K | Water at 1 bar, 293K |
|---|---|---|
| State | Liquid (bp ~240K at 1.0 bar pp; well within liquid range at 8 bar total) | Liquid |
| Density | ~660-680 kg/m³ | 998 kg/m³ |
| Viscosity | ~0.16 mPa·s | 1.00 mPa·s |
| Dielectric constant | ~22 | 80 |
| Autoprotolysis | 2NH₃ ⇌ NH₄⁺ + NH₂⁻ | 2H₂O ⇌ H₃O⁺ + OH⁻ |

**✓ SOUND.** Liquid ammonia at ~1.0 bar partial pressure and 240K (terminator) is at approximately its dew point — condensation line coincides with the terminator, making it the rain zone. It's a real solvent used in laboratory chemistry. It dissolves polar compounds, supports acid-base reactions, and importantly: **it does not attack Si-Si bonds.**

This last point is critical and correctly stated in the bible. Water hydrolyzes Si-Si bonds (producing silanols, then siloxanes, then silica). Ammonia does not — Si-N bonds are stable, and ammonia actually *forms* silazane bonds rather than breaking silicon bonds. Ammonia is the biologically compatible solvent; water is the poison.

### 10.2 Ammonia-Sea Biology

Amorphs in ammonia seas: the bible says they are "smaller, faster-metabolizing, shorter-lived, involuntary cognitive broadcasting." 

The last property has a chemical basis: ammonia is a better ionic conductor than the silazane matrix. Neural signals (electronic in the semiconductor body) leak into the surrounding ammonia as ionic currents. The organism's thoughts radiate into the medium. Privacy requires insulation; immersion in a conducting fluid makes insulation impossible.

**✓ SOUND.** This is a direct and correct consequence of ammonia's physical properties as an ionic solvent.

---

## 11. THE MOLECULAR LIBRARY — INFORMATION CHEMISTRY

### 11.1 Polysilane as Information Carrier

The bible says: "Polysilane linked-list. Short fragments with terminal addressing sequences (end-caps)."

**✓ SOUND in principle, ⚠ NEEDS MECHANISM for addressing.**

Polysilanes can encode information through variable side chains along the Si-Si backbone. Possible coding scheme:

| Position | Side chain | "Letter" |
|---|---|---|
| 1 | -H | Base state |
| 2 | -CH₃ | Methyl = one bit |
| 3 | -C₂H₅ | Ethyl = different bit |
| 4 | -NH₂ | Amino = different bit |
| 5 | -SiH₃ | Branched = different bit |

With 4+ distinguishable side chains, you get a coding density comparable to DNA's four bases. But polysilane has a significant advantage: the backbone is a semiconductor. A polysilane fragment can be *electrically read* — different substituents alter the local electronic structure, and a semiconductor reader could detect the sequence by scanning conductance along the chain. No chemical "unzipping" required. Reading is electronic, not chemical.

### 11.2 End-Cap Addressing

"Terminal addressing sequences" = specific chemical groups at the chain ends that determine which reader can bind and which slot in the library the fragment occupies. Analogous to restriction enzyme recognition sites in DNA, but matched by complementary binding geometry rather than base pairing.

**Proposed chemistry:** End-caps are cyclic silazane rings with specific substituent patterns — like a molecular barcode. Reader enzymes have complementary binding pockets. Wrong cap = no binding = fragment ignored. Right cap = fragment recruited, read, expressed.

### 11.3 Fragment Integrity and Degradation

Polysilane Si-Si bonds are ~226 kJ/mol (weaker than C-C at ~346 kJ/mol). This makes them more susceptible to:
- UV cleavage (mitigated by low stellar UV)
- Oxidative cleavage by trace H₂O (→ petrification)
- Thermal degradation above ~300°C

**Library degradation over time = aging.** Accumulated Si-Si bond breaks, cross-links from stray reactions, and oxidative damage to fragments. This is the chemical basis for the bible's "genome degradation" component of aging. The library literally wears out.

---

## 12. SPECIFIC CORRECTIONS TO BIBLE/SPINE

### 12.1 Must-Fix

| Location | Current text | Problem | Fix |
|---|---|---|---|
| Bible §6.1, §8.1 | "Silicone oil (polydimethylsiloxane and relatives)" | Oxygen-based polymer in oxygen-free world | **"Silazane oil (polymethylsilazane and relatives)"** |
| Bible §8.1 | "silane/siloxane polymer" | Same oxygen problem | **"silane/silazane polymer"** |
| Spine, Biochemistry | "Solvent/matrix: Silicone oil (PDMS and relatives)" | Same | **"Silazane oil (polymethylsilazane and relatives)"** |
| Spine, Amorph Biology | "Silane/siloxane gel + silicone oil" | Same | **"Silane/silazane gel + silazane oil"** |
| Bible §6.1 | "Silicon's bandgap (1.1 eV) matches star's peak emission (~850 nm)" | 1.1 eV → 1107 nm, not 850 nm | **"Silicon's bandgap (1.1 eV, absorption edge ~1100 nm) captures the star's peak emission (~850 nm, ~1.46 eV) efficiently"** |

### 12.2 Should-Specify

| Topic | Current state | Proposed specification |
|---|---|---|
| Conductive mineral | Unnamed | Nitrogen-doped silicon carbide (N:SiC), variable polytype |
| Deep-rock energy source | "geothermally mobilized hydrogen and mineral-bound silicon" | Geothermal SiH₄ percolating through fractures; same metabolism as surface life, different source |
| Catalysis | Not addressed | Transition-metal-centered silazane-scaffold enzymes (Fe, Ni, Ti, Co active sites) |
| Petrification mechanism | "trace oxidizers convert Si-Si to glass" | Specific: H₂O hydrolyzes Si-NH-Si → Si-O-Si → SiO₂. Staged, progressive, increasingly irreversible. |
| Fluorine storage | Not addressed | Metal fluoride (CaF₂) in SiC-lined vesicles; enzymatic F₂ liberation on deployment |
| Library chemistry | "polysilane linked-list" | Polysilane with variable side chains (H, CH₃, C₂H₅, NH₂) as coding; cyclic silazane end-caps as addressing; electronic readout |

### 12.3 Bonus: Petrification Staging

The siloxane→silica correction enables a medically detailed petrification progression:

| Stage | Chemistry | Clinical presentation | Reversible? |
|---|---|---|---|
| 0 (healthy) | All Si-NH-Si bonds intact | Normal tissue | — |
| 1 (exposure) | Scattered Si-NH-Si → Si-OH (silanol) | Localized stiffness, reduced flexibility | Yes, if caught early |
| 2 (early petrification) | Si-OH condenses: Si-O-Si (siloxane) regions | Brittle patches, loss of reconfigurability in affected zone | Partially (amputation of affected region) |
| 3 (progressive) | Siloxane regions cross-link, approach SiO₂ stoichiometry | Hard, translucent zones spreading from site of water exposure | No — amputation of entire region required |
| 4 (terminal) | Bulk conversion to amorphous SiO₂ | Entire body a rigid glass object | Organism is dead; body persists as mineral fossil |

This gives the disease the progression described in the bible (chronic, like arthritis, with amputation as treatment) but with specific chemistry at each stage.

---

## 13. OPEN CHEMISTRY QUESTIONS

Items the chemistry hub does not yet resolve:

**□ Specific catalysts for carbosilane Stage 1** — What metal center activates the CH₄ + SiH₄ → CH₃SiH₃ reaction at biological temperatures? Nickel is the best candidate (Ni-catalyzed hydrosilylation is established), but the specific enzymatic mechanism needs thought.

**□ Polysilane replication mechanism** — How is the molecular library copied during reproduction? DNA uses template-directed polymerization (complementary base pairing). What's the silicon analog? One possibility: the polysilane fragment serves as a physical template for side-chain-complementary deposition. Another: enzymatic reading + de novo synthesis (no template, just transcription).

**□ SiC polytype control** — Different SiC polytypes (3C, 4H, 6H) have different bandgaps and electronic properties. Can biology control which polytype it deposits? Earth organisms control calcite vs. aragonite (same formula CaCO₃, different crystal structure), so polytype control is biologically precedented.

**□ Quantitative energy budget** — How many moles of SiH₄ does an amorph process per day? What's the surface area needed for sufficient photovoltaic energy? What fraction of energy comes from each source (chemical, photovoltaic, piezoelectric) in different environments?

**□ The immune system** — What specific chemistry does the "chelation immune response" use? Chelation implies metal-sequestration — possibly stripping catalytic metals from invading organisms' enzymes, inactivating them. If your enzymes are metalloenzymes, stealing the metal center kills the enzyme.

**□ Crystallization disease mechanism** — "Inappropriate cross-linking propagates like prions." What's the specific chemistry? Possibly: a misfolded catalytic fragment that catalyzes further cross-linking in neighboring silazane matrix, spreading geometrically. The cross-link converts flexible -Si-NH-Si- to rigid -Si-N(-Si-)-Si- (three-coordinate nitrogen), creating a rigid network that templates further rigidification. A silazane prion.

**□ Sleep chemistry** — The bible says decomposers "attack slow-metabolizing tissue" and "sleep requires keep-alive signals." The keep-alive signal is presumably an EM emission that marks tissue as living. What chemical process generates it? Possibly: baseline semiconductor current flow through healthy tissue produces a characteristic EM signature. When metabolism drops (sleep), current drops, signature weakens, and decomposers interpret the silence as death. Sleep requires active broadcasting of a "still alive" signal.

---

## 14. SUMMARY TABLE: STATUS OF ALL CHEMISTRY

| Claim | Status | Action |
|---|---|---|
| H₂/CH₄/NH₃/SiH₄ reducing atmosphere | ✓ SOUND | None |
| Si-Si polysilane backbone | ✓ SOUND | None |
| Silicone oil (PDMS) as matrix | **⚠ REVISE** | → Silazane oil (polymethylsilazane) |
| SiH₄ as energy feedstock | ✓ SOUND | Specify reaction: SiH₄ → Si + 2H₂, ΔH = -34.3 kJ/mol |
| Photovoltaic at 850 nm | ✓ SOUND | Clarify: Si absorbs 850 nm (above bandgap), not matches it |
| Carbosilane pathway | ✓ SOUND | Specify four stages with real chemistry (§6) |
| SiC fiber composite | ✓ SOUND | None — industrial process matches biology |
| Electronic neural signaling | ✓ SOUND | Specify: N-doped SiC default, B for p-type, p-n junctions as biological diodes |
| Fluorine attacks Si → SiF₄ | ✓ SOUND | This is literally semiconductor etch chemistry |
| F₂ + H₂ → HF flame | ✓ SOUND | ΔH = -542 kJ/mol. Twice hydrogen-oxygen. |
| Lightning = Miller-Urey | ✓ SOUND | Strongest chemistry in the project |
| Ammonia doesn't attack Si-Si | ✓ SOUND | NH₃ forms Si-N, doesn't cleave Si-Si |
| Ammonia-sea cognitive leakage | ✓ SOUND | NH₃ ionic conductivity makes insulation impossible |
| Conductive mineral (lattice) | ⚠ UNSPECIFIED | → Nitrogen-doped SiC (§4) |
| Deep-rock energy source | ⚠ VAGUE | → Geothermal SiH₄ in fractures (§3.5) |
| Petrification mechanism | ⚠ VAGUE | → Si-NH-Si hydrolysis by H₂O → Si-O-Si → SiO₂ (§1, §12.3) |
| Catalysis/enzymes | ⚠ ABSENT | → Metallosilazane enzymes (§8) |
| Library information chemistry | ⚠ VAGUE | → Side-chain coding, electronic readout, cyclic end-caps (§11) |
| Molecular library copying | **□ OPEN** | Template or transcription? Needs resolution |
| Immune system chemistry | **□ OPEN** | Chelation = metal-stripping? Needs resolution |
| Crystallization disease | **□ OPEN** | Silazane prion? Needs resolution |

---

*The chemistry found substrate and began to accrete.*
