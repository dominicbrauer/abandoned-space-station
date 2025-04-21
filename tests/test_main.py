# pylint: disable=C

import unittest
import io
import random
from unittest.mock import patch, MagicMock

from src import main

from src.utils import text_formats as tf, constants as c
from src.class_room import Room
from helpers import create_grid_template


def full_grid_test(inputs: list[str]) -> list[str]:
  """Creates an input combination to scan every room on the grid
    Returns:
      list: keyboard inputs (left/right, down, scan)
  """
  direction: int = 1
  for _ in range(c.GRID_SIZE):
    for col in range(c.GRID_SIZE):
      inputs.append(c.CONTROLS["action"]["scan"])
      if col < c.GRID_SIZE - 1:
        inputs.append(c.CONTROLS["movement"]["right"] if direction == 1 else c.CONTROLS["movement"]["left"])
    inputs.append(c.CONTROLS["movement"]["down"])
    direction *= -1
  return inputs


class TestMain(unittest.TestCase):
  def test_print_briefing_output(self) -> None:
    with patch('builtins.input', return_value=''), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
      main.print_briefing(["This is a test briefing."])

      output: list[str] = mock_stdout.getvalue().split('\n')

      # Test if any given briefing message is displayed
      self.assertEqual(output[-3], f"{tf.color_text(">>> This is a test briefing.", c.COLOR_ORANGE)}")
      self.assertEqual(output[-2], f"{tf.color_text(">>> ", c.COLOR_ORANGE)}")


  def test_win_analysis(self) -> None:
    # Test return 'True' if all rooms revealed
    self.assertTrue(main.win_analysis(create_grid_template("all-revealed")))
    # Test return 'False' if no room is revealed
    self.assertFalse(main.win_analysis(create_grid_template("default")))


  def test_print_room_name(self) -> None:
    grid: list[list[Room]] = [[Room(revealed=True, name="TestingRoomName") for col in range(c.GRID_SIZE)] for row in range(c.GRID_SIZE)]

    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
      # Choose a random room on the grid
      main.print_room_name(random.choice(grid[random.choice(range(c.GRID_SIZE))]))

      output = mock_stdout.getvalue().strip()

      # Test if room name is output
      self.assertTrue("TESTINGROOMNAME" in output)
      # Test if function considers revealed status
      self.assertTrue(" (SECURED)" in output)


  def test_print_scan_result(self) -> None:
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
      main.print_scan_result(0)
      output = mock_stdout.getvalue().strip()
      # Test if output is long enough to be a full phrase
      self.assertGreater(len(output[15:-5]), 5)
      
      main.print_scan_result(1)
      output = mock_stdout.getvalue().strip()
      # Test if output is long enough to be a full phrase
      self.assertGreater(len(output[15:-5]), 5)


  def test_print_ending(self) -> None:
    with patch('builtins.input', return_value=''), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
      main.print_ending("game_win")
      output: list[str] = mock_stdout.getvalue().split('\n')
      # Test if last arrows before quit are printed
      self.assertEqual(output[-2], f"{tf.color_text(">>> ", c.COLOR_ORANGE)}")


  @patch('builtins.input', side_effect=full_grid_test(full_grid_test([""])))
  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('src.main.clear') # skip terminal clears while testing
  def test_main(self, mock_stdout: MagicMock, mock_input: MagicMock, mock_clear: MagicMock) -> None: # pylint: disable=unused-argument
    # Test if main() terminates by scanning every tile on the grid
    # With bomb count 0, it will always lead to game_win
    c.BOMB_COUNT = 0
    main.main()

    # With bomb count 2, it will always lead to game_over
    c.BOMB_COUNT = 2
    main.main()


  def test_create_grid_template(self) -> None:
    with self.assertRaises(ValueError):
      create_grid_template("InvalidCode")
