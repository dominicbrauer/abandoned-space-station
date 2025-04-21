# pylint: disable=C

import unittest

from src.class_room import Room


class TestClassRoom(unittest.TestCase):
  def test_scan(self) -> None:
    room_object: Room = Room(revealed=True)
    self.assertFalse(room_object.scan())
