import pygame
import os

WIDTH, HEIGHT = 300,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game")

WHITE = (255, 255, 255)

## Frame per second
FPS = 60

BLINDMAN_HEIGHT, BLINDMAN_WIDTH = 3, 5
## Images
BLINDMAN_IMAGE = pygame.image.load(
    os.path.join('data', 'assets', 'blindman.png'))
## scaling
BLINDMAN = pygame.transform.rotate(pygame.transform.scale(BLINDMAN_IMAGE, (BLINDMAN_HEIGHT, BLINDMAN_WIDTH)), 90) # image, width by height || angle rotate
CAR_IMAGE = pygame.image.load(
    os.path.join('data', 'assets', 'car.png'))
ROAD_IMAGE = pygame.image.load(
    os.path.join('data', 'assets', 'road.png'))

# drawings, they are squential
def draw_window():
        WIN.fill(WHITE)
        # coordinates start from top left hand corner
        WIN.blit(BLINDMAN, (0,0)) ## image, coordinate
        pygame.display.update()




def main():
    clock = pygame.time.Clock() ## control time 
    run = True
    while run:
        clock.tick(FPS)

        draw_window()

if __name__ == "main":
    main()
