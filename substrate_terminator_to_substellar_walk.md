# Walking from the Terminator Mound to the Substellar Pole

**Substrate world-building document — February 2026**

Load with: spine (required), mound geometry derivation (recommended).

---

## Overview

A walk along the equatorial terminator from the mound crest to the substellar pole covers 90° of planetary arc — approximately **15,200 km** (planet radius 9,684 km; 1° ≈ 169 km). The wind is at your back the entire way (surface flow is night→day). The star — a deep red M3V dwarf, angular diameter ~3.5° (7× the Sun from Earth), peak emission at 850 nm — rises from the horizon toward zenith as you walk. Sky color: amber to copper throughout, brightening day-ward. Illumination is dim by Earth standards (mostly near-IR), heavily red-shifted.

All distances below are measured from the mound crest. All temperatures are surface-level unless noted. θ is the angular distance from the substellar point.

### Rain physics note

Rain at the terminator is not vertical. Terminal velocity of ammonia drops in 8-bar atmosphere is ~3 m/s (2 mm drops) to ~1.5 m/s (1 mm drops). Surface wind is 9.5 m/s. Rain angle near the ground: **70–81° from vertical** depending on drop size — effectively horizontal. The wind reverses with altitude (surface layer day-ward, superstream at 12–16 km night-ward), so raindrop trajectories are S-curves, not straight slants. Horizontal displacement during fall is ~10–50 km depending on formation altitude — significant relative to the mound crest width (30–50 km) but small relative to the rain zone (~2,000 km). At the crest, the distinction between "rain" and "wind-driven fog" collapses: fine drops are aerosolized, visibility near zero, ammonia deposits on vertical surfaces (tower windward faces, grass blades) rather than falling onto horizontal ones. See §11 (Rain Column Geometry) for full derivation.

---

## 1. The Mound Crest (0 km, θ = 90°, T ≈ 230K)

**Elevation:** ~2 km above reference terrain. **Pressure:** ~5.6 bar. **Wind:** 9.5 m/s sustained (equivalent force to ~56 mph on Earth at 8-bar density).

You cannot see. The mound crest is supersaturated by ~3K — perpetually fog-bound, every surface streaming with liquid ammonia. The orographic effect (surface air forced up 2 km over the windward night-side slope) drives aggressive condensation right at the crest. Moisture delivery equivalent to 50–80 mm/hr, but arriving as **horizontal wind-driven fog and drizzle**, not as a vertical downpour. Ammonia collects on every exposed vertical surface — tower windward faces, grass blades, your own windward body — and streams day-ward as liquid film.

Continuous lightning in the 18 km saturated column overhead. Thunder at 8 bar is shockwave bombardment, not merely sound — physically damaging at ranges where Earth thunder is just loud. A thunder-skin baffle (membrane with gas pockets and Helmholtz cavities tuned to thunder frequencies) would be essential, and is in fact one of the oldest and most universal amorph memes.

The tower forest surrounds you. Towers are not columns but thin curved walls — symmetric airfoil cross-sections in plan view, blunt convex windward face, tapering to trailing edge with chimney vents (see [tower_visualization.html](tower_visualization.html) for interactive 3D shape). The windward face is the primary fog collector, presenting hundreds of meters of vertical cross-section to the horizontal ammonia blast. They rise perhaps a kilometer above you, though fog limits visibility to tens of meters. Base chord: 30–50 m. Span: 100–200+ m. Gothic cathedral buttress silhouette, merging into buried root systems via flared bases.

SiC grass covers every surface between towers — a continuous lattice of piezoelectric blades vibrating in the wind, harvesting charge. The grass is informationally dead (no signal processing, no awareness) but electrically live, feeding piezoelectric current into the tower root network. Fairy ring antenna arrays (SiC stalks budding from root nodes, dual-purpose antenna + wind harvester) appear at resistance-regular intervals along the root network — wherever cumulative signal attenuation hits the threshold for a relay node. Roots have neighbor-avoidance steering (each grows toward its target tower via the largest EM gap), so between-tower root runs don't normally cross — the only junctions are at tower bases. Fairy rings appear along each run, spaced by attenuation, not topology.

### Lightning regime and visual environment

A mature tower doesn't need continuous lightning to maintain function. Towers manage their electrical potential to **avoid** strikes when fully charged — they have no reason to attract discharge they can't use. At any given time, roughly **10% of towers** (distributed randomly) are actively recharging: lowering their potential to attract strikes from the continuous storm front. The other 90% are deflecting, their potential managed to present no preferential target.

The charge separation rate in the storm column is independent of surface behavior — the same triboelectric energy from the intense rainfall must discharge somewhere. The consequences:

- **Cloud-to-cloud and in-cloud discharges** absorb most of the energy. Without a convenient ground path through 90% of towers, most discharge stays at altitude. These illuminate the upper fog/cloud from above — diffuse, pulsing, relatively uniform.
- **The recharging 10%** become intense attractors, each pulling strikes from a catchment area roughly 10× its normal share. A recharging tower takes a strike every few seconds — nearly continuous electrical bombardment, its lattice cascading with conducted current almost without pause.
- **Grass and bare ground** collect minor residual discharge. Grass is cm-scale; even a non-attracting km-tall tower is more prominent. Grass lightning collection is real but secondary to its piezoelectric function.

**Spatial statistics:** At 6.5 km Fibonacci spacing, tower density is ~1 per 42 km². Recharging tower density at 10%: ~1 per 420 km². Average distance to nearest recharging tower: **~10 km**. Within 5 km of you: typically zero recharging towers. Within 10 km: roughly one, two-thirds of the time.

Corona discharge occurs on every conductive SiC point (grass tips, fairy ring stalks, tower strut edges) — physically real but **visually invisible**, overwhelmed by the ambient fog illumination from lightning. The ambient scattered light from overlapping discharges is 10⁵–10⁸× brighter than a corona point at viewing distance.

**What you see:**

