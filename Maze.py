#File for Maze Runner game code
#
#TTU Capstone Project Spring 2022
#@authors = perennat - Tanner Kellogg

import os
import pygame


PLAYER_MODEL = pygame.image.load(os.path.join("assets", "maze_sprite.png"))
ERASE_MODEL = pygame.image.load(os.path.join("assets", "maze_erase.png"))
BREADCRUMB_MODEL = pygame.image.load(os.path.join("assets", "maze_breadcrumb.png"))
class Player:
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.window = window

    def draw(self):
        self.window.blit(PLAYER_MODEL, (self.x, self.y))
    def erase(self):
        self.window.blit(ERASE_MODEL, (self.x, self.y))
    def leave_breadcrumb(self, b_x, b_y):
        self.window.blit(BREADCRUMB_MODEL, (b_x, b_y))
