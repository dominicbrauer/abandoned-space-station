"""test_helpers.py consists of helper methods for unittests
"""

from src.utils import constants as c
from src.class_room import Room

generation_codes: dict[str, int] = {
  "default": 0, # all value 0, unrevealed, unmarked
  "all-revealed": 1, # all value 0, revealed, unmarked
  "all-marked": 2, # default, but all marked
  "all-one": 3 # default, but all value 1
}


def create_grid_template(ruleset: str) -> list[list[Room]]:
  """Create a playing field with specific generation rules for test purposes
    Args:
      ruleset (str): the generation code
    Returns:
      list: 2D-playing field
  """
  chosen: int | None = generation_codes.get(ruleset)
  match(chosen):
    case 0:
      return [[Room() for col in range(c.GRID_SIZE)] for row in range(c.GRID_SIZE)]
    case 1:
      return [[Room(revealed=True) for col in range(c.GRID_SIZE)] for row in range(c.GRID_SIZE)]
    case 2:
      return [[Room(marked=True) for col in range(c.GRID_SIZE)] for row in range(c.GRID_SIZE)]
    case 3:
      return [[Room(value=1) for col in range(c.GRID_SIZE)] for row in range(c.GRID_SIZE)]
    case _:
      raise ValueError(f"Given generation code not supported: \'{ruleset}\'")
