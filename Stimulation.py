#Main file for execution
#
#TTU Capstone Project Spring 2022
#@authors = catwoman2209 - Christiana Taylor (main)
#           perennat - Tanner Kellogg
#           SeanCris - Sean Criswell

import os
import pygame
import pygame.font
import pygame_gui as pygui
from pygame_gui.core import ObjectID
from typeracer import Game
import random
import Book
import Editor
import Maze
import Paint
import Change

pygame.init()

pygame.display.set_caption("Stimulation")
window = pygame.display.set_mode()

x = window.get_width()
y = window.get_height()

cwd = os.getcwd()
manager = pygui.UIManager((x, y), cwd + "/menu_theme.json")
manager.get_theme().load_theme('panel.json')
manager.get_theme().load_theme('label.json')
manager.get_theme().load_theme('text_box.json')

x2 = x/2 - 400
y2 = y/2 - 300

################ CONSTANT ELEMENTS/WINDOWS #######################

#panels and windows for Stimulation
window2 = pygui.elements.UIWindow(rect=pygame.Rect(0, 0, x, y),
                            manager=manager,
                            window_display_title='Stimulation',
                            resizable=False,
                            visible=False)

stack = pygui.core.ui_window_stack.UIWindowStack(window_resolution=(x,y), root_container=window2) 

main_window = pygui.elements.UIWindow(rect=pygame.Rect(x2, y2, 800, 600),
                            manager=manager,
                            window_display_title='Main Menu',
                            resizable=False)
instruction_window = pygui.elements.UIWindow(rect=pygame.Rect(x2, y2, 800, 600),
                                            manager=manager,
                                            window_display_title='Instruction Menu',
                                            resizable=False)
game_window = pygui.elements.UIWindow(rect=pygame.Rect(x2, y2, 800, 600),
                            manager=manager,
                            window_display_title='Bookworm',
                            resizable=False)
maze_window = pygui.elements.UIWindow(rect=pygame.Rect(x2, y2, 800, 600),
                            manager=manager,
                            window_display_title='Maze Runner',
                            resizable=False)

#add windows to stack
stack.add_new_window(maze_window)
stack.add_new_window(main_window)
stack.add_new_window(instruction_window)
stack.add_new_window(game_window)
stack.move_window_to_front(main_window)

#constant background panels and toolbars
main_bg = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        container=main_window,
                                        starting_layer_height=1,
                                        object_id=ObjectID(class_id='@main_panel'))
instruction_bg = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        container=instruction_window,
                                        starting_layer_height=1,
                                        object_id=ObjectID(class_id='@instruction_panel'))
game_bg = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        container=game_window,
                                        starting_layer_height=1,
                                        object_id=ObjectID(class_id='@game_panel'))
maze_bg = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        container=maze_window,
                                        starting_layer_height=1,
                                        object_id=ObjectID(class_id='@game_panel'))
main_toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                container=main_window,
                                object_id=ObjectID(class_id='@toolbar'))
stimulation_main_label = pygui.elements.UILabel(relative_rect=pygame.Rect((300, 0), (200, 50)),
                                                text="STIMULATION",
                                                manager=manager,
                                                container=main_toolbar,
                                                visible=True, 
                                                object_id=ObjectID(class_id="@main_label"))
instruction_toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                container=instruction_window,
                                object_id=ObjectID(class_id='@toolbar'))
stimulation__inst_label = pygui.elements.UILabel(relative_rect=pygame.Rect((300, 0), (200, 50)),
                                                text="STIMULATION",
                                                manager=manager,
                                                container=instruction_toolbar,
                                                visible=True, 
                                                object_id=ObjectID(class_id="@main_label"))
game_toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                container=game_window,
                                object_id=ObjectID(class_id='@toolbar'))
maze_toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                container=maze_window,
                                object_id=ObjectID(class_id='@toolbar'))

#function for updating instruction_textbox
def instruction_text(x):
    text = ""
    if x == 1:
        text =  "<b>Blind Date</b><br><br>You went on a blind date that went great! Memorize their number to call them later!<br><br><br>This game may help those with Alzheimer’s to improve symptoms with continued use over time."

    elif x == 2:
        text =  "<b>Bookworm</b><br><br>Are you a bookworm? Use the letters to find the word matching the definition<br><br><br>This game may help those with dyslexia to improve symptoms with continued use over time."
    
    elif x == 3:
        text =  "<b>Editor</b><br><br>This author needs your help! Find and unscramble the author's errors as fast as you can!<br>Note: Do not include punctuation of any kind.<br><br><br>This game may help those with dyslexia to improve symptoms with continued use over<br>time."
    
    elif x == 4:
        text =  "<b>Find the Kiddo</b><br><br>Listen to the sound of the toddler's giggles as they run through the house,<br>and follow their path!<br><br><br>This game may help those with ADHD to improve symptoms with continued use over time."
    
    elif x == 5:
        text =  "<b>Maze Runner</b><br><br>Find the way out as quickly as you can!<br><br><br>This game may help those with ADHD to improve symptoms with continued use over time."
    
    elif x == 6:
        text =  "<b>Paint Picker</b><br><br>Your partner needs help painting! Memorize the color you <em>see</em> in the background,<br>not the color you read!<br><br><br>This game may help those with ADHD or Alzheimer’s to improve symptoms with continued use<br>over time."
    
    elif x == 7:
        text =  "<b>Quick Change</b><br><br>Customers want their change in this fast paced subtraction cafe!<br><br><br>This game may help those with ADHD to improve symptoms with continued use over time."
    
    elif x == 8:
        text =  "<b>Space Oddity</b><br><br>Choose the odd alien out in this space-themed problem solving game!<br><br><br>This game may help those with ADHD to improve symptoms with continued use over time." 
 
    else:
        text =  "<b>Type Racer</b><br><br>Test your typing skills in this race against time!<br><br><br>This game may help those with dyslexia to improve symptoms with continued use over time."

    return text
def wait():
    pygame.time.wait(5000)

################ MAIN MENU ELEMENTS #######################

blind_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((90, 100), (200, 100)),
                                            text='Blind Date',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
book_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((300, 100), (200, 100)),
                                            text='Bookworm',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
editor_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((510, 100), (200, 100)),
                                            text='Editor',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
kiddo_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((90, 210), (200, 100)),
                                            text='Find the Kiddo',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
maze_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((300, 210), (200, 100)),
                                            text='Maze Runner',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
paint_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((510, 210), (200, 100)),
                                            text='Paint Picker',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
