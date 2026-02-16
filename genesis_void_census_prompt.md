# Genesis Void Census: How Many Abiogenesis Sites Exist Simultaneously?

## Your Task

Estimate the number of subsurface cavities ("genesis voids") that simultaneously satisfy all conditions for silicon-based abiogenesis on the planet described below. Produce a Drake-equation-style chain of factors, identify which terms dominate the uncertainty, and give a defensible order-of-magnitude range.

## The Planet

A tidally locked super-Earth orbiting a red dwarf. Key physical parameters:

- **Escape velocity:** 18.6 km/s (retains H₂ atmosphere)
- **Atmosphere:** H₂ 78%, CH₄ 12%, NH₃ 5%, N₂ 3%, SiH₄ 0.3% (volcanic outgassing), trace others
- **Surface pressure at terminator:** ~8 bar (ammonia is liquid at surface: boils ~323 K at 3.5 bar, so comfortably liquid at 270 K and 8 bar)
- **Terminator surface temperature:** ~270 K
- **Permanent storm front** at the terminator — continuous lightning (the planet's Miller-Urey reactor)
- **Geology:** Volcanically active, especially on the day side. Mafic/ultramafic crust (basalt-like). Transition metals (Ni, Fe, Co, Ti) are ubiquitous in the rock.
- **Geothermal silane:** SiH₄ is generated at depth (Si + 2H₂ → SiH₄, favored at high T/P) and percolates upward through fracture networks. This is separate from the atmospheric SiH₄ — it's the deep energy source.

## What Is a Genesis Void?

A subsurface gas-filled pocket in volcanic rock, typically near the terminator, where catalytic abiogenesis occurs. Physical scale: roughly **30–50 cm** across (basketball-sized to beach-ball-sized). Not a rare large cavern — a common void in fractured rock.

### Necessary Conditions (ALL must be met simultaneously)

1. **Gas-filled cavity** in volcanic rock. Size ~0.1–2 m across. Smaller and chemistry is trivially fast but surface area limits catalysis; larger and heavy building blocks can't reach walls by diffusion. The sweet spot is in the tens-of-centimeters range.

2. **Fissure connectivity upward to the surface.** Liquid ammonia rain must be able to trickle down through cracks into the void. The rain carries:
   - Dissolved lightning products (methylsilanes, silazane fragments, carbosilane fragments, amino fragments, oligomers) — these are the building blocks forged by lightning in the atmosphere
   - The ammonia itself, which is both carrier AND fuel (N-H bonds at ~390 kJ/mol are stripped by catalysis just like Si-H bonds)

3. **Fissure connectivity downward to geothermal source.** SiH₄ must seep up from below through fractures in the rock. The geothermal gradient must be active beneath the void.

4. **The same upward fissures serve as H₂ exhaust vents.** Light H₂ (mass 2, in a mostly-mass-32 SiH₄ atmosphere) rises through the cracks countercurrent to the descending ammonia rain. This is the entropy pump — without H₂ removal, the system reaches equilibrium and chemistry stops. The requirement is that cracks are wide enough for countercurrent gas/liquid flow, which is not a demanding constraint.

5. **Catalytic metals in the wall rock.** Ni, Fe, Co, Ti must be present in the cavity walls and must leach into the void. In mafic volcanic rock these are ubiquitous — this condition is essentially free.

6. **Temperature/pressure in the ammonia dewpoint window.** This is self-regulating: the void temperature must be just above the NH₃ dewpoint so that rain evaporates upon entry (delivering cargo and fuel as gas), rather than pooling as liquid or evaporating in the cracks before arrival. Clausius-Clapeyron gives the dewpoint:
   - T_dew = 2808 / (11.685 − ln(P_NH₃))  where P_NH₃ is in bar
   - At P_NH₃ ≈ 0.8–1.5 bar → T_dew ≈ 236–250 K
   - Void temperature = T_dew + 5–15 K (margin from geothermal heating + exothermic catalysis, regulated by evaporative cooling feedback)
   - **Operating range: ~240–265 K**
   - This constrains the depth: too deep = too hot (ammonia never condenses in the cracks), too shallow = too cold (ammonia stays liquid in the void). The habitable depth window depends on the local geothermal gradient.

7. **Not flooded.** Drainage or evaporation must keep pace with rain input. The void must be gas-phase, not a liquid ammonia pool. (Liquid ammonia pools are a *different* abiogenesis environment — see §14.13 of the source document — but not what we're estimating here.)

8. **Not sealed.** The void must not be a closed pocket — it needs throughput. Crack connectivity to both surface and depth is already required by conditions 2–4, so this is redundant but worth stating explicitly.

### Conditions That Are NOT Required

- The void does NOT need to be directly exposed to lightning. Lightning occurs on the surface; rain delivers the products underground.
- The void does NOT need liquid water (there is none on this planet).
- The void does NOT need to be large. Centimeter-to-meter scale voids in fractured basalt are extremely common.
- The void does NOT need a specific geometry. Irregular pockets, vesicles, fracture intersections, and collapsed lava tubes all qualify.

## The Estimation Framework

Think of this as a product of factors:

```
N_voids = A_zone × D_depth × V_density × f_connected × f_thermal × f_drainage × f_geothermal
```

Where:
- **A_zone**: Area of the terminator zone that receives both ammonia rain and has volcanic geology (km²). Consider: how wide is the habitable terminator band? The permanent storm provides lightning products, but rain must reach the ground. What fraction of the terminator circumference is geologically suitable (volcanic terrain vs. sedimentary, eroded, ice-covered)?

- **D_depth**: Thickness of the viable depth window (meters). Constrained by the thermal window above. What geothermal gradient is plausible? On Earth, ~25–30 K/km in continental crust, ~40–80 K/km near volcanic centers. This planet is more volcanically active. The depth window where void temperature falls in 240–265 K might be quite narrow (tens of meters?) or broad (hundreds of meters?) depending on gradient.

- **V_density**: Volumetric density of gas-filled voids of appropriate size in fractured volcanic rock (voids per m³). This is a well-studied quantity in terrestrial volcanology. Basaltic lava flows have vesicularity of 10–50%. Fracture-network porosity in the upper crust is 1–10%. How many discrete voids of 0.1–2 m scale exist per cubic meter? Per cubic kilometer?

- **f_connected**: Fraction of those voids that have dual fissure connectivity (upward to surface AND downward to geothermal source). This is a percolation theory problem. In well-fractured basalt, what fraction of voids sit on connected fracture pathways in both directions?

- **f_thermal**: Fraction in the correct thermal window. Partially redundant with D_depth but accounts for lateral thermal variation (proximity to magma chambers, hydrothermal vents, etc.)

- **f_drainage**: Fraction that are gas-filled rather than flooded. Depends on rain intensity vs. evaporation rate vs. crack drainage. In a near-dewpoint environment, evaporation is fast.

- **f_geothermal**: Fraction with active silane seepage from below. How much of the terminator zone has active geothermal silane generation beneath it? The planet has strong volcanism concentrated on the day side, but geothermal gradients extend well past the terminator.

## What I'm Looking For

1. **Estimate each factor** with reasoning. Use Earth analogs where appropriate (Iceland, Hawaii, mid-ocean ridges for fracture density; Io for volcanic intensity). Flag where you're making assumptions vs. using data.

2. **Identify the bottleneck.** Which factor dominates the uncertainty? Which could plausibly be near zero (killing the whole estimate) and which are safely large?

3. **Give a range.** Something like "10⁵ to 10⁹ simultaneously viable genesis voids" with the key uncertainties that span that range.

4. **Consider the implications for abiogenesis probability.** If N voids run independently for geological time (10⁸–10⁹ years), and each needs some improbable event (first self-replicating catalyst cycle), what does the numbers game look like? You don't need to solve abiogenesis — just frame how the void population affects the probability argument.

5. **Sensitivity analysis.** Which slider matters most? If the geothermal gradient is 2× steeper, what happens to N? If fracture connectivity drops by 10×?

## Reference Values You May Find Useful

- Earth's mid-ocean ridge system: ~65,000 km long, fracture zones extend 5–20 km on either side
- Icelandic basalt vesicularity: 15–40% by volume
- Basalt fracture spacing: 0.1–1 m typical in columnar-jointed flows
- Percolation threshold in 3D random networks: ~31% connectivity for site percolation
- Ammonia latent heat of vaporization: 23.35 kJ/mol
- NH₃ Clausius-Clapeyron: ln(P) = −2808/T + 11.685 (P in bar, T in K)
- SiH₄ geothermal generation: Si + 2H₂ → SiH₄ (favored at high T/P in reducing mantle)
- Planetary escape velocity 18.6 km/s implies a large rocky world — radius perhaps 1.5–2.5 R_Earth, surface gravity perhaps 1.5–3 g (you may want to constrain this from the escape velocity and atmosphere retention)

## Tone

Be rigorous. Flag speculation. Use Fermi estimation where data is absent but show your work. I'd rather have honest uncertainty bars than false precision. If a factor could plausibly range over 4 orders of magnitude, say so.

This number matters for the worldbuilding because it determines whether abiogenesis is a singular miracle that happened once, or an inevitable statistical outcome of planetary geology running for a billion years.
