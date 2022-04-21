#File for Bookworm game code
import os
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import random
import urllib.request

################ NOTES ##############################

# Bugs:
# generated word will be out of index range when copying onto buttons
# -will result in closure of application
# generated word contains an apostrophe
# -results in an infinite loop as apostrophes cannot be entered

################ END OF NOTES #######################


jumble_list=[]
def get_jumble(x):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    req = urllib.request.Request(word_url, headers=headers)
    response = urllib.request.urlopen(req)
    long_txt = response.read().decode()
    WORDS = long_txt.splitlines()

    list = [word for word in WORDS if word[0].islower()]

    word = random.choice(list)
    while (len(word)>5):
        if (len(word)<=2):
            word = random.choice(list)
        else:
            word = random.choice(list)

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

    return correct

def main():
    return get_jumble(jumble_list)
