"""
constants.py introduces all constant variables for the game
"""

from . import text_formats as tf


GRID_SIZE: int = 7 # default: 7
"""Sets the playing field size (rows and cols)
"""

BOMB_COUNT: int = 10 # default: 10
"""Controls how many bombs are placed on the playing field
"""

# Some used color codes
COLOR_RED: int = 9
COLOR_GREEN: int = 40
COLOR_ORANGE: int = 208
COLOR_PINK: int = 164
COLOR_YELLOW: int = 226


STORY: list[str] = [
  "\033[1mSPACE STATION SEVASTOPOL\033[22m",
  "The task force has been ordered to secure the Sevastopol.",
  "Several sectors were classified as \'dangerous\'.",
  ""
]


CONTROLS: dict[str, dict[str, str]] = {
  "movement": {
    "up": 'w',
    "left": 'a',
    "down": 's',
    "right": 'd'
  },
  "action": {
    "mark": 'x',
    "scan": 'c'
  }
}

GAME_UI: list[str] = [
  tf.color_text(tf.bold("# OBJECTIVE"), COLOR_YELLOW),
  "○ Secure the space station",
  f"○ ⚠ {tf.bold(str(BOMB_COUNT))} dangers detected",
  "",
  tf.color_text(tf.bold("# CONTROLS"), COLOR_YELLOW),
  f"○ <{tf.bold(CONTROLS["movement"]["up"].capitalize())}> : move up ↑",
  f"○ <{tf.bold(CONTROLS["movement"]["left"].capitalize())}> : move left ←",
  f"○ <{tf.bold(CONTROLS["movement"]["down"].capitalize())}> : move down ↓",
  f"○ <{tf.bold(CONTROLS["movement"]["right"].capitalize())}> : move right →",
  f"○ <{tf.bold(CONTROLS["action"]["mark"].capitalize())}> : mark room !",
  f"○ <{tf.bold(CONTROLS["action"]["scan"].capitalize())}> : scan room ◊"
]

UI_ERROR_MSG: str = f"Grid size ({GRID_SIZE}) too small for UI"
BOMB_ERROR_MSG: str = f"Bomb count ({BOMB_COUNT}) too large for grid size ({GRID_SIZE}x{GRID_SIZE})"