change_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((90, 320), (200, 100)),
                                            text='Quick Change',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
space_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((300, 320), (200, 100)),
                                            text='Space Oddity',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
racer_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((510, 320), (200, 100)),
                                            text='Type Racer',
                                            manager=manager,
                                            container=main_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
back_button = pygui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                            text='Back',
                                            manager=manager,
                                            container=instruction_toolbar,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
back_game_button = pygui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (150, 50)),
                                            text='Quit Game',
                                            manager=manager,
                                            container=game_toolbar,
                                            tool_tip_text="Back to instruction screen",
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
play_button = pygui.elements.UIButton(relative_rect=pygame.Rect((350, 400), (100, 50)),
                                            text='PLAY',
                                            manager=manager,
                                            container=instruction_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
quit_button = pygui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                            text='QUIT',
                                            manager=manager,
                                            container=main_toolbar,
                                            tool_tip_text="Quit Stimulation",
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

################ BOOKWORM GAME ELEMENTS #######################
#@authors=catwoman2209 - Christiana Taylor

#Bookworm buttons
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

#Bookworm text entry lines
bookworm_text_entry = pygui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 200), (400, 50)),
                                        manager=manager,
                                        visible=False,
                                        container=game_bg)
bookworm_text_entry.set_allowed_characters('letters')

#Bookworm labels
bookworm_label_feedback1 = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (100, 50)),
                                                text="Correct!",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
bookworm_label_feedback2 = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (250, 50)),
                                                text="Incorrect! Please try again!",
                                                manager=manager,
                                                container=game_bg, 
                                                visible = False,
                                                object_id=ObjectID(class_id="@bookworm_label"))
bookworm_label_score = pygui.elements.UILabel(relative_rect=pygame.Rect((300, 10), (200, 30)),
                                                text="",
                                                manager=manager,
                                                container=instruction_bg, 
                                                visible = True,
                                                object_id=ObjectID(class_id="@bookworm_label"))

#Bookworm functions
def set_Bookworm():
    bookworm_text_entry.set_text("")
    bookworm_text_entry.visible = True
    bookworm_text_entry.enable()

    letter_button1.visible = False
    letter_button2.visible = False
    letter_button3.visible = False
    letter_button4.visible = False
    letter_button5.visible = False

    letter_button1.set_text(Book.jumble_list[0])
    letter_button2.set_text(Book.jumble_list[1])
    letter_button3.set_text(Book.jumble_list[2])
    letter_button1.visible = True
    letter_button2.visible = True
    letter_button3.visible = True

    if (len(Book.jumble_list) > 3):

        letter_button4.set_text(Book.jumble_list[3]) 
        letter_button4.visible = True

    if (len(Book.jumble_list) > 4):

        letter_button5.set_text(Book.jumble_list[4]) 
        letter_button5.visible = True
def end_Bookworm():
    try:
      score = round((accuracy/iteration)*100)
    except:
      score = 0

    string = "Accuracy: "+ str(score)+" "+str(accuracy)+"/"+str(iteration)

    bookworm_text_entry.visible = False
    bookworm_text_entry.disable()
    bookworm_label_feedback1.visible = False
    bookworm_label_feedback2.visible = False
    bookworm_label_score.set_text(string)
    bookworm_label_score.visible = True

    letter_button1.visible = False
    letter_button2.visible = False
    letter_button3.visible = False
    letter_button4.visible = False
    letter_button5.visible = False
    stack.move_window_to_front(instruction_window)

################ BLIND DATE GAME ELEMENTS #######################
#@authors=catwoman2209 - Christiana Taylor

#Blind Date panel
blind_bg = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        container=game_window,
                                        starting_layer_height=1,
                                        visible=False,
                                        object_id=ObjectID(class_id='@blind_panel'))

#Blind Date text entry lines
blind_text_entry = pygui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 200), (400, 50)),
                                        manager=manager,
                                        container=blind_bg)
blind_text_entry.set_allowed_characters('numbers')

#Blind Date labels
blind_label_number = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 50), (100, 50)),
                                                text="",
                                                manager=manager,
                                                container=blind_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@blind_label_number"))
blind_label_feedback1 = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (100, 50)),
                                                text="Correct!",
                                                manager=manager,
                                                container=blind_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@blind_label"))
blind_label_feedback2 = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (250, 50)),
                                                text="Incorrect! Please try again!",
                                                manager=manager,
                                                container=blind_bg, 
                                                visible = False,
                                                object_id=ObjectID(class_id="@blind_label"))
blind_label_score = pygui.elements.UILabel(relative_rect=pygame.Rect((300, 10), (200, 30)),
                                                text="",
                                                manager=manager,
                                                container=instruction_bg, 
                                                visible = False)

#Blind Date functions
def get_number():
    return random.randint(10000, 99999)
def set_Blind():
    blind_label_number.visible = True
    blind_text_entry.visible = False
    manager.update(time_delta)
    pygame.display.update()
    wait()
    blind_label_number.visible = False
    blind_text_entry.visible = True    
def end_Blind():
    try:
      score = round((accuracy/iteration)*100)
    except:
      score = 0

    string = "Accuracy: "+ str(score)+" "+str(accuracy)+"/"+str(iteration)

    blind_text_entry.visible = False
    blind_label_number.visible = False
    blind_label_feedback1.visible = False
    blind_label_feedback2.visible = False
    blind_label_score.set_text(string)
    blind_label_score.visible = True
    blind_bg.visible = False
    game_bg.visible = True

    manager.update(time_delta)
    stack.move_window_to_front(instruction_window)

################ EDITOR GAME ELEMENTS #######################
#@authors=catwoman2209 - Christiana Taylor

#Editor panel
editor_bg = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        container=game_window,
                                        starting_layer_height=1,
                                        visible=False,
                                        object_id=ObjectID(class_id='@editor_panel'))

#Editor text entry lines
editor_text_entry = pygui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 200), (400, 50)),
                                        manager=manager,
                                        visible=False,
                                        container=editor_bg)
editor_text_entry.set_allowed_characters('letters')

#Editor elements
editor_textbox_sentence = pygui.elements.UITextBox(html_text="",
                                        relative_rect=pygame.Rect((50, 25), (700, 75)),
                                        manager=manager,
                                        visible=False,
                                        container=editor_bg,
                                        object_id=ObjectID(class_id='@editor_textbox'))
editor_textbox_sentence_j = pygui.elements.UITextBox(html_text="",
                                        relative_rect=pygame.Rect((50, 100), (700, 75)),
                                        manager=manager,
                                        visible=False,
                                        container=editor_bg,
                                        object_id=ObjectID(class_id='@editor_textbox'))
