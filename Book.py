#File for Bookworm game code
import os
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import random
import urllib.request

<<<<<<< Updated upstream
pygame.init()

pygame.display.set_caption("Stimulation")
window = pygame.display.set_mode()

cwd = os.getcwd()
manager = pygui.UIManager((S.x, S.y), cwd + "/menu_theme.json")
manager.get_theme().load_theme('panel.json')

game_window = pygui.elements.UIWindow(rect=pygame.Rect(x2, y2, 800, 600),
                            manager=manager,
                            window_display_title='Bookworm',
                            resizable=False)

game_bg = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        container=game_window,
                                        starting_layer_height=1,
                                        object_id=ObjectID(class_id='@game_panel'))

game_toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                container=game_window,
                                object_id=ObjectID(class_id='@toolbar'))

text_entry = pygui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 200), (400, 50)),
                                        manager=manager,
                                        container=game_bg)
text_entry.set_allowed_characters('letters')

letter_button1 = pygui.elements.UIButton(relative_rect=pygame.Rect((100, 75), (50, 50)),
                                            text="",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

letter_button2 = pygui.elements.UIButton(relative_rect=pygame.Rect((175, 75), (50, 50)),
                                            text="",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

letter_button3 = pygui.elements.UIButton(relative_rect=pygame.Rect((250, 75), (50, 50)),
                                            text="",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

letter_button4 = pygui.elements.UIButton(relative_rect=pygame.Rect((325, 75), (50, 50)),
                                        text="",
                                        manager=manager,
                                        container=game_bg,
                                        visible=False,
                                        object_id=ObjectID(class_id='@game_menu_buttons'))

letter_button5 = pygui.elements.UIButton(relative_rect=pygame.Rect((400, 75), (50, 50)),
                                        text="",
                                        manager=manager,
                                        container=game_bg,
                                        visible=False,
                                        object_id=ObjectID(class_id='@game_menu_buttons'))

def get_jumble():

    text_entry.set_text("")

    letter_button1.visible = False
    letter_button2.visible = False
    letter_button3.visible = False
    letter_button4.visible = False
    letter_button5.visible = False
=======
jumble_list=[]
def get_jumble(x):
>>>>>>> Stashed changes

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
            print("Loading...")
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

# guess = input("Your guess: ")
# while guess != correct and guess != "":
#     print("Sorry, that's not it")
#     guess = input("Your guess: ")

# if guess != "":
#     print("Correct!")
# print("Thanks for playing")

# input("\n\nPress the enter key to exit")
