"""
main.py controls the overall gameplay of "Abandoned Space Station"
"""
# 💣 \U0001F4A3
# box_drawing = ["╔", "╗", "╚", "╝", "═", "║", "╦", "╩", "╠", "╣", "╬"]
# ⚠ ☢ ⚑ ╳ ⏣


import random
from src.utils.text_formats import clear
from src.utils import constants as c, text_formats as tf
from src.class_room import Room
from src.playing_field import print_grid, generate_grid
from src.player_actions import input_handling
from src.file_reading import story_elements


def print_briefing(briefings: list[str]) -> None:
  """Output random mission briefing before game starts
    Args:
      briefings (list): all available briefing messages
  """
  print(tf.color_text(tf.bold("[OBJECTIVE]"), c.COLOR_YELLOW))
  for line in c.STORY:
    print(tf.color_text(f">>> {line}", c.COLOR_ORANGE))

  msg: str = random.choice(briefings)
  msg = msg[:-1] # remove last dot of text
  split_msg: list[str] = msg.split(". ")
  msg.rsplit()
  for line in split_msg:
    line += "."
    print(tf.color_text(f">>> {line}", c.COLOR_ORANGE))
  print(tf.color_text(">>> ", c.COLOR_ORANGE))
  input(tf.color_text(">>> CONFIRM TO INFILTRATE...", c.COLOR_ORANGE))


def win_analysis(grid: list[list[Room]]) -> bool:
  """Analyze if all safe rooms are revealed
    Args:
      grid (list): 2D-playing field
    Returns:
      bool: True if the win condition is met
  """
  for room in [room for row in grid for room in row]:
    if room.get_value() != 9 and room.get_revealed() is False:
      return False
  return True


def print_room_name(room: Room) -> None:
  """Output selected room's name
  """
  msg: str = ""
  msg += tf.color_text(tf.bold("[POSITION]"), c.COLOR_YELLOW)
  msg += " " + tf.color_text(f"<{tf.bold(room.get_name().upper())}>", c.COLOR_ORANGE)
  if room.get_revealed():
    msg += tf.color_text(" (SECURED)", c.COLOR_ORANGE)
  print(msg)


def print_scan_result(value: int) -> None:
  """Output a message about scan
    Args:
      value (int): tile's value
  """
  match(value):
    case 0:
      msg = str(random.choice(story_elements["safe_room"])).upper()
    case _:
      msg = str(random.choice(story_elements["warning_room"])).upper()

  print(tf.color_text(f">>> {msg}", c.COLOR_ORANGE))


def print_ending(ending_type: str) -> None:
  """Output ending text based on win/lose
    Args:
      ending_type (str):
        *"game_over"* for lose message,
        *"game_win"* for win message
  """
  msg: str = random.choice(story_elements[ending_type])
  msg = msg[:-1] # remove last dot '.' from text
  split_msg: list[str] = msg.split(". ")
  msg.rsplit()
  for line in split_msg:
    line += "."
    print(tf.color_text(f">>> {line}", c.COLOR_ORANGE))
  print(tf.color_text(">>> ", c.COLOR_ORANGE))
  input(tf.color_text(">>> CONFIRM TO EXIT...", c.COLOR_ORANGE))


def reveal_all_bombs(grid: list[list[Room]]) -> list[list[Room]]:
  """Every tile with value 9 gets revealed
    Args:
      grid (list): 2D-playing field
    Returns:
      list: same grid, but all bombs visible
  """
  for i in range(c.GRID_SIZE):
    for j in range(c.GRID_SIZE):
      if grid[i][j].get_value() == 9:
        grid[i][j].scan()
  return grid


def main() -> None:
  """Main function running the general game logic
  """
  assert (c.GRID_SIZE*2)-1 >= len(c.GAME_UI), c.UI_ERROR_MSG
  assert c.GRID_SIZE**2 > c.BOMB_COUNT, c.BOMB_ERROR_MSG

  # This is a 2D-list containing a default Room object for each tile
  grid: list[list[Room]] = generate_grid()
  # The player_cursor always starts at the top left corner of the grid
  player_cursor: list[int] = [0, 0]
  # True if bomb tile gets revealed
  game_over: bool = False
  # True if all safe rooms revealed
  win_condition: bool = False
  # True if scan executed last turn
  scan: bool = False

  clear()
  print_briefing(story_elements["briefing"])
  clear()

  while True:
    # always represents selected room
    selection: Room = grid[player_cursor[0]][player_cursor[1]]

    print_grid(grid, player_cursor)
    print_room_name(selection)

    if scan:
      if selection.get_value() == 9:
        game_over = True
        grid = reveal_all_bombs(grid)
        break
      print_scan_result(selection.get_value())

    user_input = input(tf.color_text(">>> ", c.COLOR_ORANGE))
    clear()
    player_cursor, grid, scan = input_handling(user_input, player_cursor, grid)

    if win_analysis(grid):
      win_condition = True
      break

  clear()
  print_grid(grid, player_cursor)

  if win_condition is True:
    print_ending("game_win")

  if game_over is True:
    print_ending("game_over")

  clear()


# Coverage treats this statement as 'missing'.
# Since there is no way to unittest this part of the program, I have
# excluded it from the coverage tests to make 100% coverage even possible
if __name__ == "__main__": # pragma: no cover
  main()