editor_label_feedback1 = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (100, 50)),
                                                text="Correct!",
                                                manager=manager,
                                                container=editor_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@editor_label"))
editor_label_feedback2 = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (250, 50)),
                                                text="Incorrect! Please try again!",
                                                manager=manager,
                                                container=editor_bg, 
                                                visible = False,
                                                object_id=ObjectID(class_id="@editor_label"))
editor_label_score = pygui.elements.UILabel(relative_rect=pygame.Rect((300, 10), (200, 30)),
                                                text="",
                                                manager=manager,
                                                container=instruction_bg, 
                                                visible = False)

#Editor game functions
def set_Editor():
    editor_textbox_sentence.clear_text_surface()
    editor_textbox_sentence_j.clear_text_surface()
    editor_textbox_sentence.full_redraw()
    editor_textbox_sentence_j.full_redraw()
    editor_textbox_sentence.visible = True
    editor_textbox_sentence_j.visible = True
    editor_text_entry.set_text("")
    editor_text_entry.visible = True
    manager.update(time_delta)
    pygame.display.update()
def end_Editor():
    try:
      score = round((accuracy/iteration)*100)
    except:
      score = 0

    string = "Accuracy: "+ str(score)+" "+str(accuracy)+"/"+str(iteration)

    editor_textbox_sentence.clear_text_surface()
    editor_textbox_sentence_j.clear_text_surface()
    editor_textbox_sentence.visible = False
    editor_textbox_sentence_j.visible = False
    editor_text_entry.visible = False
    editor_label_feedback1.visible = False
    editor_label_feedback2.visible = False
    editor_label_score.set_text(string)
    editor_label_score.visible = True
    editor_bg.visible = False
    game_bg.visible = True

    manager.update(time_delta)
    pygame.display.update()
    stack.move_window_to_front(instruction_window)

################ FIND THE KIDDO GAME ELEMENTS #######################
#@authors=

################ MAZE RUNNER GAME ELEMENTS #######################
#@authors=perennat - Tanner Kellogg

maze_game_slider = pygui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((200,200), (400, 100)),
                                    manager=manager, start_value = 16, value_range = [4,32],
                                    container=maze_bg, click_increment = 1,
                                    object_id=ObjectID(class_id='@toolbar'))
maze_label_slider_title = pygui.elements.UILabel(relative_rect=pygame.Rect((200, 150), (100, 50)),
                                                text="16x16 Maze",
                                                manager=manager,
                                                container=maze_bg,
                                                visible=True, 
                                                object_id=ObjectID(class_id="@maze_label"))
maze_back_game_button = pygui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (150, 50)),
                                            text='Back',
                                            manager=manager,
                                            container=maze_toolbar,
                                            tool_tip_text="Back to instruction screen",
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
maze_play_button = pygui.elements.UIButton(relative_rect=pygame.Rect((350, 400), (100, 50)),
                                            text='Play',
                                            manager=manager,
                                            container=maze_bg,
                                            tool_tip_text="Play Game",
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

#Maze Runner Functions
maze = []
visited_squares = []
maze_stack = []
w = 20
def build_maze(size):
    maze_y = 0
    for i in range(1,size+1):
        maze_x = 20
        maze_y += 20
        for j in range(1, size+1):
            #top of cell
            pygame.draw.line(window, (255,255,255), [maze_x, maze_y], [maze_x + w, maze_y])
            #right of cell
            pygame.draw.line(window, (255,255,255), [maze_x + w, maze_y], [maze_x + w, maze_y + w])
            #bottom of cell
            pygame.draw.line(window, (255,255,255), [maze_x + w, maze_y + w], [maze_x, maze_y + w])
            #left of cell
            pygame.draw.line(window, (255,255,255), [maze_x, maze_y + w], [maze_x, maze_y])
            maze.append((maze_x,maze_y))
            maze_x += 20

#Backtracking algorithm as per wikipedia 
def go_up(maze_x, maze_y):
    pygame.draw.rect(window, (0,0,0), (maze_x + 1, maze_y - w + 1, 19, 39), 0)
    pygame.display.update()
def go_down(maze_x, maze_y):
    pygame.draw.rect(window, (0,0,0), (maze_x +  1, maze_y + 1, 19, 39), 0)
    pygame.display.update()
def go_left(maze_x, maze_y):
    pygame.draw.rect(window, (0,0,0), (maze_x - w +1, maze_y +1, 39, 19), 0)
    pygame.display.update()
def go_right(maze_x, maze_y):
    pygame.draw.rect(window, (0,0,0), (maze_x +1, maze_y +1, 39, 19), 0)
    pygame.display.update()

def create_maze(maze_x, maze_y):
    maze_stack.append((maze_x, maze_y))
    visited_squares.append((maze_x, maze_y))
    while len(maze_stack) > 0:
        possible_moves = [] #0 - up, 1 - right, 2 - down, 3 - left
        if (maze_x, maze_y - w) not in visited_squares and (maze_x , maze_y - w) in maze:
            possible_moves.append(0)
        if (maze_x + w, maze_y) not in visited_squares and (maze_x + w, maze_y) in maze:
            possible_moves.append(1)
        if (maze_x , maze_y + w) not in visited_squares and (maze_x , maze_y + w) in maze:
            possible_moves.append(2)
        if (maze_x - w, maze_y) not in visited_squares and (maze_x - w, maze_y) in maze:
            possible_moves.append(3)
        if len(possible_moves) > 0:
            move = random.choice(possible_moves)
            if move == 0:
                go_up(maze_x, maze_y)
                maze_y -= w
                visited_squares.append((maze_x, maze_y))
                maze_stack.append((maze_x, maze_y))
            elif move == 1:
                go_right(maze_x, maze_y)
                maze_x += w
                visited_squares.append((maze_x, maze_y))
                maze_stack.append((maze_x, maze_y))
            elif move == 2:
                go_down(maze_x, maze_y)
                maze_y += w
                visited_squares.append((maze_x, maze_y))
                maze_stack.append((maze_x, maze_y))
            elif move == 3:
                go_left(maze_x, maze_y)
                maze_x -= w
                visited_squares.append((maze_x, maze_y))
                maze_stack.append((maze_x, maze_y))
        else:
            maze_x, maze_y = maze_stack.pop()
        pygame.draw.rect(window, (193, 225, 193), (21,21, 19, 19), 0)
    
MAZE_SIZE = maze_game_slider.get_current_value()
in_maze = False
player = Maze.Player(MAZE_SIZE*20+4, MAZE_SIZE*20+4, window)

def init_maze_runner():
    main_window.visible = False
    instruction_window.visible = False
    game_window.visible = False
    maze_window.visible = False
    main_window.rebuild()
    instruction_window.rebuild()
    game_window.rebuild()
    maze_window.rebuild()
    window.fill((0,0,0))
    MAZE_SIZE = maze_game_slider.get_current_value()
    build_maze(MAZE_SIZE)
    create_maze(20,40)
    #player = Maze.Player(MAZE_SIZE*20+4, MAZE_SIZE*20+4, window)
    player.x = MAZE_SIZE*20+8
    player.y = MAZE_SIZE*20+8
    #player.draw() 
def deinit_maze_runner():
    in_maze = False
    player.erase()
    while len(maze) > 0:
        maze.pop()
    while len(visited_squares) > 0:
        visited_squares.pop()
    while len(maze_stack) > 0:
        maze_stack.pop()
    window.fill((0,0,0))
    main_window.visible = True
    instruction_window.visible = True
    game_window.visible = True
    maze_window.visible = True
    main_window.rebuild()
    instruction_window.rebuild()
    game_window.rebuild()
    maze_window.rebuild()
    stack.move_window_to_front(instruction_window)

################ PAINT PICKER GAME ELEMENTS #######################
#@authors=catwoman2209 - Christiana Taylor

#Paint Picker panels
paint_bg = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        container=game_window,
                                        starting_layer_height=2,
                                        visible=False,
                                        object_id=ObjectID(class_id="@game_panel"))

