# pylint: disable=C

import io
import unittest
from unittest.mock import patch

from src import playing_field
from src.file_reading import story_elements
from helpers import create_grid_template


class TestPlayingField(unittest.TestCase):
  def test_current_room_status(self) -> None:
    tileText = playing_field.current_room_status(create_grid_template("all-one")[0][0], False)
    self.assertIn("1", tileText)
    tileText = playing_field.current_room_status(create_grid_template("all-marked")[0][0], False)
    self.assertIn("!", tileText)


  def test_pick_room_names(self) -> None:
    story_elements["room_names"] = []

    with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
      playing_field.pick_room_names(create_grid_template("default"))

      output = mock_stdout.getvalue().strip()

      self.assertIn("IndexError", output)
