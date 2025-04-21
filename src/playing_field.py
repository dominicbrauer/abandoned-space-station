"""
playing_field.py handles playing field printing and generation
"""

import random
from .class_room import Room
from .utils import constants as c, text_formats as tf
from .file_reading import story_elements


def wall_top_row() -> str:
  """Generates the top wall of the playing field
    Returns:
      str: the top wall of the playing field
  """
  temp = "▄ ╔"
  for col in range(c.GRID_SIZE):
    temp += 5 * "═"
    temp += "╦" if col < c.GRID_SIZE-1 else ""
  temp += "╗ ▄"
  return temp


def wall_middle_row() -> str:
  """Generates a middle wall of the playing field
    Returns:
      str: a middle wall of the playing field
  """
  temp = "█ ╠"
  for col in range(c.GRID_SIZE):
    temp += "═╍╍╍═"
    temp += "╬" if col < c.GRID_SIZE-1 else ""
  temp += "╣ █"
  return temp


def wall_bottom_row() -> str:
  """Generates the bottom wall of the playing field
    Returns:
      str: the bottom wall of the playing field
  """
  temp = "▀ ╚"
  for col in range(c.GRID_SIZE):
    temp += 5 * "═"
    temp += "╩" if col < c.GRID_SIZE-1 else ""
  temp += "╝ ▀"
  return temp


def number_row(row: int, grid: list[list[Room]], player_cursor: list[int]) -> str:
  """Prints the current state of the playing field
    Args:
      row (int): current row
      grid (list): 2D-grid of playing field
      player_cursor (list): grid coordinates of selected tile
  """
  temp = "▓═╣"
  for col in range(c.GRID_SIZE):
    temp += current_room_status(grid[row][col], row == player_cursor[0] and col == player_cursor[1])
    temp += "░" if col < c.GRID_SIZE-1 else ""
  temp += "╠═▓"
  return temp


def current_room_status(room: Room, selected: bool) -> str:
  """Analyzes the value of given grid tile
    Args:
      room (Room): room object
    Returns:
      str: final visualization
  """
  room_string = ""

  if room.get_revealed() is True:
    match(room.get_value()):
      case 0:
        room_string = tf.color_text("⚑ 0", c.COLOR_GREEN)
      case 9:
        room_string = tf.color_text(" ╳ ", c.COLOR_RED)
      case _:
        room_string = tf.color_text(f"⚠ {room.get_value()}", c.COLOR_ORANGE)
  elif room.get_marked() is True:
    room_string = tf.color_text("☢ !", c.COLOR_RED)
  else:
    room_string = tf.color_text(" ? ", 12)

  # highlight current tile if player has selected it
  room_string = tf.gray_bg(room_string) if selected is True else room_string

  return f" {room_string} "


def print_grid(grid: list[list[Room]], player_cursor: list[int]) -> None:
  """Prints the current state of the playing field
    Args:
      grid (list): 2D-grid of playing field
  """
  print(wall_top_row())
  ui_start: int = (c.GRID_SIZE*2) - len(c.GAME_UI) - 0
  ui_line: int = 0
  for row in range(c.GRID_SIZE):
    print(number_row(row, grid, player_cursor), end="")
    ui_line += 1
    print_ui(ui_line, ui_start)
    if row < c.GRID_SIZE-1:
      print(wall_middle_row(), end="")
      ui_line += 1
      print_ui(ui_line, ui_start)

  print(wall_bottom_row())


def print_ui(ui_line: int, ui_start: int) -> None:
  """Adds UI line next to the grid
    Args:
      ui_line (int): current line
      ui_start (int): where to start printing the UI
  """
  if ui_line >= ui_start and ui_line-ui_start < len(c.GAME_UI):
    print(f"  {c.GAME_UI[ui_line-ui_start]}")
  else:
    print()


def generate_grid() -> list[list[Room]]:
  """Fully generates a random playing field
    Args:
      grid (list): grid with default room objects
    Returns:
      list: final grid
  """
  grid: list[list[Room]] = [[Room() for col in range(c.GRID_SIZE)] for row in range(c.GRID_SIZE)]
  grid = pick_room_names(grid)
  grid = bomb_placement(grid)
  grid = warning_analysis(grid)
  return grid


def pick_room_names(grid: list[list[Room]]) -> list[list[Room]]:
  """Picks a room name one by one. After every room name has been used ones,\
    it will use the last one (default: Hallways) for the remaining rooms.

    Args:
      row (int): current grid row
      col (int): current grid col
    Returns:
      list: same grid, now containing room names from file
  """
  all_tiles: list[tuple[int, int]] = [
    (x, y) for x in range(c.GRID_SIZE) for y in range(c.GRID_SIZE)
  ]
  default_name: str = "Room" # default if room_names.txt is empty
  try:
    default_name = story_elements["room_names"][len(story_elements["room_names"])-1]
  except IndexError:
    error: str = ""
    error += tf.color_text(tf.bold("[IndexError]"), c.COLOR_RED)
    msg: str = "\'data/room_names.txt\' is empty. Using default instead..."
    error += " " + tf.color_text(msg, c.COLOR_PINK)
    print(error)

  for idx in range(len(all_tiles)):
    x, y = random.choice(all_tiles)
    if idx+1 < len(story_elements["room_names"]):
      grid[x][y].set_name(story_elements["room_names"][idx])
    else:
      grid[x][y].set_name(default_name)
    all_tiles.remove((x, y))

  return grid


def bomb_placement(grid: list[list[Room]]) -> list[list[Room]]:
  """Random bomb placement on the playing field
    Args:
      grid (list): 2D-grid of playing field
    Returns:
      list: same grid, now containing all bombs
  """
  allowed_spots = list(range((c.GRID_SIZE**2)-1))

  for _ in range(c.BOMB_COUNT):
    digit = random.choice(allowed_spots)
    row = digit // c.GRID_SIZE
    col = digit % c.GRID_SIZE
    grid[row][col].set_value(9)
    allowed_spots.remove(digit)

  return grid


def warning_analysis(grid: list[list[Room]]) -> list[list[Room]]:
  """Based on the bomb placement, the warning number for each tile is calculated
    Args:
      grid (list): 2D-grid of playing field
    Returns:
      list: final playing field
  """
  for row in range(c.GRID_SIZE):
    for col in range(c.GRID_SIZE):
      if grid[row][col].get_value() != 9:
        count: int = check_surroundings(grid, row, col)
        grid[row][col].set_value(count)

  return grid


def check_surroundings(grid: list[list[Room]], row: int, col: int) -> int:
  """Checks surrounding tiles for bombs
    Args:
      grid (list): 2D-playing field
      row (int): current row
      col (int): current column
    Returns:
      int: total bomb count surrounding the tile
  """
  tile_check: list[list[int]] = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
  ]
  count: int = 0

  for k in range(8):
    ni = row + tile_check[k][0]
    nj = col + tile_check[k][1]

    if 0 <= ni < c.GRID_SIZE and 0 <= nj < c.GRID_SIZE:
      if grid[ni][nj].get_value() == 9:
        count += 1

  return count
