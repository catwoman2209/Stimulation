#File for Editor game code
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import random

sentence=[['There', 'is', 'some', 'good', 'in', 'this', 'world,', 'and', "it's", 'worth', 'fighting', 'for.'],
        ['It', 'is', 'only', 'with', 'the', 'heart', 'that', 'one', 'can', 'see', 'rightly;', 'what', 'is', 'essential', 'is', 'invisible', 'to', 'the', 'eye.'],
        ['I', 'am', 'no', 'bird;', 'and', 'no', 'net', 'ensnares', 'me:', 'I', 'am', 'a', 'free', 'human', 'being', 'with', 'an', 'independent', 'will,' 'which', 'I', 'now', 'exert', 'to', 'leave', 'you.']]
a = []

a = (random.choice(sentence))
print(a)