#Paint Picker text entry lines
paint_text_entry = pygui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 200), (200, 50)),
                                        manager=manager,
                                        visible=False,
                                        container=paint_bg)
paint_text_entry.set_allowed_characters('letters')

#Paint picker variables
paint_surface = pygame.Surface((150,50))
font = pygame.font.SysFont("", 50)

#Paint Picker labels
paint_label_feedback1 = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (100, 50)),
                                                text="Correct!",
                                                manager=manager,
                                                container=paint_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@editor_label"))
paint_label_feedback2 = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (250, 50)),
                                                text="Incorrect! Please try again!",
                                                manager=manager,
                                                container=paint_bg, 
                                                visible = False,
                                                object_id=ObjectID(class_id="@editor_label"))
paint_label_score = pygui.elements.UILabel(relative_rect=pygame.Rect((300, 10), (200, 30)),
                                                text="",
                                                manager=manager,
                                                container=instruction_bg, 
                                                visible = False)

#Paint Picker functions
def set_Paint(x):
    paint_bg.visible = True
    paint_text_entry.visible = False

    if x == "black":
        paint_surface.fill(pygame.Color(0, 0, 0))
        color_text = ""
        color_text = Paint.get_paint_word("black")
        color_text_color = Paint.get_paint_word_color("black",color_text)
        word = font.render(color_text, False, pygame.Color(color_text_color))
        paint_surface.blit(word, (25, 5))
    if x == "white":
        paint_surface.fill(pygame.Color(255, 255, 255))
        color_text = ""
        color_text = Paint.get_paint_word("white")
        color_text_color = Paint.get_paint_word_color("white",color_text)
        word = font.render(color_text, False, pygame.Color(color_text_color))
        paint_surface.blit(word, (25, 5))
    if x == "red":
        paint_surface.fill(pygame.Color(255, 0, 0))
        color_text = ""
        color_text = Paint.get_paint_word("red")
        color_text_color = Paint.get_paint_word_color("red",color_text)
        word = font.render(color_text, False, pygame.Color(color_text_color))
        paint_surface.blit(word, (25, 5))
    if x == "blue":
        paint_surface.fill(pygame.Color(0, 0, 255))
        color_text = ""
        color_text = Paint.get_paint_word("blue")
        color_text_color = Paint.get_paint_word_color("blue",color_text)
        word = font.render(color_text, False, pygame.Color(color_text_color))
        paint_surface.blit(word, (25, 5))
    if x == "yellow":
        paint_surface.fill(pygame.Color(255, 255, 0))
        color_text = ""
        color_text = Paint.get_paint_word("yellow")
        color_text_color = Paint.get_paint_word_color("yellow",color_text)
        word = font.render(color_text, False, pygame.Color(color_text_color))
        paint_surface.blit(word, (25, 5))
    if x == "gray":
        paint_surface.fill(pygame.Color(128, 128, 128))
        color_text = ""
        color_text = Paint.get_paint_word("gray")
        color_text_color = Paint.get_paint_word_color("gray",color_text)
        word = font.render(color_text, False, pygame.Color(color_text_color))
        paint_surface.blit(word, (25, 5))
    if x == "green":
        paint_surface.fill(pygame.Color(0, 128, 0))
        color_text = ""
        color_text = Paint.get_paint_word("green")
        color_text_color = Paint.get_paint_word_color("green",color_text)
        word = font.render(color_text, False, pygame.Color(color_text_color))
        paint_surface.blit(word, (25, 5))
    if x == "purple":
        paint_surface.fill(pygame.Color(128, 0, 128))
        color_text = ""
        color_text = Paint.get_paint_word("purple")
        color_text_color = Paint.get_paint_word_color("purple",color_text)
        word = font.render(color_text, False, pygame.Color(color_text_color))
        paint_surface.blit(word, (25, 5))

    pygame.display.update()
    manager.update(time_delta)
    return paint_surface
def cont_Paint():
    wait()
    paint_surface.fill(pygame.Color(228, 225, 137))
    pygame.display.flip()
    paint_label_feedback1.visible = False
    paint_label_feedback2.visible = False
    paint_text_entry.visible = True
    manager.update(time_delta)
    pygame.display.update()
def end_Paint():
    try:
      score = round((accuracy/iteration)*100)
    except:
      score = 0

    string = "Accuracy: "+ str(score)+" "+str(accuracy)+"/"+str(iteration)

    paint_text_entry.visible = False
    paint_label_feedback1.visible = False
    paint_label_feedback2.visible = False
    paint_label_score.set_text(string)
    paint_label_score.visible = True
    paint_bg.visible = False
    game_bg.visible = False

    manager.update(time_delta)
    stack.move_window_to_front(instruction_window)

################ QUICK CHANGE GAME ELEMENTS #######################
#@authors=perennat - Tanner Kellogg

