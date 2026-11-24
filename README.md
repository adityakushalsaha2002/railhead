# Railhead

A first-person shooter that runs in the browser. You drop by helicopter into a rail yard, fight drones, robot dogs and armed guards across the yard, station and container port, and ride the engine out at the end.

Everything is generated in code when the page loads: models, textures, sounds and music. The game is one HTML file plus three.js from a CDN.

Built by Aditya K.

## Play

Open `index.html` in a desktop browser (Chrome, Edge or Firefox). Phones and tablets get touch controls.

To host it, turn on GitHub Pages for this repository (Settings, Pages, deploy from the `main` branch, root folder). The game is then served at `https://<username>.github.io/<repo-name>/`.

## Modes

- **Signal run:** overload three signal cabinets, then reach the engine at the junction.
- **Holdout:** survive waves of drones, walkers and guards.
- **Infiltration:** stealth. Cut the power and the network, defuse a bomb, free two hostages and reach the boat unseen.

Time of day: day, dusk, night or fog.

## Features

- Helicopter fast-rope opening and a departing-engine ending (any key skips).
- Rotating minimap with objectives and enemies.
- 26 primary weapons (assault rifles, SMGs, shotguns, marksman rifles, sniper rifles, LMGs) and 8 secondaries (pistols, rocket, guided missile and grenade launchers, combat knife).
- 20 sights including holographic, magnified, hybrid, variable, range-finder and thermal, with selectable reticles; muzzle devices and suppressors.
- Guards with hit zones, base sirens you can silence, a rail yard, station and container port.

## Controls

| Action | Keyboard and mouse |
| --- | --- |
| Move | W A S D or arrow keys |
| Jump | Space |
| Look | Mouse |
| Fire / aim | Left / right mouse button |
| Reload | R |
| Switch weapon | 1, 2, Q or mouse wheel |
| Crouch | C or Ctrl |
| Sprint | Shift (hold while scoped to steady your aim) |
| Use, defuse, silence sirens | E |
| Melee | F |
| Sight zoom | V (hybrid, dual and variable sights) |
| Pause | Esc or P |

Gamepads are supported.

## Building

Edit files in `src/` or `template.html`, then run `python3 build.py`, which rewrites `index.html`. No other tools are needed.

## Credits

- Built by Aditya K.
- Developed with Claude (Anthropic).
- Uses [three.js](https://threejs.org/) r128 (MIT licence).
