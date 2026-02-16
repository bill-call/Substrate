# SUBSTRATE WORLDBUILDING — SESSION PROMPT

## CONTEXT

You are continuing a multi-session worldbuilding collaboration for a hard SF novel called SUBSTRATE. The world features silicon-based life on a tidally locked super-Earth orbiting a red dwarf.

This session focuses on **mantle geology and volcanism** — specifically whether the planet's volcanic regime is survivable, and what constraints need to hold for the biosphere to persist.

## KEY DOCUMENTS TO LOAD

1. **\_temp\_spine.md** — Master constraints. Always load. Contains planet parameters, atmosphere, geology section.
2. **\_temp\_bible.md** (v2.2) — Full reference. Load geology/atmosphere sections for deep-dive. Contains prose context the spine omits.
3. **substrate\_silicon\_chemistry\_hub (10).md** — Chemistry reference. Relevant for atmospheric SiH₄ budget (volcanic outgassing vs biological consumption = the crisis).
4. **substrate\_pool\_genesis\_hub.md** — Pool genesis. Relevant for terminator basin geology (flexure zones, fracture networks, sea basins).
5. **substrate\_fauna\_structural\_hub.md** — Fauna hub. Relevant for tower death mechanics during crisis, deep-rock biosphere survival.

## WHAT'S ESTABLISHED

### Planet Parameters

|Parameter|Value|
|-|-|
|Mass|4.2 M⊕|
|Radius|1.52 R⊕|
|Surface gravity|1.82g (17.85 m/s²)|
|Escape velocity|18.6 km/s|
|Orbit|0.12 AU, 18-day period, tidally locked 1:1|
|Atmosphere|8 bar. N₂ 55%, H₂ 15%, NH₃ 12.5%, CH₄ 10%, SiH₄ 0.3%|
|Surface temps|Substellar 265K, terminator 240K, antistellar 215K (ΔT = 50K)|

### Geology (from Spine)

* **Stagnant lid.** No plate tectonics, no subduction. Heat escapes via mantle plumes.
* **Hemispheric asymmetry:** Day-side lid thinner/warmer, plumes breach preferentially. Dark-side lid thick/cold/stable.
* **Day side:** Volcanically active. Shield volcanoes, flood basalts. Periodically resurfaced. Source of SiH₄ outgassing.
* **Dark side:** Geologically quiescent. Ancient stable crust. Minimal volcanism.
* **Terminator:** Lithospheric flexure zone. Chronic cracking/faulting. Primary fracture networks.
* **Fracture networks:** Discontinuous. Each isolated system hosts independent deep-rock colony.
* **Sea basins:** Volcanic: calderas, rift basins, terminator flexure depressions.
* **Metal ores:** Native metals (reducing atm = no oxidation). Concentrated by magmatic differentiation + NH₃ hydrothermal. Day-side volcanic provinces.
* **Fissile materials:** U/Th present (~4.2× Earth inventory). Magmatic + NH₃-hydrothermal concentration.
* **Atm. silane budget:** Volcanic outgassing replenishes. Crisis = volcanic decline outpaced by biological consumption.

### The Crisis (from Spine)

* Atmospheric SiH₄ depletion + oxidizer accumulation.
* Volcanic outgassing declining (planet cooling) vs biological consumption.
* High v\_esc retains H₂, accelerating crisis.
* Tower deaths: first in history. Source of morally harvestable material.
* Deep-rock survives (geothermal, not atm-dependent). Crisis kills branches, not trunk.

### Deep-Rock Biosphere (from Spine)

* Oldest life. Chemolithotrophic. Geothermal SiH₄ percolating through fracture networks.
* Day-side subsurface network: young, repeatedly pruned by volcanism.
* Dark-side: ancient, uninterrupted.
* Deep-rock survives atmospheric crisis (geothermal, not atm-dependent).

## THE CORE PROBLEM

The spine describes a stagnant-lid planet where heat escapes via mantle plumes. On Earth, stagnant-lid volcanism (think Venus or early Mars) can produce catastrophic flood basalt events when plumes breach the lid. Earth's Large Igneous Provinces (Siberian Traps, Deccan Traps) each drove mass extinctions — and those were on a 1 M⊕ planet WITH plate tectonics providing continuous pressure release.

On a 4.2 M⊕ super-Earth with stagnant lid:

* **Higher mantle heat budget.** More radiogenic heating (spine: ~4.2× Earth U/Th inventory). Higher primordial heat. More total energy to dissipate.
* **No continuous release valve.** No subduction, no mid-ocean ridges. Heat builds under the lid until a plume punches through. Events may be infrequent but enormous.
* **Day-side preferential breaching.** The thinner/warmer day-side lid is where plumes breach — which is also the hemisphere closest to the star, already the warmest.
* **Flood basalt scale.** A single Large Igneous Province on this planet could be vastly larger than anything in Earth's history. What does a super-Earth-scale flood basalt event do to the atmosphere? To the biosphere?
* **SiH₄ outgassing vs SO₂/CO₂ equivalent.** On Earth, flood basalts release SO₂ and CO₂, causing cooling (aerosol) then warming (greenhouse). What does a reducing-atmosphere super-Earth's volcanism release? SiH₄, H₂, NH₃, CH₄, H₂S? What are the atmospheric consequences?
* **Frequency.** How often do plume breakthroughs occur? If they're every few million years but devastating, the biosphere needs a recovery mechanism. If they're quasi-continuous but moderate, the biosphere can adapt.

**The existential question: Is this planet survivable on geological timescales, or does stagnant-lid volcanism on a 4.2 M⊕ super-Earth sterilize the surface periodically?**

## SESSION GOALS

1. **Mantle thermal model.** What is the heat budget? How does it compare to Earth? How does stagnant-lid convection behave at super-Earth scale? What controls plume frequency and intensity?
2. **Volcanic regime characterization.** What does volcanism look like on this planet? Shield volcanoes vs flood basalts vs something else? How large are individual events? How frequent?
3. **Atmospheric consequences.** What gases does reducing-atmosphere volcanism produce? What are the short-term and long-term effects on atmospheric composition? Is there an analog to Earth's volcanic winters?
4. **Biosphere survivability.** Can surface life persist through major volcanic events? What about the deep-rock biosphere? What recovery timescales are needed?
5. **Day-side vs dark-side asymmetry.** The day-side is repeatedly resurfaced. How often? How completely? What survives? Why is the dark-side stable?
6. **The SiH₄ budget problem.** Volcanism is the source of atmospheric SiH₄. But if volcanism is declining (planet cooling), when does the crisis hit? Is there a quantitative timeline?
7. **Knobs available for tuning.** If the default physics produces an uninhabitable planet, what parameters can we adjust (lid thickness, mantle viscosity, plume frequency, geographic containment, planet age) without breaking established constraints?

## ADDITIONAL CONTEXT FROM USER

Read super\_earth\_analysis.md

## WORKING METHOD

The user prefers:

* Rigorous physics (check energy budgets, thermal models, timescales)
* Tables for clarity
* Explicit marking of resolved vs open questions
* Building toward hub document updates (spine, bible, potentially new Geology module)
* Honest critique of proposals — if the numbers don't work, say so
* Technical peer interaction. No ego-boosting affirmations.