- **Dominant feature: a luminous ceiling.** Cloud-to-cloud discharges at altitude illuminate the upper fog from above — a pulsing, flickering overhead glow, lavender-pink-white (plasma emission from N₂/H₂/NH₃/CH₄ mixture: violet from N₂ second positive band, red from H₂ Balmer series, blue-green from CH radicals). The glow varies in brightness several times per second but never goes dark. Light comes from above, not from all directions — the ground plane is dimmer than the ceiling.
- **Most towers (90%): dark shapes.** No strikes, no flaring. Silent SiC shadows looming in softly glowing fog. At 30 m through fog, a non-recharging tower is a vague darkening — the lattice silhouette blocking some of the overhead glow. The apex (3–5% solids) is nearly invisible.
- **Recharging towers (~10%): beacons.** When one happens to be nearby (< 3–5 km), it is unmistakable — a persistent directional brightening in the fog, flickering at several strikes per second, the lattice cascading with conducted current almost continuously. Not resolvable as a shape through dense fog, but a *direction that is always brighter*. At 5–10 km, a recharging tower registers as a faint directional pulse at the limit of fog visibility. Beyond 10 km, individual recharging towers merge into the general ambient.
- **Ground level:** ammonia streaming horizontally across grass and sediment, lit by the overhead glow. No visible corona on any surface. Dark texture in glowing fog.

The recharging beacons are **landmarks** — and their positions shift over time as towers cycle through charge states. The landscape has navigable features despite near-zero fog visibility. An amorph at the crest orients by the beacons, tracking their slow rotation as different towers enter and leave the recharging cycle.

**Natural zoning:** The 90% non-recharging towers are calmer, less EM-noisy — habitable, approachable, the normal environment for tower-coupled life. The recharging subset are temporarily unapproachable electrical furnaces: intense EM noise, near-continuous shockwave bombardment at close range, hazardous current densities in the lattice and surrounding ground. A rotating exclusion zone.

The acoustic environment is ferocious regardless: overlapping thunder from cloud-to-cloud discharges and distant recharging towers, wind roaring through porous tower lattice (broadband biological noise from symbiote-coated struts), ammonia fog hammering every surface. The cloud-to-cloud thunder at altitude is less intense per stroke than ground strikes but far more numerous, creating a sustained low-frequency pressure wall. A nearby recharging tower adds sharp shockwave pulses punching through the background roar. This is the richest, most violent habitat on the planet.

Tower spacing: ~6.5 km (Fibonacci phyllotaxis). The crest plateau is ~30–50 km wide and essentially flat. Crossing it, you pass through 5–8 tower shadows — most dark and silent, occasionally one blazing with recharge.

---

## 2. Lee Face Descent (0–170 km, θ = 90° → 89°, T = 230K → 241K)

You step off the crest onto the day-side slope and the wind becomes chaotic. Flow separating over the crest creates a recirculation zone — gusty, directionally unpredictable eddies, vortex shedding. This is **the only location on the planet with non-steady, non-unidirectional wind.** For any organism adapted to constant laminar flow, this is a disorienting sensory environment.

The **orographic rain shadow** begins immediately. Air descending the lee face warms adiabatically, evaporating moisture. Direct fog deposition drops off sharply. Liquid ammonia on the lee face comes primarily from what the towers and grass intercepted on the windward side and crest — collected fog draining day-ward as surface runoff, not from rain falling on the lee face itself.

The slope averages 0.7–1.2° (12–21 m/km descent), carved by ammonia runoff into gully/canyon systems spaced 1–5 km apart. Between gullies: grass-stabilized ridges with towers. In the gullies: braided ammonia channels rushing day-ward, carrying sediment eroded from the mound itself — the primary erosive load, orders of magnitude more than atmospheric particulate.

**Lightning on the lee face:** You are still under the 18 km storm column. The rain shadow suppresses local condensation, so ground strikes are less frequent here than at the crest — but cloud-to-cloud discharge overhead continues undiminished. The upper fog still pulses with lavender light above you, and thunder rolls continuously, though without the close-range shockwave bombardment of the crest. Recharging towers on the lee face still flare as beacons, but fewer (the rain shadow slightly reduces the need for recharging — less fog-net collection means less grid-surplus power cycling through). The storm is above and behind you, not around you.

**Visibility improves as you descend.** The condensation floor in this atmosphere rises ~120 m per degree K above the 240K dew point. At the crest (230K, 2 km elevation), the air is supersaturated — fog blankets everything. As you descend and warm, the fog thins. By ~50–80 km into the descent (elevation ~1.3 km, local T ~234K), horizontal visibility opens to a few hundred meters. By ~120 km (elevation ~0.5 km, local T ~238K), you can see 1–2 km — but the overcast ceiling is still low, perhaps 200–300 m above the ground. Towers vanish into the cloud deck less than halfway up their height. You see buttressed bases, flared root systems, the lower windward face — and above that, grey opacity.

**The surface root network is now visible.** Between towers, raised highways of structured SiC lattice cross the grass-covered ridges — the surface root network, connecting every tower to its neighbors. These are FPGA-structured conduits, informationally live, carrying signal packets and charge. They stand 10–30 cm above the surrounding grass, perhaps a meter wide — travel corridors for amorphs, the planet's road system. Unlike the grass (bare, dead SiC, piezoelectric only), the root highways have the fine-grained pore structure of tower lattice: regular, maintained, signal-carrying. At resistance-regular intervals along the highways, fairy ring antenna arrays sprout — rings of SiC stalks at varying heights, each ring ~2–5 m across, dual-purpose antenna and wind harvester. They appear wherever cumulative signal attenuation demands a relay node — several per tower-to-tower root run. Since roots steer toward their target tower and avoid other roots, the highways don't cross between towers; junctions exist only at tower bases. From a distance, the fairy rings punctuate each highway like mileposts along a road that runs straight from tower to tower.

