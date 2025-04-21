"""player_actions.py handles player movement, tile scanning and marking
"""

from .utils import constants as c
from .utils.error_handling import InvalidActionError
from .class_room import Room


def input_handling(user_input: str, player_cursor: list[int], grid: list[list[Room]]) -> tuple:
  """Processes and responds to player input
    Args:
      user_input (str): player input
      player_cursor (list): current selection
      grid (list): 2D-playing field
    Returns:
      tuple: 
        - list: updated player_selection
        - list: updated grid
        - bool: True if scan made
  """
  user_input = user_input.lower()
  x, y = player_cursor[0], player_cursor[1]
  scan: bool = False
  try:
    if user_input == c.CONTROLS["movement"]["up"]:
      x -= 1 if x > 0 else 0

    elif user_input == c.CONTROLS["movement"]["left"]:
      y -= 1 if y > 0 else 0

    elif user_input == c.CONTROLS["movement"]["down"]:
      x += 1 if x < c.GRID_SIZE-1 else 0

    elif user_input == c.CONTROLS["movement"]["right"]:
      y += 1 if y < c.GRID_SIZE-1 else 0

    elif user_input == c.CONTROLS["action"]["mark"]:
      grid[x][y].toggle_marked()

    elif user_input == c.CONTROLS["action"]["scan"]:
      scan = grid[x][y].scan()

    else:
      raise InvalidActionError(user_input)
  except InvalidActionError as e:
    print(e)

  return ([x, y], grid, scan)
