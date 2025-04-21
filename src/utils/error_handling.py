"""class_error.py contains custom error handling
"""

from . import constants as c, text_formats as tf


class InvalidActionError(Exception):
  """Error for non-existent player moves or actions
  """
  def __init__(self, value: str) -> None:
    self._value = value
    self._message = "Can't handle unknown input"
    self._type = type(self).__name__


  def __str__(self) -> str:
    error: str = ""
    error += tf.bold(tf.color_text(f"[{self._type}]", c.COLOR_RED)) + " "
    error += tf.color_text(f"{self._message}: \'{self._value[0:10]}...\'", c.COLOR_PINK)
    return error
