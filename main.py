import pygame
import os
import time
import random
from pygame import mixer


pygame.font.init()
mixer.init()

WIDTH, HEIGHT = 360, 660
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blind man's game")
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Car Velocity
CAR_VEL = 4.5


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
    def __init__(self, x, y, lane):
        super().__init__(x, y)
        self.obj_img = CAR_IMAGE
        self.mask = pygame.mask.from_surface(self.obj_img)
        self.lane = lane  # Store the lane where the car spawns

        # Load the appropriate sound based on the lane
        if self.lane == 0:
            self.spawn_sound = pygame.mixer.Sound("./data/audio/car_horn_right.mp3")
        elif self.lane == 1:
            self.spawn_sound = pygame.mixer.Sound("./data/audio/car horn.mp3")
        elif self.lane == 2:
            self.spawn_sound = pygame.mixer.Sound("./data/audio/car_horn_left.mp3")

        self.sound_played = False

    def play_spawn_sound(self):
        if not self.sound_played:
            self.spawn_sound.play()
            self.sound_played = True
    
    def has_crossed_line(self, line_y):
        return self.y > line_y

    def move(self, vel):
        self.y += vel

class Veil(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 270
        self.height = 400
        self.color = (0, 0, 0)
        self.obj_img = pygame.Surface((self.width, self.height))
        self.last_shape_change_time = pygame.time.get_ticks()
        self.shape_change_interval = 2000 
        self.max_y = 30  # Maximum height limit for the veil

    def draw(self, window):
        if self.should_change_shape():
            self.update_shape()
        self.adjust_position()
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def should_change_shape(self):
        # Check the time before shape change
        current_time = pygame.time.get_ticks()
        return current_time - self.last_shape_change_time >= self.shape_change_interval
    
    def update_shape(self):
        # Randomly update the width and height of the veil
        self.width = random.randint(240, 300)
        self.height = random.randint(350, 500)
        self.obj_img = pygame.Surface((self.width, self.height))
        self.obj_img.fill(self.color)
        self.last_shape_change_time = pygame.time.get_ticks()

    def adjust_position(self):
        # Check if the veil's y position exceeds the maximum limit
        if self.y < self.max_y:
            self.y = self.max_y

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
    wave_length = 7 # Number of cars in 1 wave

    blindman = BlindMan(COLUMN[1], 590)

    veil = Veil(COLUMN[1], 0)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def road_background():
        mixer.music.load("data/audio/traffic_sound.mp3")
        mixer.music.set_volume(1.3)
        mixer.music.play()

    def redraw_window():
        WIN.blit(ROAD_IMAGE, (0,0))

        #draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, WHITE)
        WIN.blit(lives_label, (5, 5))

        score_label = main_font.render(f"Score: {score}", 1, WHITE)
        WIN.blit(score_label, (260, 6))

        
        for cars in car_ls:
            cars.draw(WIN)
        blindman.draw(WIN)
        veil.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost :c", 1, WHITE)
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    veil_change_time = pygame.time.get_ticks()
    veil_move_interval = 2000  # Move the veil in how many seconds

    while run : 
        clock.tick(FPS)
        redraw_window()
        road_background()

        sound_line_y = 200

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
                CAR_COL_IND = random.randint(0,2)
                car = Car(CAR_COLUMN[CAR_COL_IND], random.randrange(-1500, -100), CAR_COL_IND)
                car_ls.append(car)

        current_time = pygame.time.get_ticks()
        if current_time - veil_change_time >= veil_move_interval:
            veil.move_randomly()
            veil_change_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
        keys_pressed = pygame.key.get_pressed()
        # BLINDMAN_VEL = 5
        # if keys_pressed[pygame.K_a] and blindman.x - BLINDMAN_VEL > 0 : #LEFT
        #     blindman.x -= BLINDMAN_VEL
        # if keys_pressed[pygame.K_d] and blindman.x + BLINDMAN_VEL + blindman.get_width() < WIDTH: #RIGHT
        #     blindman.x += BLINDMAN_VEL
            
        if keys_pressed[pygame.K_a]: #LEFT
            blindman.x = COLUMN[0]
        if keys_pressed[pygame.K_s]: #MIDDLE
            blindman.x = COLUMN[1]
        if keys_pressed[pygame.K_d]: # RIGHT
            blindman.x = COLUMN[2]

        for cars in car_ls[:]:
            cars.move(CAR_VEL)
        
            if cars.has_crossed_line(sound_line_y) and not cars.sound_played:
                cars.play_spawn_sound()
                cars.sound_played = True

            if collide(cars, blindman):
                lives -= 1
                hurt = pygame.mixer.Sound("data/audio/hurt.mp3")
                pygame.mixer.Sound.play(hurt)
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