**Close-up tower appearance (lower windward face).** Walking into the wind toward a tower (the blunt convex windward face is the side facing you), the lattice resolves out of the fog. At 100 m: a dark curved wall, slightly translucent — the 8–15% solids fraction at the base lets some of the overhead glow through. At 30 m: individual pore structure visible. The struts are ~2 mm SiC/SiCN, but coated in biological material to ~4–6 mm effective diameter — irregular, soft-looking, alive. The pore openings at the base are ~6–8 mm, tighter than higher up. The windward surface has a wet-forest texture: symbiote organisms coat every strut, their shells catching fog droplets that stream downward, carrying dissolved particulate. Among the sessile Healers (permanent encrusting organisms, their shells part of the lattice itself), mobile Healers crawl at 0.5–2 cm/s — 8-limbed scaffold-climbers, mm to cm scale, moving from strut to strut. They're performing routine maintenance: scraping, depositing PCS fill into erosion pits, metabolizing captured grit. Occasionally one pauses and discharges a brief blue-white arc into a strut crack — flow-through arc-CVD repair, the tower's lattice current powering the organism like a hand tool. Miners (similar body plan, heavier metallosilazane cargo visible as a darker ventral mass) cycle between the exterior surface and the interior, carrying metals inward. Guards lurk in junction pockets at strut intersections — ambush predators, spring-loaded, culling any symbiote that draws power without contributing.

The windward face **sounds** like rushing wind through dense wet forest — broadband biological noise from turbulent flow through irregularly-coated pore channels. Behind it, from the interior, a faint tonal hum: ~1 kHz Aeolian tones from bare struts in the structural webbing where no symbiotes live. The tower's voice.

Step around the flank and the character changes abruptly. The trailing edge is narrower, the struts barer, the chimney vents visible as discrete openings exhaling warm H₂-rich gas upward. The leeward face is sheltered — fewer symbiotes, less biological coating, the lattice more skeletal and crystalline. Miners stage here before depth runs. Guards patrol the transition zone. The acoustic shadow is sharp: the windward broadband cuts off within a few meters of the flank, replaced by the quiet filtered chord of chimney noise and attenuated interior tones.

Temperature rises rapidly: ~0.06 K per horizontal kilometer (the surface gradient near the terminator) *plus* ~5 K per kilometer of descent (lapse rate). You warm on both accounts. By the mound base at ~170 km, you've descended ~2 km and the reference surface temperature is ~241K — right at the ammonia dew point. The fog lifts fully. The cloud base is now ~120 m above the surface — the overcast ceiling that was pressing down on you for the entire descent has pulled away, and for the first time you can see horizontal distance. Towers ahead are visible to ~5–10 km (rain-free lee face, some residual haze), but their upper portions still disappear into the low overcast at ~120 m. You see a forest of truncated buttresses stretching to the horizon, cloud-capped.

For the first time you can see distance.

Looking back: the terminator wall. A kilometers-high cliff of fog stretching to the horizon in both directions — not a mountain range but a *luminous front*, the entire rain column made visible. The upper reaches pulse with lavender and pink-white light from cloud-to-cloud discharges that never stop, the fog acting as a diffuser for the continuous electrical storm inside. The wall has no fixed features. But embedded in it, irregularly spaced, towers in their recharging cycle flare into incandescence — each one a pillar of brighter light punching through the murk for hours, flickering at several strikes per second, then dimming as the tower fills its charge and the next one somewhere else along the wall lights up. No pattern, no rhythm. The wall breathes. At this distance (~170 km from the crest, fog thinning) you can see perhaps a dozen of these beacons spread across your field of view, each at a different stage of its cycle. They are not landmarks — they are weather. Attenuated thunder still reaches you: low-frequency pressure pulses arriving seconds after the flares, propagating efficiently in the dense atmosphere. The ground shudders faintly.

Looking forward: a vast, nearly flat plain stretching day-ward under a brightening amber sky. The star is ~1° above the horizon, a deep red ember barely visible through atmospheric haze. Towers day-ward of you are backlit — dark truncated silhouettes against the amber horizon, each outlined by a faint red-amber line at the flanks where the airfoil profile thins to a few strut layers. SiC is transparent to the star's red and near-IR output (bandgap 2.36 eV, transparent above ~525 nm), so where the optical path through the lattice is short enough — the knife-edge of the airfoil flanks — starlight passes through and the edge glows. At this distance and star elevation the effect is subtle, a hair-thin bright outline on each dark shape, but it's the first indication of something you'll see far more dramatically further on. Ammonia runoff from the mound spreads in braided channels across dark sediment, catching the dim reflected glow from the wall behind you.

---

## 3. The Mudflat (170–450 km, θ ≈ 89° → 87.5°, T = 241K → 243K)

At the mound base, gully mouths punch into the mudflat. Ammonia runoff exits the mound slope with significant energy and cuts into the flat — but like punching a pillow. The channel penetrates a short distance, turbulent churning picks up loose sediment and drops it right back, net transport near zero. Within 10 km the channelized flow spreads into broad sheet flow, 1–5 cm deep.

This is the **genesis environment** — a planet-wide band wrapping the entire 62,000 km terminator. Shallow ammonia film over reworked sediment, atmospheric SiH₄ in direct contact (maximum surface-to-volume ratio), metal-bearing sediment from tower ejecta, lightning from the storm front overhead. Abiogenesis has been running here continuously for billions of years. At the scale of genesis organisms (≤100 μm), you would see nothing.

The mudflat grades outward: wet (1–5 cm liquid NH₃) → damp (<5 mm film) → crusted (evaporites forming) over ~100–300 km. Towers continue throughout — the network extends well past the mound base into the rain zone. SiC grass thins as sediment transitions from mound-compacted to loose mudflat, but root highways persist between towers, their structured lattice standing above the wet surface like causeways. Fairy ring antenna arrays at the nodes are the most prominent vertical features between towers — stalks 1–3 m tall, catching the wind.

**Cloud base** has risen to ~200–360 m across the mudflat (T = 241–243K). Towers are now visible to roughly a third of their height — the lower buttresses, the first few hundred meters of the windward face and its crawling symbiote fauna, and then the lattice fading into grey overcast above. At ~360 m (outer mudflat edge), you can just see where the solids fraction begins to thin noticeably — the transition from 10–12% base opacity to the 5–8% mid-height region where the lattice becomes increasingly translucent. What lies above that remains hidden.

