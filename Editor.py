#File for Editor game code
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import random

sentence = [["There is some good in this world, and it’s worth fighting for."],
            ["It is only with the heart that one can see rightly; what is essential is invisible to the eye."]]

#initializing the arrays and strings used to parse
sentence_array = []
word_array = []
letter_array = []
word_string = ""
jumble_string = ""
letter_string = ""

sentence_array = random.choice(sentence)
print(sentence_array[0])
word_array = str.split(sentence_array[0])
word_string = random.choice(word_array)

while len(word_string)>8:
    word_string = random.choice(word_array)
while len(word_string)<3:
    word_string = random.choice(word_array)

original = word_string
print(word_string)
for character in word_string:
    if character.isalpha() == False:
        word_string = word_string.replace(character, "")

correct = word_string
print(word_string)

while word_string:
    position = random.randrange(len(word_string))
    jumble_string += word_string[position]
    word_string = word_string[:position] + word_string[(position + 1):]

while correct == jumble_string:
    jumble_string = ""
    word_string = correct
    while word_string:
        position = random.randrange(len(word_string))
        jumble_string += word_string[position]
        word_string = word_string[:position] + word_string[(position + 1):]

sentence_array = list(map(lambda word_string: word_string.replace(original, jumble_string), sentence_array))

print(sentence_array)
print("The jumble is: ")
print(jumble_string)
    