import sys
import time
import pygame

from src.components.car_side import CarSide
from src.components.incoming_car import Car
from src.components.blind_man import BlindMan
from src.components.scoreboard import Scoreboard

scoreboard = Scoreboard()
## SPRITE SET UP
RC = Car(CarSide.RIGHT)
MC = Car(CarSide.MIDDLE)
LC = Car(CarSide.LEFT)