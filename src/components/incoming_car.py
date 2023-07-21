import random
import pygame

from src.components.car_side import CarSide
### ROAD => LEFT, MIDDLE, RIGHT

class Car(pygame.sprite.Sprite):
     def __init__(self, car_side, Carside):
          super().__init__()
          self.new_speed = random.uniform(2,3.5)
          self.new_y = 0
          self.offset_x = 0
          self.new_x = sine(100.0, 1280, 20.0, self.offset_x)
          self.side = car_side