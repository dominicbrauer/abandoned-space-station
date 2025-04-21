# pylint: disable=C

import unittest
from unittest.mock import patch, MagicMock

from src import file_reading


class TestFileReading(unittest.TestCase):
  @patch('sys.exit')
  @patch('src.file_reading.print')
  def test_insert_story_elements(self, mock_exit: MagicMock, mock_print: MagicMock) -> None: # pylint: disable=unused-argument
    file_reading.story_elements = {
      "briefin": [], # little error
      "room_names": [],
      "safe_room": [],
      "warning_room": [],
      "game_over": [],
      "game_win": []
    }
    
    file_reading.insert_story_elements()

    self.assertEqual(mock_print.call_count, 1)    
