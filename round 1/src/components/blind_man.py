import pygame
from pygame.locals import *

from src.config import Config
from src.services.visualise_service import VisualizationService

vec = pygame.math.Vector2

MAN_COLUMN = [25, 155, 275]

class BlindMan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = VisualizationService.get_player_image()
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.acc = vec(0,0)

        keys_pressed =  pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]: # LEFT
            blindman.x = MAN_COLUMN[0]
        if keys_pressed[pygame.K_s]:
            blindman.x = MAN_COLUMN[1]
        if keys_pressed[pygame.K_d]: # RIGHT
            blindman.x = MAN_COLUMN[2]



    # def draw(self, screen):
    #     screen.blit(VisualizationService.get_santa_hand(), (self.rect.x - 25, self.rect.y - 25))
    #     screen.blit(self.image, self.rect)

    # def reset(self):
    #     self.pos = vec((180, 550))
    #     self.vel = vec(0, 0)
    #     self.acc = vec(0, 0)