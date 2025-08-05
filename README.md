# Abandoned Space Station 🛰️

A strategic terminal game based on [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) from 1990. Reveal all tiles on a grid while avoiding the bomb-infested ones.


## Getting started

This game can be played both on Windows 10/11 and Linux based systems. Regardless of what you are using, you will need **Python** to run it.

- **Windows** - Download Python 3.13.2 [here](https://www.python.org/downloads/).
- **Linux** - If you are using Linux, try to install Python with your preferred package manager (like APT):
```bash
sudo apt get update
sudo apt-get install python3.13.2
```

After you've installed Python on your system, you can start the game by running `mission_start.bat` on Windows or `mission_start.sh` on Linux.


## Story

- The space station [**Sevastopol**](https://alienanthology.fandom.com/wiki/Sevastopol_Station) has been a safe haven for many travelers in outer space. Though, after several conflicts with terrorist groups, the station had to be **evacuated**.
- You, member of a special task force, have been commanded to **secure the station** and all remaining inhabitants. Although all terrorists have left, evidence suggests that several **active explosive devices** remain scattered around the station.
- A **Radiac Scanner** is part of your equipment, indicating how many threats are near your location. You may only scan rooms that are safe since these bombs are **highly reactive** to your scanner's electromagnetic waves.


## Gameplay

As mentioned before, **Abandoned Space Station** is a modified version of *Minesweeper*. Therefore, the general gameplay follows the original:

- There is a cursor indicating which tile is targeted by the player. With `WASD`, it can be moved to any location on the playing field.
- With `X`, the player can mark the targeted tile if he's sure it contains a bomb.
- With `C`, the targeted tile is scanned. If it is safe, a digit indicating how many bombs are located around that tile gets shown. If an infested tile is scanned, the game is over.
- The player must use the given information to determine which tiles contain a bomb.
- If all tiles except the ones with a bomb are revealed, the player wins. The space station is secured.


## Features

Just recreating *Minesweeper* wouldn't be fun, right? Given that the game's setting is a space station, I have implemented many special features.

- There is a story about your mission.
- The playing field is displayed on a terminal. Each tile represents a room on the *Sevastopol*. Rooms are named randomly every game. You can add custom room names in `data/room_names.txt`.
- The terminal uses colors and symbols to indicate safe rooms and hazards.
- The user interface contains an overview about the game controls.
- Each action results in a random story text being displayed, which enhances immersion and brings life into the game.

## Dependencies

This project was developed on **Ubuntu 24.04 (WSL2)** using **Python 3.13.2**. Tested on Windows 11 and Ubuntu WSL2.
