import random
import pygame

from src.components.car_side import CarSide
from src.services import visualise_service
### ROAD => LEFT, MIDDLE, RIGHT

COLUMNS = {"LEFT": 25, "MIDDLE" : 155, "RIGHT" : 275}
COLUMN = [25, 155, 275]


class Car(pygame.sprite.Sprite):
     def __init__(self, car_side, Carside):
          super().__init__()
          self.new_speed = 2.9
          self.new_y = 0
          self.new_x = 0
          self.side = COLUMN[random.randint(0,2)]

          self._load_car()

     def reset(self):
          self.new_spd = 5
          self.can_score = True
        
          if self.side == CarSide.RIGHT:
            self.offset_x = COLUMNS.get("RIGHT")
            self.new_y = -40
            self.new_x = 0

          if self.side == CarSide.LEFT

          if self.side == CarSide.LEFT:
               self.offset_x = random.randint(-50, 120)
               self.new_y = -320
               self.new_x = 0

     def _load_car(self):
          if self.side == CarSide.RIGHT:
               self._load_right_car()

          if self.side == CarSide.MIDDLE:
               self._load_middle_car()

          if self.side == CarSide.LEFT:
               self._load_left_car()

     def _load_left_car(self):
          self.image = visualise_service.get_car_image()
          self.rect = self.image.get_rect()
          self.mask = pygame.mask.from_surface(self.image)
          self.x = COLUMNS.get("LEFT")
          self.new_y = -320
     
     def _load_middle_car(self):
          self.image = visualise_service.get_car_image()
          self.rect = self.image.get_rect()
          self.mask = pygame.mask.from_surface(self.image)
          self.x = COLUMNS.get("MIDDLE")
          self.new_y = -320

     def _load_right_hand(self):
          self.image = visualise_service.get_car_image()
          self.rect = self.image.get_rect()
          self.mask = pygame.mask.from_surface(self.image)
          self.x = COLUMNS.get("RIGHT")
          self.new_y = -40

     def move(self, player_position):
          self.new_x = sine(100.0, 620, 20.0, self.offset_x)
          self.new_y += self.new_spd
          self.rect.center = (self.new_x, self.new_y)

          # if self.rect.top > player_position.y - 35 and self.can_score:
          #      scoreboard.increase_current_score()
          #      self.can_score = False

          #      MusicService.play_score_sound()

          #      if scoreboard.get_current_score() % 5 == 0:
          #           MusicService.play_cheer_sound()

          if self.rect.top > Config.HEIGHT:
               self.rect.bottom = 0
               # Play Kung Fu Sound
               self.new_spd = random.uniform(0.5, 8)

               if self.side == HandSide.RIGHT:
                    self.offset_x = random.randint(260, 380)
                    self.new_y = -40

               if self.side == HandSide.LEFT:
                    self.offset_x = random.randint(-50, 120)
                    self.new_y = -320

               if self.new_spd >= 6:
                    self.new_spd = 8
                    MusicService.play_chop_sound()

               self.can_score = True

