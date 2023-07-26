import pygame
import os
import random

WIDTH, HEIGHT = 360, 660
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game")

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
WHITE = (255, 255, 255)
BLINDMAN_VEL = 5 # Velocity for blindman
CAR_VEL = 3


COLUMNS = {"LEFT": 25, "MIDDLE" : 155, "RIGHT" : 275}
MAN_COLUMN = [25, 155, 275]

## Frame per second
FPS = 60

BLINDMAN_WIDTH, BLINDMAN_HEIGHT = 50, 50
ROAD_WIDTH, ROAD_HEIGHT = 460, 360
CAR_WIDTH, CAR_HEIGHT = 100, 100
## Images
BLINDMAN_IMAGE = pygame.image.load(
    os.path.join('data', 'assets', 'blindman.png'))
## scaling
BLINDMAN = pygame.transform.scale(BLINDMAN_IMAGE, (BLINDMAN_WIDTH, BLINDMAN_HEIGHT))
CAR = pygame.image.load(
    os.path.join('data', 'assets', 'car.png'))
CAR_IMAGE = pygame.transform.scale(CAR, (CAR_WIDTH, CAR_HEIGHT))
ROAD = pygame.image.load(
    os.path.join('data', 'assets', 'road.png'))
ROAD_IMAGE = pygame.transform.scale(ROAD, (WIDTH,HEIGHT))

def blindman_movement(keys_pressed, blindman):
    if keys_pressed[pygame.K_a]: # LEFT
        blindman.x = MAN_COLUMN[0]
    if keys_pressed[pygame.K_s]:
        blindman.x = MAN_COLUMN[1]
    if keys_pressed[pygame.K_d]: # RIGHT
        blindman.x = MAN_COLUMN[2]

## Input lane_side: LEFT, MIDDLE, RIGHT
def car_movements(lane_side):
     car_x = COLUMNS.get(lane_side)
     car_y = -10
    ## OOP

     pass

def handle_hit(blindman, car):
     
     pass

# drawings, they are squential
def draw_window(blindman):
        WIN.fill(WHITE)
        # coordinates start from top left hand corner
        ## COORDINATES
        WIN.blit(ROAD_IMAGE, (0,0))
        WIN.blit(BLINDMAN, (blindman.x, HEIGHT - BLINDMAN_HEIGHT -30)) ## image, coordinate
        WIN.blit(CAR_IMAGE, (10,10))

        ## SCORE SYSTEM


        pygame.display.update()



def main():
    blindman = pygame.Rect(MAN_COLUMN[1], 10, BLINDMAN_WIDTH, BLINDMAN_HEIGHT)
    pos = 1
    clock = pygame.time.Clock() ## control time
    run = True
    try:
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            
            keys_pressed = pygame.key.get_pressed()
            blindman_movement(keys_pressed, blindman)

            draw_window(blindman)
        pygame.quit()
    except SystemExit:
         pygame.quit()



if __name__ == "__main__":
    main()
