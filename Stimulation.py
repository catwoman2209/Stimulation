#Main file for execution
#
#TTU Capstone Project Spring 2022
#@authors = christiana_taylor

import os
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import random
import Book

pygame.init()

pygame.display.set_caption("Stimulation")
window = pygame.display.set_mode()

x = window.get_width()
y = window.get_height()

cwd = os.getcwd()
manager = pygui.UIManager((x, y), cwd + "/menu_theme.json")
manager.get_theme().load_theme('panel.json')
manager.get_theme().load_theme('label.json')

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

#add windows to stack
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

main_toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                container=main_window,
                                object_id=ObjectID(class_id='@toolbar'))

instruction_toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                container=instruction_window,
                                object_id=ObjectID(class_id='@toolbar'))

game_toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                container=game_window,
                                object_id=ObjectID(class_id='@toolbar'))

#function for updating instruction_textbox
def instruction_text(x):

    if x == 1:
        return "<b>Blind Date</b><br><br>You went on a blind date that went great! Memorize their number to call them later!<br><br><br>This game may help those with Alzheimer’s to improve symptoms with continued use over time."

    if x == 2:
        return "<b>Bookworm</b><br><br>Are you a bookworm? Use the letters to find the word matching the definition<br><br><br>This game may help those with dyslexia to improve symptoms with continued use over time."
    
    if x == 3:
        return "<b>Editor</b><br><br>This author needs your help! Unscramble the author's errors as fast as you can!<br><br><br>This game may help those with dyslexia to improve symptoms with continued use over time."
    
    if x == 4:
        return "<b>Find the Kiddo</b><br><br>Listen to the sound of the toddler's giggles as they run through the house,<br>and follow their path!<br><br><br>This game may help those with ADHD to improve symptoms with continued use over time."
    
    if x == 5:
        return "<b>Maze Runner</b><br><br>Find the way out as quickly as you can!<br><br><br>This game may help those with ADHD to improve symptoms with continued use over time."
    
    if x == 6:
        return "<b>Paint Picker</b><br><br>Your partner needs help painting! Memorize the color you <em>see</em>,<br>not the color you read!<br><br><br>This game may help those with ADHD or Alzheimer’s to improve symptoms with continued use over time."
    
    if x == 7:
        return "<b>Quick Change</b><br><br>Customers want their change in this fast paced subtraction cafe!<br><br><br>This game may help those with ADHD to improve symptoms with continued use over time."
    
    if x == 8:
        return "<b>Type Racer</b><br><br>Test your typing skills in this race against time!<br><br><br>This game may help those with dyslexia to improve symptoms with continued use over time."
    
    if x == 9:
        return "<b>Space Oddity</b><br><br>Choose the odd alien out in this space-themed problem solving game!<br><br><br>This game may help those with ADHD to improve symptoms with continued use over time."

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
#@authors=christiana_taylor

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

bookworm_label_score = pygui.elements.UILabel(relative_rect=pygame.Rect((325, 10), (150, 30)),
                                                text="",
                                                manager=manager,
                                                container=instruction_bg, 
                                                visible = False,
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
      score = (accuracy/iteration)*100
    except:
      score = 0

    string = "Accuracy: "+ str(score)

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
#@authors=christiana_taylor

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
bookworm_text_entry.set_allowed_characters('numbers')

#Blind Date labels
blind_label_number = pygui.elements.UILabel(relative_rect=pygame.Rect((100, 50), (100, 50)),
                                                text="",
                                                manager=manager,
                                                container=blind_bg,
                                                visible=False, 
                                                object_id=ObjectID(class_id="@blind_label"))

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

blind_label_score = pygui.elements.UILabel(relative_rect=pygame.Rect((325, 10), (150, 30)),
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
      score = (accuracy/iteration)*100
    except:
      score = 0

    string = "Accuracy: "+ str(score)

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

clock = pygame.time.Clock()
is_running = True
flag = 0
flag2 = 0
accuracy = 0
iteration = 0

while is_running:

    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()

        #event handllers for game menu buttons
        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == blind_menu_button:
                print('Blind Date game launched')
                stack.move_window_to_front(instruction_window)
                flag = 1
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)
                
            if event.ui_element == book_menu_button:
                print('Bookworm game launched')
                stack.move_window_to_front(instruction_window)
                flag = 2
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == editor_menu_button:
                print('Editor game launched')
                stack.move_window_to_front(instruction_window)
                flag = 3
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == kiddo_menu_button:
                print('Find the Kiddo game launched')
                stack.move_window_to_front(instruction_window)
                flag = 4
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == maze_menu_button:
                print('Maze Runner game launched')
                stack.move_window_to_front(instruction_window)
                flag = 5
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == paint_menu_button:
                print('Paint Picker game launched')
                stack.move_window_to_front(instruction_window)
                flag = 6
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == change_menu_button:
                print('Quick Change game launched')
                stack.move_window_to_front(instruction_window)
                flag = 7
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == space_menu_button:
                print('Space Oddity game launched')
                stack.move_window_to_front(instruction_window)
                flag = 9
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == racer_menu_button:
                print('Type Racer game launched')
                stack.move_window_to_front(instruction_window)
                flag = 8
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(flag),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

            if event.ui_element == back_button:
                bookworm_label_score.visible = False
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

            if event.ui_element == quit_button:
                pygame.quit()

            if event.ui_element == play_button:
                instruction_textbox.clear_all_active_effects()
                instruction_textbox.full_redraw()

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

                if flag == 2:
                    game_window.set_display_title("Bookworm")
                    Book.jumble_list=[]
                    ans = Book.main()
                    print(ans)
                    set_Bookworm()
                    stack.move_window_to_front(game_window)

                if flag == 3:
                    exec(open("Editor.py").read())
                    stack.move_window_to_front(main_window)

                if flag == 4:
                    exec(open("Kiddo.py").read())
                    stack.move_window_to_front(main_window)

                if flag == 5:
                    exec(open("Maze.py").read())
                    stack.move_window_to_front(main_window)

                if flag == 6:
                    exec(open("Paint.py").read())
                    stack.move_window_to_front(main_window)

                if flag == 7:
                    exec(open("Change.py").read())
                    stack.move_window_to_front(main_window)

                if flag == 8:
                    exec(open("Racer.py").read())
                    stack.move_window_to_front(main_window)
                    
                if flag == 9:
                    exec(open("Space.py").read())
                    stack.move_window_to_front(main_window)

        if event.type == pygui.UI_TEXT_ENTRY_FINISHED:
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
                    if accuracy < 2:
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


        manager.process_events(event)

    manager.update(time_delta)

    manager.draw_ui(window)

    pygame.display.update()
        
    if game_window.window_display_title == "Blind Date":
        if flag2 == 1:
            set_Blind()
            flag2 = 0