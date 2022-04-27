#File for Paint Picker game code
#
#TTU Capstone Project Spring 2022
#@authors = christiana_taylor

import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import random

def get_paint_color():
    colors=["black", "white", "red", "blue", "yellow", "gray", "green", "purple"]
    choice = colors[random.randint(0,7)]
    print(choice)
    return choice 

def get_paint_word(x):
    colors=["black", "white", "red", "blue", "yellow", "gray", "green", "purple"]
    colors.remove(x)
    choice = colors[random.randint(0,6)]
    print(choice)
    return choice

def get_paint_word_color(x, y):
    colors=["black", "white", "red", "blue", "yellow", "gray", "green", "purple"]
    colors.remove(x)
    colors.remove(y)

    choice = random.choice(colors)
    value = (0, 0, 0)

    if choice == "black":
        value = (0,0,0)
    if choice == "white":
        value = (255, 255, 255)
    if choice == "red":
        value = (255, 0, 0)
    if choice == "blue":
        value = (0, 0, 255)
    if choice == "yellow":
        value = (255, 255, 0)
    if choice == "gray":
        value = (128, 128, 128)
    if choice == "green":
        value = (0, 128, 0)
    if choice == "purple":
        value = (128, 0, 128)
    print(choice)
    return value