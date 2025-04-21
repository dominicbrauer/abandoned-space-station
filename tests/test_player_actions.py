# pylint: disable=C

import io
import unittest
from unittest.mock import patch

from src import player_actions
from helpers import create_grid_template
from src.utils import constants as c


class TestPlayerActions(unittest.TestCase):
  def test_input_handling(self) -> None:
    grid = create_grid_template("default")

    # Test movement 'up'
    returnTuple = player_actions.input_handling(c.CONTROLS["movement"]["up"], [0, 0], grid)
    self.assertEqual(returnTuple, ([0, 0], grid, False))

    # Test action 'mark'
    returnTuple = player_actions.input_handling(c.CONTROLS["action"]["mark"], [0, 0], grid)
    grid[0][0].toggle_marked()
    self.assertEqual(returnTuple, ([0, 0], grid, False))

    # Test if invalid input triggers error
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
      returnTuple = player_actions.input_handling("InvalidInput", [0, 0], grid)

      output = mock_stdout.getvalue().strip()
      
      self.assertIn("InvalidActionError", output)