**Lightning** is still vigorous. The storm column overhead extends from the cloud base (~200–360 m) to ~18 km — still a massive engine of charge separation. Cloud-to-cloud discharge pulses continuously. Ground strikes hit recharging towers. Thunder is attenuated slightly (fewer nearby ground strikes than at the crest, the nearest recharging tower averaging ~10 km away), but the overlapping cloud-to-cloud thunder maintains a sustained low-frequency pressure that you feel in the ground as much as hear. The mudflat surface vibrates faintly with each major discharge overhead.

Looking back from the mid-mudflat: the terminator wall has receded but not diminished. At 250+ km distance the individual recharging beacons are no longer resolvable — they merge into the general luminosity of the front, a band of cold light stretching across the entire night-ward horizon. The wall is taller than it is distant (18 km storm column vs 250 km range), still dominating the sky behind you. Occasional brighter pulses ripple through it where a cluster of towers happens to recharge in synchrony — coincidence, not coordination, but it gives the wall a slow, irregular heartbeat. The foreground is dark wet sediment under angled rain, lit from behind by the glow. Your own shadow stretches day-ward, faint and diffuse. Nothing ahead but flat ground and dim red sky.

Rain here still reaches the surface — not the horizontal fog-blast of the mound crest, but angled precipitation. The condensation floor is now a few hundred meters up (surface temperature slightly above the 240K dew point), and the wind-driven slant (~70° from vertical) stretches rain arriving from the superstream above across the terrain at a steep angle. Drops that formed at 10–15 km altitude in the superstream tens of km night-ward of your position arrive here having been swept day-ward through the surface layer. The rain angle is gentler at altitude but still markedly non-vertical.

---

## 4. Day-Slope Rain Zone (450–1,700 km, θ ≈ 87° → 80°, T = 243K → 249K)

Past the mudflat's wet zone, walking across the **inner deposition zone** — accumulated wind-deposited sediment, km-deep over geological time. The surface warms and dries gradually. Rain is lighter and more intermittent: 5–10 mm/hr, falling from a condensation floor that rises as the surface warms. The rain is still severely angled (surface wind remains ~8–9 m/s, terminal velocity still ~3 m/s, angle ~70° from vertical), but it is recognizably *rain* rather than fog — individual drops visible, arriving at steep angles from the night-ward side.

Towers are present throughout this zone. All prerequisites are met: rainfall ammonia, atmospheric SiH₄ (a permanent gas everywhere — bp 161K, invisible to NH₃ rain), convective lightning from the storm front, deep-rock fracture networks below the geologically active day-side crust. Tower spacing may widen somewhat. SiC grass and fairy-ring antenna arrays continue between towers. Root highways connect towers across the plain — the same raised FPGA-structured causeways, now crossing dry sediment rather than grass-stabilized ridges.

The wind stabilizes. The lee-face recirculation is well behind you. A steady ~8–9 m/s pushes at your back. Ammonia from the lighter rain forms ephemeral rivers and deltas flowing day-ward, evaporating as the surface temperature rises above 240K. The rivers shorten, thin, and vanish over the distance. The star climbs to ~5–10° elevation. The amber sky brightens.

**The cloud base lifts progressively** as the surface warms (~120 m per K above 240K). At the start of this zone (243K), the ceiling is ~360 m. By 600 km from the crest (T ≈ 244K), it has risen to ~500 m. At 900 km (T ≈ 246K), ~700 m. Towers that were truncated by overcast at the mudflat are now revealed further up their height with every few hundred kilometers of walking. **Around 1,000–1,200 km from the crest (T ≈ 246–247K, cloud base ~800–900 m), you see a full tower for the first time** — base to apex, in a single view.

