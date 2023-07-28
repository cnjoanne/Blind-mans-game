import pygame
import os
import time
import random

pygame.font.init()


WIDTH, HEIGHT = 360, 660
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blind man's game")
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car Velocity
CAR_VEL = 3


## LEFT. MIDDLE, RIGHT
COLUMN = [25, 155, 275]
CAR_COLUMN = [10, 140, 260]


BLINDMAN_WIDTH, BLINDMAN_HEIGHT = 50, 50
ROAD_WIDTH, ROAD_HEIGHT = 1, 660
CAR_WIDTH, CAR_HEIGHT = 100, 100

## Images & Scaling
BLINDMAN = pygame.image.load(
    os.path.join('data', 'assets', 'blindman.png'))
BLINDMAN_IMAGE = pygame.transform.scale(BLINDMAN, (BLINDMAN_WIDTH, BLINDMAN_HEIGHT))
CAR = pygame.image.load(
    os.path.join('data', 'assets', 'car.png'))
CAR_IMAGE = pygame.transform.scale(CAR, (CAR_WIDTH, CAR_HEIGHT))
ROAD = pygame.image.load(
    os.path.join('data', 'assets', 'road.png'))
ROAD_IMAGE = pygame.transform.scale(ROAD, (WIDTH,HEIGHT))


class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obj_img = None
    
    def draw(self, window):
        window.blit(self.obj_img, (self.x, self.y))

    def get_width(self):
        return self.obj_img.get_width()

    def get_height(self):
        return self.obj_img.get_height()


class BlindMan(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.obj_img = BLINDMAN_IMAGE
        self.mask = pygame.mask.from_surface(self.obj_img)

    def draw(self, window):
        super().draw(window)


class Car(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.obj_img = CAR_IMAGE
        self.mask = pygame.mask.from_surface(self.obj_img)

    def move(self, vel):
        self.y += vel

class Veil(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 250
        self.height = 400
        self.color = (0, 0, 0)

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def get_mask(self):
        return pygame.mask.from_surface(self.obj_img)

    def move_randomly(self):
        # Move the Veil randomly around the screen
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(0, HEIGHT - self.height)


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    run = True
    FPS = 60
    lives = 3
    score = 0
    main_font = pygame.font.SysFont("roboto mono", 30)
    lost_font = pygame.font.SysFont("roboto mono", 30)

    car_ls = []
    wave_length = 6 # Number of cars in 1 wave

    blindman = BlindMan(COLUMN[1], 590)

    veil = Veil(COLUMN[1], 0)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(ROAD_IMAGE, (0,0))
        #draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        WIN.blit(lives_label, (5, 5))
        score_label = main_font.render(f"Score: {score}", 1, (255,255,255))
        WIN.blit(score_label, (260, 6))
        
        for cars in car_ls:
            cars.draw(WIN)
        blindman.draw(WIN)
        veil.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost :c", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    veil_change_time = pygame.time.get_ticks()
    veil_move_interval = 1000  # Move the veil in how many seconds

    while run : 
        clock.tick(FPS)
        redraw_window()

        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS *3:
                run = False
            else:
                continue

        if len(car_ls) == 0 :
            for i in range(wave_length):
                car = Car(CAR_COLUMN[random.randint(0,2)], random.randrange(-1500, -100) )
                car_ls.append(car)

        current_time = pygame.time.get_ticks()
        if current_time - veil_change_time >= veil_move_interval:
            veil.move_randomly()
            veil_change_time = current_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]: #LEFT
            blindman.x = COLUMN[0]
        if keys_pressed[pygame.K_s]: #MIDDLE
            blindman.x = COLUMN[1]
        if keys_pressed[pygame.K_d]: # RIGHT
            blindman.x = COLUMN[2]

        for cars in car_ls[:]:
            cars.move(CAR_VEL)
            
            if collide(cars, blindman):
                lives -= 1
                car_ls.remove(cars)
            elif cars.y + cars.get_height() > HEIGHT:
                 score += 1
                 car_ls.remove(cars)

def main_menu():
    title_font = pygame.font.SysFont("roboto mono", 30)
    run = True
    while run:
        WIN.blit(ROAD_IMAGE, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, WHITE)
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


    

if __name__ =="__main__":
    main_menu()