import pygame
import os

WIDTH, HEIGHT = 485,740
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game")

WHITE = (255, 255, 255)


## Frame per second
FPS = 60

BLINDMAN_WIDTH, BLINDMAN_HEIGHT = 100,  120
ROAD_WIDTH, ROAD_HEIGHT = 460, 360
CAR_WIDTH, CAR_HEIGHT = 100, 100
## Images
BLINDMAN_IMAGE = pygame.image.load(
    os.path.join('data', 'assets', 'blindman.png'))
## scaling
BLINDMAN = pygame.transform.rotate(pygame.transform.scale(BLINDMAN_IMAGE, (BLINDMAN_HEIGHT, BLINDMAN_WIDTH)), 90) # image, width by height || angle rotate
CAR_IMAGE = pygame.image.load(
    os.path.join('data', 'assets', 'car.png'))
ROAD_IMAGE = pygame.image.load(
    os.path.join('data', 'assets', 'road.png'))

def blindman_movement(key_pressed, blindman):
     pass


# drawings, they are squential
def draw_window():
        WIN.fill(WHITE)
        # coordinates start from top left hand corner
        WIN.blit(ROAD_IMAGE, (0,0))
        # WIN.blit(ROAD_IMAGE)
        WIN.blit(BLINDMAN, (0,0)) ## image, coordinate
        WIN.blit(CAR_IMAGE, (10,10))
        pygame.display.update()




def main():
    clock = pygame.time.Clock() ## control time 
    run = True

    try: 
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            draw_window()
            pygame.display.update()
        pygame.quit()
    except SystemExit:
         pygame.quit()
    


if __name__ == "__main__":
    main()
