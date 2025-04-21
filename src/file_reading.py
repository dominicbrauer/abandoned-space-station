"""file_reading.py handles story text files to use throughout the game
"""

import os
import sys
from .utils import constants as c, text_formats as tf


# directory of this script file_reading.py
script_dir: str = os.path.dirname(os.path.abspath(__file__))
# leads to data/ containing all relevant story elements
data_dir: str = os.path.join(script_dir, "..", "data")
del script_dir


story_elements: dict[str, list] = {
  "briefing": [],
  "room_names": [],
  "safe_room": [],
  "warning_room": [],
  "game_over": [],
  "game_win": []
}


def insert_story_elements() -> None:
  """Reads story-relevant text files from 'data/' and inserts them into a dictionary
  """
  try:
    for key in story_elements:
      file_path = os.path.join(data_dir, f"{key}.txt")
      with open(file_path, 'r', encoding="utf-8") as file:
        # this rather over-complex reading style ensures to not include any \n (new-line) characters
        story_elements.update({key: [line.strip() for line in file.readlines()]})

  except FileNotFoundError as e:
    print(tf.color_text(tf.bold("[FileNotFoundError]"), c.COLOR_RED))
    print(tf.color_text(str(e), c.COLOR_PINK))
    print(tf.color_text("Unable to run game. Shutting down...", c.COLOR_ORANGE))
    sys.exit(1)


insert_story_elements()
