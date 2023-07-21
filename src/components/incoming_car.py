import random
import pygame

from src.components.car_side import CarSide
### ROAD => LEFT, MIDDLE, RIGHT

class Car(pygame.sprite.Sprite):
     def __init__(self, car_side, Carside):
          super().__init__()