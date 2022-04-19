#File for Blind Date game code
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import Stimulation as S


S.main_window.change_layer(1)
S.main_window.disable()
S.main_window.visible = False
S.main_window.update(S.time_delta)
S.instruction_window.change_layer(3)
S.instruction_window.visible = True
S.instruction_window.update(S.time_delta)
S.instruction_bg.visible = True
S.instruction_bg.update(S.time_delta)
S.manager.update(S.time_delta)

print("Blind Date game code")