#File for Blind Date game code
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import Stimulation as S

pygame.init()

running = True

while running:
    print("Blind Date game code")
    S.window.blit(toolbar, (0, 0))

    S.manager.draw_ui(window)
    pygame.display.update()