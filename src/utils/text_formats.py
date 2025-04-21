"""text_formats.py contains all sorts of text conversion functions
"""

import os


def italic(text: str) -> str:
  """Turns text italic
    Args:
      text (str): text to be converted
    Returns:
      str: italic text
  """
  return "\033[3m" + text + "\033[23m"


def bold(text: str) -> str:
  """Turns text bold
    Args:
      text (str): text to be converted
    Returns:
      str: bold text
  """
  return "\033[1m" + text + "\033[22m"


def gray_bg(text: str) -> str:
  """Sets the background color to gray
    Args:
      text (str): text to be converted
    Returns:
      str: text with gray background
  """
  return "\033[48;5;238m" + text + "\033[49m"


def color_text(text: str, color_number: int) -> str:
  """Colors text with color code
    Args:
      text (str): text to be converted
      color_number (int): 0-255
    Returns:
      str: colored text
  """
  return f"\033[38;5;{color_number}m{text}\033[39m"


def clear() -> None:
  """Clears the terminal
  """
  os.system('clear' if os.name == 'posix' else 'cls')