#Quick Change buttons
qc_button_20u = pygui.elements.UIButton(relative_rect=pygame.Rect((12, 275), (50, 50)),
                                            text="+",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_20d = pygui.elements.UIButton(relative_rect=pygame.Rect((12, 375), (50, 50)),
                                            text="-",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

qc_button_10u = pygui.elements.UIButton(relative_rect=pygame.Rect((112, 275), (50, 50)),
                                            text="+",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_10d = pygui.elements.UIButton(relative_rect=pygame.Rect((112, 375), (50, 50)),
                                            text="-",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

qc_button_5u = pygui.elements.UIButton(relative_rect=pygame.Rect((212, 275), (50, 50)),
                                            text="+",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_5d = pygui.elements.UIButton(relative_rect=pygame.Rect((212, 375), (50, 50)),
                                            text="-",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

qc_button_1u = pygui.elements.UIButton(relative_rect=pygame.Rect((312, 275), (50, 50)),
                                            text="+",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_1d = pygui.elements.UIButton(relative_rect=pygame.Rect((312, 375), (50, 50)),
                                            text="-",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

qc_button_qu = pygui.elements.UIButton(relative_rect=pygame.Rect((412, 275), (50, 50)),
                                            text="+",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_qd = pygui.elements.UIButton(relative_rect=pygame.Rect((412, 375), (50, 50)),
                                            text="-",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

qc_button_du = pygui.elements.UIButton(relative_rect=pygame.Rect((512, 275), (50, 50)),
                                            text="+",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_dd = pygui.elements.UIButton(relative_rect=pygame.Rect((512, 375), (50, 50)),
                                            text="-",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

qc_button_nu = pygui.elements.UIButton(relative_rect=pygame.Rect((612, 275), (50, 50)),
                                            text="+",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_nd = pygui.elements.UIButton(relative_rect=pygame.Rect((612, 375), (50, 50)),
                                            text="-",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

qc_button_pu = pygui.elements.UIButton(relative_rect=pygame.Rect((712, 275), (50, 50)),
                                            text="+",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_pd = pygui.elements.UIButton(relative_rect=pygame.Rect((712, 375), (50, 50)),
                                            text="-",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))
qc_button_give = pygui.elements.UIButton(relative_rect=pygame.Rect((300, 175), (125, 50)),
                                            text="Give Change",
                                            manager=manager,
                                            container=game_bg,
                                            visible=False,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

#Quick Change labels
qc_label_20 = pygui.elements.UILabel(relative_rect=pygame.Rect((12, 325), (50, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_10 = pygui.elements.UILabel(relative_rect=pygame.Rect((112, 325), (50, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_5 = pygui.elements.UILabel(relative_rect=pygame.Rect((212, 325), (50, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_1 = pygui.elements.UILabel(relative_rect=pygame.Rect((312, 325), (50, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_q = pygui.elements.UILabel(relative_rect=pygame.Rect((412, 325), (50, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_d = pygui.elements.UILabel(relative_rect=pygame.Rect((512, 325), (50, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_n = pygui.elements.UILabel(relative_rect=pygame.Rect((612, 325), (50, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_p = pygui.elements.UILabel(relative_rect=pygame.Rect((712, 325), (50, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_receipt = pygui.elements.UILabel(relative_rect=pygame.Rect((250, 50), (200, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_paid = pygui.elements.UILabel(relative_rect=pygame.Rect((250, 100), (200, 50)),
                                                text="0",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))


qc_label_20_name = pygui.elements.UILabel(relative_rect=pygame.Rect((12, 425), (50, 50)),
                                                text="$20",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_10_name = pygui.elements.UILabel(relative_rect=pygame.Rect((112, 425), (50, 50)),
                                                text="$10",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_5_name = pygui.elements.UILabel(relative_rect=pygame.Rect((212, 425), (50, 50)),
                                                text="$5",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_1_name = pygui.elements.UILabel(relative_rect=pygame.Rect((312, 425), (50, 50)),
                                                text="$1",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_q_name = pygui.elements.UILabel(relative_rect=pygame.Rect((412, 425), (50, 50)),
                                                text="$0.25",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_d_name = pygui.elements.UILabel(relative_rect=pygame.Rect((512, 425), (50, 50)),
                                                text="$0.10",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_n_name = pygui.elements.UILabel(relative_rect=pygame.Rect((612, 425), (50, 50)),
                                                text="$0.05",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))
qc_label_p_name = pygui.elements.UILabel(relative_rect=pygame.Rect((712, 425), (50, 50)),
                                                text="$0.01",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))

qc_label_answer = pygui.elements.UILabel(relative_rect=pygame.Rect((450, 175), (250, 50)),
                                                text="",
                                                manager=manager,
                                                container=game_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@bookworm_label"))

receipt_total = 0
payment = 0
qc_range = 21
qc_20 = 0
qc_10 = 0
qc_5 = 0
qc_1 = 0
qc_q = 0
qc_d = 0
qc_n = 0
qc_p = 0
#Quick Change functions
def set_quick_change():
    global qc_20, qc_10, qc_5, qc_1, qc_q, qc_d, qc_n, qc_p
    qc_20 = 0
    qc_10 = 0
    qc_5 = 0
    qc_1 = 0
    qc_q = 0
    qc_d = 0
    qc_n = 0
    qc_p = 0
    qc_button_20u.visible = True
    qc_button_20d.visible = True
    qc_button_10u.visible = True
    qc_button_10d.visible = True
    qc_button_5u.visible = True
    qc_button_5d.visible = True
    qc_button_1u.visible = True
    qc_button_1d.visible = True
    qc_button_qu.visible = True
    qc_button_qd.visible = True
    qc_button_du.visible = True
    qc_button_dd.visible = True
    qc_button_nu.visible = True
    qc_button_nd.visible = True
    qc_button_pu.visible = True
    qc_button_pd.visible = True

    qc_button_give.visible = True

    qc_label_20.visible = True
    qc_label_10.visible = True
    qc_label_5.visible = True
    qc_label_1.visible = True
    qc_label_q.visible = True
    qc_label_d.visible = True
    qc_label_n.visible = True
    qc_label_p.visible = True

    qc_label_20_name.visible = True
    qc_label_10_name.visible = True
    qc_label_5_name.visible = True
    qc_label_1_name.visible = True
    qc_label_q_name.visible = True
    qc_label_d_name.visible = True
    qc_label_n_name.visible = True
    qc_label_p_name.visible = True

    global receipt_total
    global payment


    receipt_total = Change.get_total()
    qc_label_receipt.set_text("Order total: ${}".format(receipt_total))
    qc_label_receipt.visible = True
    payment = Change.get_payment(receipt_total, qc_range)
    qc_label_paid.set_text("Paid: ${}".format(payment))
    qc_label_paid.visible = True
def reset_quick_change():
    global qc_20, qc_10, qc_5, qc_1, qc_q, qc_d, qc_n, qc_p
    qc_20 = 0
    qc_10 = 0
    qc_5 = 0
    qc_1 = 0
    qc_q = 0
    qc_d = 0
    qc_n = 0
    qc_p = 0

    qc_label_20.set_text(str(qc_20))
    qc_label_10.set_text(str(qc_10))
    qc_label_5.set_text(str(qc_5))
    qc_label_1.set_text(str(qc_1))
    qc_label_q.set_text(str(qc_q))
    qc_label_d.set_text(str(qc_d))
    qc_label_n.set_text(str(qc_n))
    qc_label_p.set_text(str(qc_p))

    global receipt_total
    global payment

    receipt_total = Change.get_total()
    qc_label_receipt.set_text("Order total: ${}".format(receipt_total))
    payment = Change.get_payment(receipt_total, qc_range)
    qc_label_paid.set_text("Paid: ${}".format(payment))
def qc_correct_score(change):
    qc_answer = "Change: ${} is correct!".format(change)
    qc_label_answer.set_text(qc_answer)
    qc_label_answer.visible = True
def qc_incorrect_score(change):
    qc_answer = "Change: ${} is incorrect!".format(change)
    qc_label_answer.set_text(qc_answer)
    qc_label_answer.visible = True
def qc_remove_score():
    qc_label_answer.set_text("")
    qc_label_answer.visible = False
def end_quick_change():
    try:
      score = round((accuracy/iteration)*100)
    except:
      score = 0

    string = "Accuracy: "+ str(score)+" "+str(accuracy)+"/"+str(iteration)

    global receipt_total
    global payment
    global qc_20, qc_10, qc_5, qc_1, qc_q, qc_d, qc_n, qc_p
    receipt_total = 0
    payment = 0
    qc_20 = 0
    qc_10 = 0
    qc_5 = 0
    qc_1 = 0
    qc_q = 0
    qc_d = 0
    qc_n = 0
    qc_p = 0

    qc_button_20u.visible = False
    qc_button_20d.visible = False
    qc_button_10u.visible = False
    qc_button_10d.visible = False
    qc_button_5u.visible = False
    qc_button_5d.visible = False
    qc_button_1u.visible = False
    qc_button_1d.visible = False
    qc_button_qu.visible = False
    qc_button_qd.visible = False
    qc_button_du.visible = False
    qc_button_dd.visible = False
    qc_button_nu.visible = False
    qc_button_nd.visible = False
    qc_button_pu.visible = False
    qc_button_pd.visible = False

    qc_button_give.visible = False

    qc_label_20.visible = False
    qc_label_10.visible = False
    qc_label_5.visible = False
    qc_label_1.visible = False
    qc_label_q.visible = False
    qc_label_d.visible = False
    qc_label_n.visible = False
    qc_label_p.visible = False
    qc_label_receipt.visible = False
    qc_label_paid.visible = False

    qc_label_20_name.visible = False
    qc_label_10_name.visible = False
    qc_label_5_name.visible = False
    qc_label_1_name.visible = False
    qc_label_q_name.visible = False
    qc_label_d_name.visible = False
    qc_label_n_name.visible = False
    qc_label_p_name.visible = False
    
    stack.move_window_to_front(instruction_window)

################ SPACE ODDITY GAME ELEMENTS #######################
#@authors=


####################### MAIN CODE #################################
#start of main code

clock = pygame.time.Clock()
is_running = True
flag = 0
flag2 = 0
flag3 = 0
flag4 = 0
accuracy = 0
iteration = 0
breadcrumb_count = 0

while is_running:

    time_delta = clock.tick(60)/1000.0

    ### START MAZE STUFF
    finished_maze = False
    if in_maze == True:
        player.draw()
        green_up = window.get_at((player.x, player.y-1)) == (193, 225, 193)
        green_right = window.get_at((player.x+1, player.y)) == (193, 225, 193)
        green_down = window.get_at((player.x, player.y+1)) == (193, 225, 193)
        green_left = window.get_at((player.x-1, player.y)) == (193, 225, 193)
        finished_maze = (green_up and (green_right or green_left)) or (green_down and (green_right or green_left))
        if finished_maze:
            player.erase()
            in_maze = False
            bookworm_label_score.set_text("You beat the maze!")
            deinit_maze_runner()
        
        key = pygame.key.get_pressed()
        
        can_go_up = True
        for i in range(0, 5):
            if window.get_at((player.x+i, player.y - 1)) == (255,255,255):
                can_go_up = False
                break
        can_go_right = True
        for i in range(0, 5):
            if window.get_at((player.x+5, player.y + i)) == (255,255,255):
                can_go_right = False
                break
        can_go_down = True
        for i in range(0, 5):
            if window.get_at((player.x+i, player.y + 5)) == (255,255,255):
                can_go_down = False
                break
        can_go_left = True
        for i in range(0, 5):
            if window.get_at((player.x-1, player.y + i)) == (255,255,255):
                can_go_left = False
                break
        if (key[pygame.K_UP] or key[pygame.K_w]):      
            if can_go_up:
                breadcrumb_count += 1
                if breadcrumb_count == 20:
                    player.leave_breadcrumb(player.x, player.y+5)
                    breadcrumb_count = 0
                player.erase()
                player.y -= 1
                player.draw()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            if can_go_right:
                breadcrumb_count += 1
                if breadcrumb_count == 20:
                    player.leave_breadcrumb(player.x-1, player.y)
                    breadcrumb_count = 0
                player.erase()
                player.x += 1
                player.draw()
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            if can_go_down:
                breadcrumb_count += 1
                if breadcrumb_count == 20:
                    player.leave_breadcrumb(player.x, player.y-1)
                    breadcrumb_count = 0
                player.erase()
                player.y += 1
                player.draw()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            if can_go_left:
                breadcrumb_count += 1
                if breadcrumb_count == 20:
                    player.leave_breadcrumb(player.x + 5, player.y)
                    breadcrumb_count = 0
                player.erase()
                player.x -= 1
                player.draw()
        if key[pygame.K_ESCAPE]:
            finished_maze = True
            in_maze = False
            bookworm_label_score.set_text("")
            player.erase()
            window.fill((0,0,0))
            deinit_maze_runner()
    if in_maze == False and finished_maze == True:
        finished_maze = False
        player.erase()
        window.fill((0,0,0))
    ### END MAZE STUFF
    
    for event in pygame.event.get():
        if flag3 == 1:
            flag3 = 0
            flag4 = 1
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()

        #maze slider
        if event.type == pygui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == maze_game_slider:
                s = "{}x{} Maze".format(event.value, event.value)
                maze_label_slider_title.text = s
                maze_label_slider_title.rebuild()
                manager.update(time_delta)

        #event handllers for game menu buttons
        if event.type == pygui.UI_BUTTON_PRESSED:
            blind_label_score.visible = False
            bookworm_label_score.visible = False
            editor_label_score.visible = False
            paint_label_score.visible = False
            
            if event.ui_element == blind_menu_button:
                print('Blind Date game launched')
                stack.move_window_to_front(instruction_window)
                flag = 1
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)
                
            if event.ui_element == book_menu_button:
                print('Bookworm game launched')
                stack.move_window_to_front(instruction_window)
                flag = 2
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == editor_menu_button:
                print('Editor game launched')
                stack.move_window_to_front(instruction_window)
                flag = 3
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == kiddo_menu_button:
                print('Find the Kiddo game launched')
                stack.move_window_to_front(instruction_window)
                flag = 4
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == maze_menu_button:
                print('Maze Runner game launched')
                stack.move_window_to_front(instruction_window)
                flag = 5
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == paint_menu_button:
                print('Paint Picker game launched')
                stack.move_window_to_front(instruction_window)
                flag = 6
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == change_menu_button:
                print('Quick Change game launched')
                stack.move_window_to_front(instruction_window)
                flag = 7
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == space_menu_button:
                print('Space Oddity game launched')
                stack.move_window_to_front(instruction_window)
                flag = 8
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == racer_menu_button:
                print('Type Racer game launched')
                stack.move_window_to_front(instruction_window)
                flag = 9
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (765, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == back_button:
                blind_label_score.visible = False
                bookworm_label_score.visible = False
                editor_label_score.visible = False
                paint_label_score.visible = False
                stack.move_window_to_front(main_window)

            if event.ui_element == quit_button:
                pygame.quit()

            if event.ui_element == back_game_button:

                if game_window.window_display_title == "Blind Date":
                   end_Blind()
                   accuracy = 0
                   iteration = 0

                if game_window.window_display_title == "Bookworm":
                   end_Bookworm()
                   accuracy = 0
                   iteration = 0

                if game_window.window_display_title == "Editor":
                   end_Editor()
                   accuracy = 0
                   iteration = 0
                
                if game_window.window_display_title == "Paint Picker":
                   end_Paint()
                   accuracy = 0
                   iteration = 0 
                    
                if game_window.window_display_title == "Quick Change":
                    end_quick_change()
                    accuracy = 0
                    iteration = 0

            if event.ui_element == maze_back_game_button:
                in_maze = False
                accuracy = 0
                iteration = 0
                #bookworm_label_score.set_text("")
                bookworm_label_score.visible = False
                deinit_maze_runner()
            if event.ui_element == maze_play_button:
                in_maze = True
                init_maze_runner()

            #Quick Change stuff
            if game_window.window_display_title == "Quick Change":
                if event.ui_element == qc_button_20u:
                    qc_20 += 1
                    qc_label_20.set_text(str(qc_20))
                    manager.update(time_delta)
                if event.ui_element == qc_button_20d and qc_20 > 0:
                    qc_20 -= 1
                    qc_label_20.set_text(str(qc_20))
                    manager.update(time_delta)
                if event.ui_element == qc_button_10u:
                    qc_10 += 1
                    qc_label_10.set_text(str(qc_10))
                    manager.update(time_delta)
                if event.ui_element == qc_button_10d and qc_10 > 0:
                    qc_10 -= 1
                    qc_label_10.set_text(str(qc_10))
                    manager.update(time_delta)
                if event.ui_element == qc_button_5u:
                    qc_5 += 1
                    qc_label_5.set_text(str(qc_5))
                    manager.update(time_delta)
                if event.ui_element == qc_button_5d and qc_5 > 0:
                    qc_5 -= 1
                    qc_label_5.set_text(str(qc_5))
                    manager.update(time_delta)
                if event.ui_element == qc_button_1u:
                    qc_1 += 1
                    qc_label_1.set_text(str(qc_1))
                    manager.update(time_delta)
                if event.ui_element == qc_button_1d and qc_1 > 0:
                    qc_1 -= 1
                    qc_label_1.set_text(str(qc_1))
                    manager.update(time_delta)
                if event.ui_element == qc_button_qu:
                    qc_q += 1
                    qc_label_q.set_text(str(qc_q))
                    manager.update(time_delta)
                if event.ui_element == qc_button_qd and qc_q > 0:
                    qc_q -= 1
                    qc_label_q.set_text(str(qc_q))
                    manager.update(time_delta)
                if event.ui_element == qc_button_du:
                    qc_d += 1
                    qc_label_d.set_text(str(qc_d))
                    manager.update(time_delta)
                if event.ui_element == qc_button_dd and qc_d > 0:
                    qc_d -= 1
                    qc_label_d.set_text(str(qc_d))
                    manager.update(time_delta)
                if event.ui_element == qc_button_nu:
                    qc_n += 1
                    qc_label_n.set_text(str(qc_n))
                    manager.update(time_delta)
                if event.ui_element == qc_button_nd and qc_n > 0:
                    qc_n -= 1
                    qc_label_n.set_text(str(qc_n))
                    manager.update(time_delta)
                if event.ui_element == qc_button_pu:
                    qc_p += 1
                    qc_label_p.set_text(str(qc_p))
                    manager.update(time_delta)
                if event.ui_element == qc_button_pd and qc_p > 0:
                    qc_p -= 1
                    qc_label_p.set_text(str(qc_p))
                    manager.update(time_delta)
                if event.ui_element == qc_button_give:
                    correct_change = round(payment - receipt_total, 2)
                    given_change = round(20*qc_20 + 10*qc_10 + 5*qc_5 + 1*qc_1 + 0.25*qc_q + 0.1*qc_d + 0.05*qc_n + 0.01*qc_p, 2)
                    if given_change == correct_change:
                        #print("Correct!")
                        qc_correct_score(given_change)
                        qc_range += 5
                        reset_quick_change()
                        
                    else:
                        #print("Receipt total: {}".format(receipt_total))
                        #print("Payment: {}".format(payment))
                        #print("Correct change: {}".format(correct_change))
                        #print("Given change: {}".format(given_change))
                        qc_incorrect_score(given_change)
            
            #event handler for play button based on game clicked
            if event.ui_element == play_button:
                instruction_textbox.clear_all_active_effects()
                instruction_textbox.full_redraw()

                #Activates Blind Date
                if flag == 1:
                    game_window.set_display_title("Blind Date")
                    game_bg.visible = False
                    blind_bg.visible = True
                    blind_label_number.visible = True
                    ans = get_number()
                    print(ans)
                    blind_label_number.set_text(str(ans))
                    stack.move_window_to_front(game_window)
                    flag2 = 1

                #Activates Bookworm
                if flag == 2:
                    game_window.set_display_title("Bookworm")
                    Book.jumble_list=[]
                    ans = Book.main()
                    print(ans)
                    set_Bookworm()
                    stack.move_window_to_front(game_window)

                #Activates Editor
                if flag == 3:
                    game_window.set_display_title("Editor")
                    answer = Editor.main()
                    set_Editor()
                    editor_textbox_sentence.append_html_text(answer[0])
                    print(answer[0])
                    editor_textbox_sentence_j.append_html_text(answer[1])
                    print(answer[1])
                    ans = answer[2]
                    stack.move_window_to_front(game_window)

                #Activates Find the Kiddo - currently under development
                if flag == 4:
                    exec(open("Kiddo.py").read())
                    stack.move_window_to_front(main_window)

                #Activates Maze Runner
                if flag == 5:
                    stack.move_window_to_front(maze_window)

                #Activates Paint Picker
                if flag == 6:
                    game_window.set_display_title("Paint Picker")
                    game_bg.visible = False
                    ans = Paint.get_paint_color()
                    flag2 = 1

                #Activates Quick Change
                if flag == 7:
                    game_window.set_display_title("Quick Change")
                    set_quick_change()
                    stack.move_window_to_front(game_window)

                #Activates Space Oddity - currently under development
                if flag == 8:
                    exec(open("Space.py").read())
                    stack.move_window_to_front(main_window)

                #Activates Type Racer
                if flag == 9:
                    while True:
                        Game().start_screen()

        if event.type == pygui.UI_TEXT_ENTRY_FINISHED:
            #if text entry is within Blind Date game
            if event.ui_element == blind_text_entry:
                print(blind_text_entry.get_text())
                blind_text_entry.visible = False
                if blind_text_entry.get_text() == str(ans):
                    blind_label_feedback1.visible = True
                    blind_label_feedback2.visible = False
                    print("Correct!")
                    accuracy += 1
                    iteration += 1
                    blind_text_entry.set_text("")
                    blind_text_entry.redraw()
                    blind_text_entry.update(time_delta)
                    if accuracy < 10:
                        blind_label_number.visible = True
                        ans = get_number()
                        print(ans)
                        blind_label_number.set_text(str(ans))
                        flag2 = 1 
                    else:
                        end_Blind()
                else:
                    blind_label_number.visible = True
                    blind_text_entry.set_text("")
                    blind_label_feedback2.visible = True
                    blind_label_feedback1.visible = False
                    iteration += 1
                    print("Incorrect!")
                    flag2 = 1
            #if text entry is within Bookworm game
            if event.ui_element == bookworm_text_entry:
                print(bookworm_text_entry.get_text())
                if bookworm_text_entry.get_text() == ans:
                    bookworm_label_feedback1.visible = True
                    bookworm_label_feedback2.visible = False
                    print("Correct!")
                    accuracy += 1
                    iteration += 1
                    Book.jumble_list=[]
                    if accuracy < 10:
                        ans = Book.main()
                        set_Bookworm()
                        print(ans)
                    else:
                        end_Bookworm()
                else:
                    bookworm_text_entry.set_text("")
                    bookworm_label_feedback2.visible = True
                    bookworm_label_feedback1.visible = False
                    iteration += 1
                    print("Incorrect!")
            #if text entry is within Editor game
            if event.ui_element == editor_text_entry:
                print(editor_text_entry.get_text())
                if editor_text_entry.get_text() == ans:
                    editor_label_feedback1.visible = True
                    editor_label_feedback2.visible = False
                    print("Correct!")
                    accuracy += 1
                    iteration += 1
                    if accuracy < 10:
                        answer = Editor.main()
                        set_Editor()
                        editor_textbox_sentence.append_html_text(answer[0])
                        print(answer[0])
                        editor_textbox_sentence_j.append_html_text(answer[1])
                        print(answer[1])
                        ans = answer[2]
                    else:
                        end_Editor()
                else:
                    editor_text_entry.set_text("")
                    editor_label_feedback2.visible = True
                    editor_label_feedback1.visible = False
                    iteration += 1
                    print("Incorrect!")
            #if text entry is within Paint Picker game
            if event.ui_element == paint_text_entry:
                print(paint_text_entry.get_text())
                paint_text_entry.visible = False
                if paint_text_entry.get_text() == ans:
                    paint_label_feedback1.visible = True
                    paint_label_feedback2.visible = False
                    print("Correct!")
                    accuracy += 1
                    iteration += 1
                    paint_text_entry.set_text("")
                    paint_text_entry.redraw()
                    paint_text_entry.update(time_delta)
                    if accuracy < 10:
                        ans = Paint.get_paint_color()
                        flag2 = 1 
                    else:
                        end_Paint()
                else:
                    paint_text_entry.set_text("")
                    paint_label_feedback2.visible = True
                    paint_label_feedback1.visible = False
                    iteration += 1
                    print("Incorrect!")
                    ans = Paint.get_paint_color()
                    flag2 = 1

        manager.process_events(event)

    manager.update(time_delta)
    manager.draw_ui(window)
    pygame.display.update()

    #for looping between wait() to ensure correct UI display
    if game_window.window_display_title == "Blind Date":
        if flag2 == 1:
            set_Blind()
            flag2 = 0    
    if game_window.window_display_title == "Paint Picker":
        if flag2 == 1:
            stack.move_window_to_front(game_window)
            paint_image = pygui.elements.UIImage(relative_rect=pygame.Rect((100,100), (150, 45)),
                                        image_surface=set_Paint(ans),
                                        manager=manager,
                                        container=paint_bg,
                                        visible=False)
            paint_image.visible = True
            flag2 = 0
            flag3 = 1
        if flag4 == 1:
            paint_image.visible = False
            cont_Paint()
            flag4 = 0
        
