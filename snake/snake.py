import pygame
import sys
import random


class Game():
    def __init__(self):
        self.screen_width = 400
        self.screen_height = 400
        self.red = pygame.color(255,0,0)
        self.white = pygame.color(255,255,255)
        self.black = pygame.color(0,0,0)
        self.brown = pygame.color(165,42,42)
        self.fps_controller = pygame.time.Clock()
        self.score = 0

    def init_and_check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('OK')

    def set_surface_and_title(self):
        self.playgame










