import pygame

from PATH import AUDIO_DIR

class MusicService:  
    @staticmethod
    def play_car_center_honk():
        honk = pygame.mixer.Sound(AUDIO_DIR/"car_horn.mp3")
        pygame.mixer.Sound.play(honk)
    
    @staticmethod
    def play_car_left_honk():
        honk = pygame.mixer.Sound(AUDIO_DIR/"car_horn_left.mp3")
        pygame.mixer.Sound.play(honk)

    @staticmethod
    def play_car_right_honk():
        honk = pygame.mixer.Sound(AUDIO_DIR/"car_horn_right.mp3")
        pygame.mixer.Sound.play(honk)

    @staticmethod
    def play_car_far_left_honk():
        honk = pygame.mixer.Sound(AUDIO_DIR/"car_horn_left_further.mp3")
        pygame.mixer.Sound.play(honk)

    @staticmethod
    def play_car_far_right_honk():
        honk = pygame.mixer.Sound(AUDIO_DIR/"car_horn_right_further.mp3")
        pygame.mixer.Sound.play(honk)

    @staticmethod
    def play_injured():
        injured = pygame.mixer.Sound(AUDIO_DIR/"hurt.mp3")
        pygame.mixer.Sound.play(injured)

    @staticmethod
    def start_background_music():
        if pygame.mixer.music.get_busy():
            return

        pygame.mixer.music.load(AUDIO_DIR/"background_road.mp3")
        pygame.mixer.music.play()