import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

class My_sprite(pygame.sprite.Sprite):
  def __init__(self, image_file_name:str, location:tuple[int, int]=(0,0)):
    pygame.sprite.Sprite.__init__(self)
    self.rendering = pygame.image.load(image_file_name)
    self.width = self.rendering.get_width()  
    self.height = self.rendering.get_height()
    self.location = location
    
  def get_image(self) -> pygame.Surface:
    return(self.rendering)
  
  def get_width(self)-> int:
    return(self.rendering.get_width())
  
  def get_height(self) -> int:
    return(self.rendering.get_height())
