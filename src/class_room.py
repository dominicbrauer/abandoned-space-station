"""
class_room.py contains the Room class
"""

class Room():
  """A room object is representing a single grid tile
    Args:
      value (int): m
      revealed (bool): m
      marked (bool): m
      name (str): m
    All parameters are optional and overwritten by defaults if missing
  """
  def __init__(self,
               value: int = 0,
               revealed: bool = False,
               marked: bool = False,
               name: str = "no-name") -> None:
    self._value: int = value
    self._revealed: bool = revealed
    self._marked: bool = marked
    self._name: str = name


  def get_value(self) -> int:
    """Does what it says
      Returns:
        int: value of room
    """
    return self._value


  def get_revealed(self) -> bool:
    """Does what it says
      Returns:
        bool: revealed-status of room
    """
    return self._revealed


  def get_marked(self) -> bool:
    """Does what it says
      Returns:
        bool: marked-status of room
    """
    return self._marked


  def set_value(self, val: int) -> None:
    """Does what it says
      Args:
        val (int): value from 0-9
    """
    self._value = val


  def get_name(self) -> str:
    """Does what it says
      Returns:
        str: room's name
    """
    return self._name


  def set_name(self, name: str) -> None:
    """Does what it says
      Args:
        name (str): room name
    """
    self._name = name


  def toggle_marked(self) -> None:
    """Marks or unmarks the room
    """
    if self._revealed is False:
      match(self._marked):
        case True:
          self._marked = False
        case False:
          self._marked = True


  def scan(self) -> bool:
    """Reveals the tile
      Returns:
        bool: True if freshly scanned, False if already scanned
    """
    if self._revealed:
      return False
    self._revealed = True
    return True
