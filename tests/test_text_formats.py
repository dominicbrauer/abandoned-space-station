# pylint: disable=C

import unittest
from unittest.mock import patch, MagicMock

from src.utils import text_formats


class TestTextFormats(unittest.TestCase):
  def test_italic(self) -> None:
    normalText = "Hello World"
    italicText = text_formats.italic(normalText)
    self.assertEqual("\033[3m" + normalText + "\033[23m", italicText)


  @patch('os.system')
  def test_clear(self, mock_system: MagicMock) -> None:
    text_formats.clear()
    mock_system.assert_called_once()
