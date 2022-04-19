#File for Blind Date game code
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import Stimulation as S

S.main_bg.visible = False
S.main_bg.update(S.time_delta)
S.main_toolbar.visible = False
S.main_toolbar.update(S.time_delta)
S.main_window.disable()
S.main_window.visible = False
S.main_window.update(S.time_delta)
S.instruction_window.visible = True
S.instruction_window.update(S.time_delta)
S.stack.move_window_to_front(S.instruction_window)
S.instruction_bg.visible = True
S.instruction_bg.update(S.time_delta)
S.manager.update(S.time_delta)

print("Blind Date game code")