# Pixel Streamer — Rebuild Roadmap

Full design recovered from the original Google Playground build (13 prompts, Oct 10 2026).
We are rebuilding this entire game in Python, piece by piece — including every add-on.

## The game

2D pixel-art arcade game: run a livestream studio, gain subscribers, don't let your rig overheat.

- **Win:** reach 1,000,000 subs + Diamond Creator trophy → unlock endless "Surfing" prestige mode
- **Lose:** rig overheats completely, or broadcast health hits zero from unresolved glitches

## All the add-ons (every feature, to be rebuilt)

1. **Core loop** — stream to gain subs (heat rises), cool the rig (heat drops), hype blasts (limited uses, big gains)
2. **Glitch events** — live-chat alerts pop up mid-stream; resolve them fast or lose subs and broadcast health
3. **Studio Props shop** — Artuban sculpture, pixelated movie posters (Cyber Odyssey 2027, Neon Mecha Rising, 8-Bit Space Hero), gaming figures (Pixel Samurai, Cyber Mecha, Mythic Chibi Dragon)
4. **Upcoming Rappers** — signable artists: Lil Byte (8-Bit Trap Pioneer), MC 808 (Cyber Boom-Bap Titan), Nova Flow (Melodic Autotune Queen), Young Quantum (Hyper-Drill Prodigy); in-studio performances + collab royalties
5. **Music Recording Studio wing** (unlockable) — vocal booth, mixing console / DJ turntables, gold & platinum record plaques
6. **Stream Length formats** — Quick Hit (30s), Standard (60s), Endurance Marathon (120s, 2.1x subs), 24-Hour Subathon (240s, 3.5x), Never-Ending Cypher (infinite, 5.0x)
7. **Passive sub generation** — subs trickle in over time from hardware, props, rappers, studio wing; Community Sub Bomb gift events
8. **Brand Promotions & Sponsorships** — NanoByte Energy, PixelWear Apparel, HyperViper Peripherals, Quantum Audio Labs, Neo-Tokyo Cyber Records, Solaris Interstellar Media; lump-sum credits, sub boosts, per-stream bonuses
9. **Camera angles** — default Streamer Webcam POV; presets: 2D Desk Stream, Rap Vocal Booth, Mixing Console & DJ, Streamer Facecam, 2.5D Isometric Room, Artuban & Props, Cyber Pet Cam, Cinematic Wide, Overhead Blueprint
10. **Surfing prestige mode** — after the 1M-sub goal, restart ("surfing") with 2x stat multipliers and infinite algorithm-surfing runs
11. **Life Chapter prestige/rebirth** — keep 100% of subs, reset hardware/props/studio, +35% compounding sub multiplier per prestige, story reasons per chapter

## Build order (Python)

- **v1** ✅ — text version: core loop (stream/cool/hype), heat vs subs, glitch events
- **v2** — props shop (spend subs on props), more glitch events, sponsorships
- **v3** — rappers roster + music studio wing
- **v4** — stream lengths, passive subs, surfing + life chapter prestige
- **v5** — graphics with pygame, camera views

## Original prompt history (design record)

1. "Make me a pewdiepie tuber simulator inspired game that's styled around streaming and upgrading equipment in the year 2027" → first draft "Holocaster 2027", isometric 3D
2. "lets try 2d" → re-drafted as 2D pixel-art arcade version
3. "After the final goal make a way to restart and call it surfing" → surfing prestige restart
4. "After the final goal make a way to restart and call it surfing lets also pixelate it more and styli…" → full pixelated visual overhaul + endless surfing mode
5. "add artuban sculpture,pixelated movie posters,gaming figures.Inside of the studio shop add a prop se…" → studio props shop
6. "yes lets proceed" → built everything so far
7. "I want it to be 2d but able to move the camera angles" → 2D default + free camera presets
8. "make it to where I can upcoming rappers and have a studio section to unlock as well" → rappers roster + music studio wing
9. "lets make a definitive way to earn subs over time maybe even longer streams" → passive subs + 5 stream length formats
10. "put the ui off the left hand side as well making it smaller.lets add set camera angles to pick from" → compact left sidebar + 9 camera presets
11. "the arms idle animation is backwards add the camera options to the right side" → fixed arm animations, camera panel right
12. "as well as make it to where I don't earn as much through subscribers off stream but rather getting p…" → rebalanced economy + brand promotions
13. "I would like the default camera to be webcam styled almost but still the available options on the ri…" → webcam POV default + life chapter prestige

(A few messages had their final characters clipped on screen; meaning is clear from what was built. Usage limit hit after prompt 13 — resets Oct 17.)
