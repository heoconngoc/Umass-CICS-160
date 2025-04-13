import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

class My_sprite():
  def __init__(self, image_file_name: str, location: tuple[int, int] = (0, 0)):
    self.image_name = image_file_name
    self.image = pygame.image.load(image_file_name)
    self.location = location
    self.width = self.image.get_width()
    self.height = self.image.get_height()

  def get_image(self):
    return self.image

  def get_width(self) -> int:
    return self.width

  def get_height(self) -> int:
    return self.height

  def __eq__(self, other):
    return (
      isinstance(other, My_sprite) 
      and self.height == other.height 
      and self.width == other.width 
      and self.location == other.location
    )
