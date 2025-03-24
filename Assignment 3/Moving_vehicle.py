import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from Colliding_object import Colliding_object

class Moving_vehicle(Colliding_object):
  def __init__(self, image_file_name, location: tuple[int, int] = (0, 0)):
    super().__init__(image_file_name, location)
    
  def set_location(self, loc:tuple[int,int]):
    locx, locy = loc
    self.location = loc
    self.bounding_box = pygame.Rect(locx, locy, self.width, self.height)