**The full tower portrait.** Approach from the windward side (you are walking with the wind; the tower's blunt convex face points night-ward, toward you). The star is behind it — 5–10° elevation, day-ward — so every tower in this direction is backlit.

At 5 km in the now-clear sub-cloud air: a dark airfoil silhouette against copper sky, **outlined in a sharp red-amber line**. The line traces the flanks and apex — everywhere the airfoil profile thins to a few strut layers and the star's light passes through. SiC is transparent to wavelengths above ~525 nm (bandgap 2.36 eV for 3C-SiC); the M-dwarf's output is almost entirely red and near-IR. But transparency per strut does not mean transparency through the lattice: each 2 mm SiC strut (refractive index ~2.6) reflects ~20% at each air-SiC interface, and through the full chord of the airfoil — hundreds of strut crossings — transmission is effectively zero. The center of the windward face is black. Only at the airfoil flanks, where the profile thins to centimeters and the path crosses a handful of struts, does starlight punch through. The gradient is exponential in path length and therefore knife-sharp: within the last few centimeters of the edge, transmission jumps from zero to near-full. A solar-eclipse corona effect — dark disk, bright limn.

The tower is a curved wall, wider cross-wind (100–200 m) than deep along the wind axis (30–50 m at the base, tapering to 3–8 m at the summit ridge). The base is broad and buttressed, flaring into the monadnock substrate. The profile narrows upward — widest at ~20–30% of height, converging to a thin blade at the apex. The apex ridge runs cross-wind, perhaps 20–60 m long. The red limn is brightest at the apex (thinnest lattice, fewest strut layers, least biological coating) and dims toward the base (denser lattice, thicker biological layer at the edge). Towers not directly between you and the star show the effect on one flank only — a red edge on the star-facing side, dark on the other.

At 1 km: the lattice texture resolves. The lower base (12–15% solids) reads as a dark, substantial wall — opaque even at the flanks (the higher solids fraction means more strut crossings per unit of edge thinning). Above the first 100 m, the solids fraction drops to 8%, then 5%. The face remains opaque center-to-center — you cannot see through the lattice at any solids fraction across the full chord — but the limn brightens as both the lattice thins and the biological coating becomes sparser. Near the apex (3–5% solids, minimal symbiotes), the lattice is so thin in the wind-axis dimension (3–8 m) that even moderate angular offsets from the center catch some transmitted starlight. The apex reads as a faint red haze dissolving into sky, capped by the bright edge-line. The windward face is darker than the leeward at all heights (biological coating absorbs and scatters), giving the tower an asymmetric appearance — grey-brown windward, pale green-grey leeward where bare crystalline SiCN catches reflected starlight.

At 200–500 m: the windward face's biological activity is visible as texture and motion. The symbiote-coated strut zone (2–3 m deep from the surface) reads as a rough, irregular skin — not the clean geometry of the interior structural webbing behind it. Mobile Healers crawl across the outer surface (visible as small moving shapes at this distance, mm-to-cm-scale 8-limbed climbers). Occasional arc-CVD flashes — brief blue-white sparks where a Healer is repairing a strut crack, each lasting a fraction of a second. In a well-maintained tower, you might count a dozen sparks per minute across the visible face. The windward face is a construction site that never stops.

The root-buttress interstices at the base are where amorphs live — naturally occurring gaps between the flared root structures and the monadnock substrate, meter-scale spaces sheltered from wind by the tower above. From outside: dark openings at the base of the buttresses, some with visible amorph activity (shapes moving in the sheltered space, the glint of SiC shell material). The maintained entry corridors on the leeward side are visible as smooth-walled passages through the base lattice, distinct from the raw pore structure around them.

**Lightning diminishes through this zone.** The rain rate has dropped from 50–80 mm/hr at the crest to 5–10 mm/hr and falling. Charge separation scales with rain intensity. At the start of the zone (450 km), lightning is still frequent — flashes every few seconds, thunder a sustained rumble. By 800 km (rain ~8 mm/hr), the cadence slows to individual flashes every 10–30 seconds, each followed by discrete thunder rather than a continuous wall of sound. You can count between flash and thunder now — the discharges are thinning enough to distinguish individual strokes. By 1,200 km (rain patchy, long dry intervals), lightning is sporadic — minutes between flashes. The overhead ceiling still lights up occasionally, but the continuous luminous glow of the crest is gone, replaced by individual flicker-and-dark events against the grey overcast. Recharging tower beacons become **more common, not less**: power demand hasn't changed but lightning supply has dropped, so each tower spends a larger fraction of its time in the recharging state. This is partially offset by increasing solar input — the star is now at 7–10° elevation, and the leeward-face Si photovoltaic films contribute real power that was negligible at the terminator horizon. But lightning remains the dominant source for heavy renovation work, and the net recharging fraction still rises — perhaps 20–40% here versus 10% at the crest. Each beacon is dimmer (fewer strikes per second in the thinning storm). The visual gradient shifts: at the crest, 10% of towers blaze intensely against a field of dark shapes. Here, a larger fraction flicker more faintly, competing for scarce lightning.

Around 1,200 km from the crest (θ ≈ 83°, T ≈ 246K), rain becomes patchy: long dry intervals, punctuated by showers. The towers here are **perpetually marginal** — not degraded from a former healthy state, but always stunted by the thin ammonia supply at this edge of the rain zone. Symbiote coverage on the windward face is patchy at steady state: bare SiCN struts visible between islands of biological activity, the lattice showing its crystalline skeleton through gaps where the ammonia supply can't sustain a full population. Fewer arc-CVD sparks — renovation is slower, limited by power and feedstock. Guards patrol smaller territories. Miners are fewer (less volcanic dust in the lighter rain, less metal to shuttle). The tower's acoustic signature shifts: more Aeolian tone (more bare struts exposed) relative to biological broadband (fewer symbiote-coated surfaces). The voice is cleaner, thinner, less alive. Dead-bug plume from the mound crest towers drifts overhead, carried day-ward by the wind — faint particulate haze of recycled SiC shells and tower waste.

---

## 5. The Rain Edge (1,700–2,100 km, θ ≈ 80° → 78°, T = 249K → 250K)

Surface rain ceases. What falls from the superstream above evaporates in the warmer lower atmosphere — virga, visible as curtains of ammonia rain that dissolve before reaching the ground. The condensation floor is now ~1.2–1.5 km above you — above the top of any tower. For the first time, the sky above the towers is not cloud but open air: hazy amber, brightening, the overcast retreating upward to become a distinct cloud layer rather than an all-encompassing ceiling. Horizontal visibility extends to 10+ km in the clear sub-cloud air. You can see several towers simultaneously, their full profiles from buttress to apex ridge, standing in a landscape that finally has depth.

**Lightning ends at the surface.** No rain reaching the ground means no conductive rain path for cloud-to-ground discharge. The last ground strikes hit the last recharging towers somewhere in the transition. Cloud-to-cloud discharges still flicker in the virga layer overhead — sporadic, dim, the remnants of the storm column's charge separation occurring entirely above the condensation floor. Thunder from these events is distant and muffled (1+ km of clear air between discharge and ground). At the crest, lightning was a thing that happened TO you. Here it is a thing that happens above you, fading.

The tower network ends. The last networked towers — the most marginal, barely sustained by the thinnest edge of the rain zone — are behind you now. You can see them clearly in the 10+ km visibility (star at ~10° elevation): sparse symbiote coverage at steady state, the red backlighting limn *brighter* on these marginal towers than on healthy crest towers because less biological coating means less scattering at the edges. A healthy tower is a dark shape with a red edge-line; a marginal tower glows redder, bare SiC transmitting the star's light more cleanly through thinner biological cover. Their Aeolian voice carries on the wind — cleaner, more tonal than the crest's broadband roar, the sound of mostly-bare struts.

Ahead of you: nothing that resembles a tower. Deep-rock vents still reach the surface past the rain edge — the geological substrate doesn't care about the rain boundary. But without liquid ammonia (the solvent that drives the dominant Si-N cementation pathway), without lightning (the pre-activation that produces reactive intermediates), and without Healers, these vents can only deposit polymer via gas-phase SiH₄ reacting with atmospheric NH₃ vapor on their catalytic surfaces at 250K. Extremely slow — orders of magnitude below the terminator rate. And without lightning, there is no ceramification: no heat source to convert polymer to SiC ceramic. What little polymer accumulates is just organic film, stripped by 7–8 m/s wind erosion nearly as fast as it forms. The equilibrium is essentially invisible — bare deep-rock outcrops with a thin polymer skin, indistinguishable from the surrounding sediment unless you knew where to look. Not degraded towers, not even stubs. Towers that never could be.

SiC grass thins to isolated patches, then stops — without tower-generated charge surplus, there's no root network to feed the grass's electrical connection. The last fairy rings are behind you, at the last networked tower. Surface roots end where the network decided the investment wasn't worth it. For the first time, you step off the grid entirely.

The ecological transition is stark. Behind you: a populated, managed, signal-rich landscape. Ahead: silence. No towers, no grass, no grid power, no rain. Occasional virga lightning still flickers in the overcast above, but at the surface the electrical environment is dead — no corona, no piezoelectric hum from grass, no lattice current. Any amorph walking this direction carries only the charge in its body and whatever it can metabolize from atmospheric SiH₄ (slow baseline, ~300W resting for a 100 kg individual). This is why the deposition zone was **pre-industrially inaccessible** — not physically impassable, but an energy desert stretching thousands of kilometers with no recharge opportunity.

Wind: ~7–8 m/s, steady, at your back.

---

## 6. The Dry Deposition Zone (2,100–6,800 km, θ ≈ 78° → 50°, T = 250K → 264K)

The longest, emptiest stretch. Nearly 5,000 km of dry, wind-sculpted sediment under a brightening amber sky. No life. No sound except wind.

The deposition zone is the planet's great sedimentary basin — atmospheric fines, volcanic ash, and dead-bug plume debris transported by the day-ward wind from the terminator storm belt and deposited as the air warms and dries. Sediment is potentially hundreds of meters deep over geological time (though deep compaction reduces the figure). The surface is compacted sediment plain, not bedrock.

**2,100–3,500 km (θ ≈ 78° → 65°, T = 250K → 257K):** Virga overhead — ammonia rain visible falling from the superstream but evaporating in the warm lower atmosphere. Sporadic lightning still flickers within the virga layer — increasingly rare, increasingly faint, cloud-to-cloud only. By ~2,500 km, flashes occur minutes apart. By ~3,000 km, you may walk for an hour between events. Temperature climbs steadily. Wind decreasing from ~7 m/s toward ~5 m/s. The star rises to 15–25° elevation. The landscape has a scoured, empty quality. Wind-sculptured surface features begin to appear: shallow **yardangs** (streamlined ridges) and **ventifacts** (wind-polished rock faces), both oriented radially toward the substellar point, carved by billions of years of unidirectional day-ward wind.

**3,500–5,100 km (θ ≈ 65° → 60°, T = 257K → 261K):** The sky clears of virga. No condensation at any altitude. **Complete electrical silence for the first time since the walk began** — no lightning at any range, no thunder, no corona, no piezoelectric hum. The only sound is wind on sediment. After 3,500 km of continuous electrical environment (from the crest's shockwave bombardment through the rain zone's diminishing flashes to the last virga flickers), the absence is profound. Wind drops toward its day-side minimum: ~3–4 m/s. This is the **doldrums** — the quietest, calmest region between the terminator's violence and the substellar chimney's acceleration. The star is at ~30° elevation, noticeably brighter, deep red-orange, the disk 7× the Sun's apparent size from Earth. The deep sediment plain stretches to the horizon in every direction. Silence. If you've crossed the Nullarbor Plain or the Empty Quarter, scale them by ten.

**5,100–6,800 km (θ ≈ 60° → 50°, T = 261K → 264K):** Temperature nearly flat (the day side is a thermostat, homogenized by convective mixing). Wind at its minimum: **2–4 m/s** — a gentle breeze by the standards of this planet, barely perceptible after the terminator. Sediment thins. Bedrock emerges — the first volcanic terrain. Shield volcano silhouettes appear on the horizon. The deposition zone grades into the active volcanic day side.

---

## 7. The Volcanic Transition (6,800–10,100 km, θ ≈ 50° → 30°, T ≈ 264K → 265K)

The terrain transforms. Deep sediment gives way to volcanic geology: basalt flows, shield volcanoes, lava tubes, fumaroles. The planet maintains 10–30 volcanic provinces simultaneously, preferentially on the day side (thinner, warmer lithosphere). You're walking into this construction zone.

Wind accelerates again as spherical convergence concentrates the day-ward flow. From the doldrums minimum of ~3 m/s, it climbs steadily. By θ = 30° (~10,100 km from the crest), wind is back to **5–8 m/s**. The velocity field follows v(θ) = v_term × (sin θ)^(−1/4), with acceleration noticeable as θ decreases.

The star is 60° above the horizon. Full day-side illumination — deep red-amber, dim by Earth-solar standards, but the brightest this planet gets at the surface.

**The fluorine ecology appears.** Day-side volcanic provinces are the domain of **thorn-flora** — sexual/genomic organisms, the planet's closest analog to plants (though with no photosynthesis in the Earth sense — they harvest geothermal and solar energy). Two energy variants: geothermal (thermoelectric roots into hot volcanic rock, simplest engineering, armed with thorns) and solar (heliostat reflector canopy + PV organ, more complex, unarmed, widespread). The thorns are seeds, pollen, and weapons simultaneously — triple-function reproductive/defense structures.

This is **viper territory.** Fluorine-vipers are the apex predators of the fluorine biome — biological railgun organisms that fire CaF₂ thorn ammunition. They're also the premium seed dispersers for thorn-flora (thorn-seeds embedded in corpses near CaF₂ deposits). CaF₂-loaded organisms broadcast aposematic EM signatures — honest, unfakeable warnings (crystal structure alters dielectric properties). One bad experience educates an amorph lineage permanently; sexual predators must relearn each generation.

The ecological character is utterly unlike the tower ecosystem — no grid, no network, no authentication, no managed ecology. This is a wild, unmanaged, venomous landscape. Fluorine biochemistry represents an entire adaptive radiation around volcanic provinces: SiF₄ volatilization (tissue gasses off on death), HF as weapon, CaF₂ as armor and ammunition.

Volcanism here is a **chemical hazard, not thermal** (stellar heating is ~1,600× internal heat flux). But volcanic outgassing — SiH₄, H₂O, HF near fluorine provinces — creates localized chemical dangers. H₂O exposure = petrification (K ≈ 10⁵, thermodynamically irreversible; organisms survive only through active metabolic repair). No ammonia at the surface — all vapor. SiH₄ is atmospheric (everywhere). Any amorph here metabolizes atmospheric SiH₄ for slow baseline power plus whatever solar energy their membrane captures (Si bandgap at 1.1 eV matches M-dwarf peak at 850 nm / 1.46 eV).

**Daysider amorphs exist here.** Refugees, originally, from key-rot plague (a pathological loss of tower authentication — "keyless" and "key-rot" are social slurs). Now an established diaspora. They raid the terminator for **charge** (power) and **metals** (tower-delivered catalytic metals), not ammonia (which is available from rainfall on the mound's day slope, 80–95% of which falls on their side of the crest).

---

## 8. Inner Volcanic Day Side (10,100–13,200 km, θ ≈ 30° → 12°, T ≈ 265K)

Temperature is locked at ~265K (−8°C). The tanh profile is flat — the day side is thermally homogenized by convective mixing in the chimney. Wind climbs steadily: 5–8 m/s at θ = 30°, rising as convergent geometry concentrates the flow.

Volcanic terrain dominates. Shield volcanoes, flood basalt provinces, fresh lava fields (no rain weathering — only wind erosion). Near the substellar point, volcanic construction rate exceeds erosion. The landscape is geologically young and active. Fountains of silane and water vapor (the two primary volcanic volatiles). Lava flows of silicate magma. Metal ores exposed at the surface — native metals, never oxidized in the reducing atmosphere, concentrated by magmatic differentiation and ammonia-hydrothermal processes. Day-side volcanic provinces are the planet's primary metal source.

Wind erosion sculpts the volcanic terrain: ventifacts, streamlined ridges oriented radially toward the substellar point, yardangs cut from softer inter-flow deposits. Close to the substellar point, fresh volcanic construction replaces anything the wind removes.

The star is nearly overhead — 60–78° elevation. Clear copper-amber sky. Paired **cyclonic Rossby gyres** flank the substellar point at mid-latitudes — standing atmospheric features, the planet's only permanent vortex systems outside the terminator storm belt.

The wind becomes serious. At θ ≈ 15°: ~12–15 m/s in 8-bar atmosphere. Dynamic pressure approaching 600–900 Pa — equivalent to sustained hurricane force on Earth. The air is dry, warm, and accelerating toward the convergence point ahead. Walking becomes difficult even with the wind at your back; the ground is scoured clean.

---

## 9. The Substellar Chimney (13,200–15,200 km, θ ≈ 12° → 0°, T = 265K)

The final 2,000 km. Wind peaks at **~17 m/s** around θ ≈ 12° — dynamic pressure ~1,200 Pa, equivalent to ~100 mph sustained on Earth. The atmosphere is screaming toward the substellar point. Walking *with* this wind, you'd be tumbling. Walking against it would be impossible for an amorph (cruise speed 0.1–0.3 m/s).

The chimney is where converging surface winds reach the substellar point and turn **upward**. Warm, ammonia-vapor-laden air rises in a massive thermal updraft — the engine driving the entire planetary overturning cell. This is why the substellar region is **dry**: the chimney is an evaporator, not a condenser. All ammonia is vapor. All SiH₄ is vapor. No liquid anywhere.

The star hangs directly overhead. Deep red disk, ~3.5° angular diameter. The amber sky is clearest here — heated from above, rising, no particulate (the chimney lofts everything upward into the superstream). Ground-level visibility is excellent for the first time since the deposition-zone doldrums, though looking straight up into the chimney would show a column of rising haze disappearing into altitude.

At the exact substellar point (θ = 0°), surface wind drops abruptly — horizontal flow has become vertical. **Calm at ground level**, roaring updraft above. Temperature: 265K (−8°C). The ground is fresh volcanic basalt — the youngest, most geologically active terrain on the planet, directly above the thinnest lithosphere and the most vigorous mantle plume activity.

No life. Too dry, too far from towers, too geologically violent. The only organisms that pass through are balloon fauna riding the chimney updraft into the superstream — the beginning of the planetary drifter circuit that will carry them night-ward across the dark side and back in a 30–65 day loop.

---

## 10. Summary Table

| Distance | θ | T (K) | Wind (m/s) | Key transition |
|---|---|---|---|---|
| 0 km | 90° | 230 | 9.5 (turbulent at lee edge) | Mound crest. Fog, visibility ~30 m. Continuous lightning (ceiling glow + beacons). 10%/90% tower recharging split. Root highways, fairy rings |
| ~170 km | 89° | 241 | 9.5 (stabilizing) | Mound base. Fog lifts; cloud base ~120 m. Towers truncated by overcast. Root network, symbiotes visible. Lightning vigorous |
| ~450 km | 87.5° | 243 | ~9 | Mudflat dry edge. Cloud base ~360 m (lower third of tower visible). Angled rain. Lightning frequent |
| ~1,000 km | 84° | 246 | ~8.5 | Cloud base ~800 m. **First full tower visible** base to apex. Lightning diminishing (discrete flashes) |
| ~1,700 km | 80° | 249 | ~8 | **Surface rain ceases.** Cloud base above towers. **Ground strikes end.** Last marginal networked towers. No viable monadnocks beyond |
| ~2,100 km | 78° | 250 | ~7 | Virga overhead, sporadic virga lightning. Dry deposition zone. Off the grid entirely |
| ~3,500 km | 65° | 257 | ~5 | Sky fully clear. **Complete electrical silence.** Sediment plain |
| ~5,100 km | 60° | 261 | ~3–4 | **Doldrums.** Wind minimum. Deepest silence |
| ~6,800 km | 50° | 264 | ~3 | Volcanic terrain emerges. Thorn-flora + fluorine ecology begins |
| ~10,100 km | 30° | 265 | 5–8 | Full volcanic construction zone. Wind re-accelerating |
| ~13,200 km | 12° | 265 | ~17 (peak) | **Chimney outer edge.** Hurricane-force at 8 bar |
| ~15,200 km | 0° | 265 | ~0 (horizontal) | Substellar pole. Surface calm, vertical updraft. Fresh basalt. No life |

**Total temperature change:** 230K → 265K (+35K over 15,200 km). Most of the thermal transition happens in the first ~2,000 km — the ammonia thermostat concentrates the gradient at the terminator. Beyond θ ≈ 60°, the temperature is essentially constant at 265K.

**Wind pattern:** Starts at 9.5 m/s (turbulent on lee face), stabilizes at ~8–9 m/s through the rain zone, drops to a minimum of 2–4 m/s in the doldrums (θ ≈ 50–60°), then re-accelerates via spherical convergence to a peak of ~17 m/s at θ ≈ 12° before dropping to zero horizontal at the substellar stagnation point.

---

## 11. Rain Column Geometry

### The problem

Ammonia raindrops in 8-bar atmosphere have terminal velocities of ~1.5–3.5 m/s (1–2.8 mm drops). Surface wind at the terminator is 9.5 m/s. The ratio gives a rain angle of **70–81° from vertical** near the ground — effectively horizontal. This applies throughout the surface rain zone (θ ≈ 78–90°).

Maximum stable ammonia drop diameter: ~2.8 mm (surface tension ~23 mN/m, about 1/3 of water, at 1.82g).

### The S-curve trajectory

The surface wind (0–~5 km) blows day-ward at ~9.5 m/s. The superstream (12–16 km) blows night-ward at ~20–40 m/s. The wind reverses with altitude. A raindrop born in the superstream follows a curved (S-shaped) trajectory: initially night-ward (carried by the superstream), decelerating through the shear zone (~5–10 km), then accelerating day-ward in the surface layer.

**Drop relaxation time:** τ = v_t / g = 3 / 17.85 ≈ **0.17 s**. Drops match local wind within fractions of a second (~30,000 relaxation times during a fall from 15 km). They track the wind field essentially perfectly.

### Horizontal displacement budget

Using a three-layer wind model at the equatorial terminator (+ = day-ward, − = night-ward):

| Layer | Altitude | Wind speed | Fall time (2 mm drop) | Horizontal displacement |
|---|---|---|---|---|
| Surface | 0–4 km | +9.5 m/s | ~1,300 s | +12.7 km (day-ward) |
| Transition | 4–10 km | +9.5 → −15 m/s (avg −2.75) | ~2,000 s | −5.5 km (night-ward) |
| Superstream | 10–16 km | −15 → −30 m/s (avg −22.5) | ~2,000 s | −45 km (night-ward) |

**Drop born at 16 km:** net displacement ≈ −38 km (night-ward).
**Drop born at 10 km:** net displacement ≈ +7 km (day-ward).
**Drop born at 4 km:** net displacement ≈ +13 km (day-ward).
**Crossover altitude** (zero net displacement): ~9–10 km.

Rain landing at a given surface point comes from displaced origins: upper-level condensate formed ~25–45 km day-ward (carried night-ward by superstream to arrive), low-level condensate formed ~5–13 km night-ward (carried day-ward by surface wind to arrive).

### Why rainfall rate approximately survives

Rainfall rate on a horizontal surface equals the vertical condensate flux: R = n × V_drop × v_t. This depends only on the downward velocity component and the condensate density — independent of horizontal wind. The horizontal displacement (~10–50 km) redistributes rain sources modestly but is small compared to the rain zone width (~2,000 km on the day side, ~850 km on the night side).

Consequence: the spine's rainfall rate numbers (10–20 mm/hr average, 50–80 mm/hr peak at crest) survive as **equivalent vertical moisture flux**, though the physical delivery mechanism is horizontal fog deposition and wind-driven drizzle rather than a vertical downpour.

### Orographic enhancement at the crest

The 2 km mound forces surface air upward over the windward (night-side) slope. Forced ascent cools air at the moist adiabatic rate (~5 K/km × 2 km = 10K cooling), driving enhanced condensation at and just before the crest. The crest is supersaturated by ~3K (230K surface vs ~233K local dew point). Fog deposition on tower and grass surfaces (occult precipitation) is a major moisture delivery mechanism at the crest, independent of raindrop trajectory.

### Lee-face rain shadow

Air descending the day-side slope warms adiabatically → evaporates moisture → rain shadow on the lee face. Runoff on the lee face comes primarily from ammonia intercepted by towers and grass on the windward side and crest, draining day-ward as surface liquid — not from direct rainfall on the lee face. This reinforces the role of towers as **fog-net collectors**: the blunt convex windward face of the airfoil cross-section is the primary ammonia interceptor, catching horizontal fog/drizzle on a vertical surface hundreds of meters tall.

### Peak rainfall location

The peak likely shifts **slightly night-ward** of the geometric mound crest — by perhaps 10–30 km — onto the upper windward face, where orographic condensation is strongest (air still ascending, maximum cooling rate). This shift is comparable to the crest plateau width (30–50 km) and could be absorbed into the existing model as a refinement without changing the architecture.

### Uncertainties

- Wind profile between the surface layer and superstream is poorly constrained (transition altitude, shear zone thickness, superstream speed at the terminator specifically). The displacement calculations are order-of-magnitude.
- Superstream speed at the terminator may differ from the transit-average 20–40 m/s cited in the spine (mass flux conservation suggests it could be higher, but the flow is 3D on a sphere).
- Drop size distribution in the fog/drizzle regime at the crest affects whether "rain" or "fog" is the better description (likely both coexist).
- The orographic enhancement magnitude depends on the actual wind profile over the night-side mound slope, which is not independently modeled.
