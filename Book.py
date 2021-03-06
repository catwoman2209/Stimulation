#File for Bookworm game code
#
#TTU Capstone Project Spring 2022
#@authors = catwoman2209 - Christiana Taylor

########################### NOTES ##############################

# Bugs:
# generated word contains an apostrophe
# -results in an infinite loop as apostrophes cannot be entered

########################### END OF NOTES #######################

import os
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import random
import urllib.request


jumble_list=[]
def get_jumble(x):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    req = urllib.request.Request(word_url, headers=headers)
    response = urllib.request.urlopen(req)
    long_txt = response.read().decode()
    WORDS = long_txt.splitlines()

    list = [word for word in WORDS if word[0].islower()]

    #ensures word is between 3 and 5 letters long
    word = random.choice(list)
    while (len(word)>5):
        word = random.choice(list)

    while (len(word)<3):
        word = random.choice(list)

    #jumble word array
    correct = word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    count = 0
    for i in jumble:
        count+=1
        x.append(i)

    print("The jumble is: ")
    print(x)

    #returns correct answer
    return correct

def main():
    return get_jumble(jumble_list)
