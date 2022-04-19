#File for Blind Date game code
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import Stimulation as S


S.stack.move_window_to_front(S.instruction_window)

S.manager.update(S.time_delta)

print("Blind Date game code")