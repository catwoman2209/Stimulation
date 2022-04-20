import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID

pygame.init()

pygame.display.set_caption("Stimulation")
window = pygame.display.set_mode()

x = window.get_width()
y = window.get_height()

manager = pygui.UIManager((x, y), "/Users/ctaylor/pyqt_proj/menu_theme.json")
manager.get_theme().load_theme('panel.json')

x2 = x/2 - 400
y2 = y/2 - 300

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

#panels and windows for Stimulation
window2 = pygui.elements.UIWindow(rect=pygame.Rect(0, 0, x, y),
                            manager=manager,
                            window_display_title='Stimulation',
                            resizable=False)

stack = pygui.core.ui_window_stack.UIWindowStack(window_resolution=(x,y), root_container=window2) 

main_window = pygui.elements.UIWindow(rect=pygame.Rect(x2, y2, 800, 600),
                            manager=manager,
                            window_display_title='Main Menu',
                            resizable=False)

instruction_window = pygui.elements.UIWindow(rect=pygame.Rect(x2, y2, 800, 600),
                                            manager=manager,
                                            window_display_title='Instruction Menu',
                                            resizable=False)

stack.add_new_window(main_window)
stack.add_new_window(instruction_window)
stack.move_window_to_front(main_window)

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

#menu buttons for the games
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

play_button = pygui.elements.UIButton(relative_rect=pygame.Rect((350, 400), (100, 50)),
                                            text='PLAY',
                                            manager=manager,
                                            container=instruction_bg,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

quit_button = pygui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                            text='QUIT',
                                            manager=manager,
                                            container=main_toolbar,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))


clock = pygame.time.Clock()
is_running = True
flag = 0

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            quit()

        #event handllers for game menu buttons
        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == blind_menu_button:
                print('Blind Date game launched')
                stack.move_window_to_front(instruction_window)
                flag = 1
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(1),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)
                
        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == book_menu_button:
                print('Bookworm game launched')
                stack.move_window_to_front(instruction_window)
                flag = 2
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(2),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == editor_menu_button:
                print('Editor game launched')
                stack.move_window_to_front(instruction_window)
                flag = 3
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(3),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == kiddo_menu_button:
                print('Find the Kiddo game launched')
                stack.move_window_to_front(instruction_window)
                flag = 4
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(4),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == maze_menu_button:
                print('Maze Runner game launched')
                stack.move_window_to_front(instruction_window)
                flag = 5
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(5),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == paint_menu_button:
                print('Paint Picker game launched')
                stack.move_window_to_front(instruction_window)
                flag = 6
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(6),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == change_menu_button:
                print('Quick Change game launched')
                stack.move_window_to_front(instruction_window)
                flag = 7
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(7),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == space_menu_button:
                print('Space Oddity game launched')
                stack.move_window_to_front(instruction_window)
                flag = 8
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(8),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == racer_menu_button:
                print('Type Racer game launched')
                stack.move_window_to_front(instruction_window)
                flag = 9
                instruction_textbox = pygui.elements.UITextBox(html_text=instruction_text(9),
                                            relative_rect=pygame.Rect((0, 50), (800, 350)),
                                            manager=manager,
                                            container=instruction_bg)
                instruction_textbox.set_active_effect(pygui.TEXT_EFFECT_TYPING_APPEAR)
                manager.update(time_delta)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == back_button:
                stack.move_window_to_front(main_window)

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == quit_button:
                quit()

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == play_button:
                if flag == 1:
                    exec(open("Blind.py").read())
                    stack.move_window_to_front(main_window)

                if flag == 2:
                    exec(open("Book.py").read())
                    stack.move_window_to_front(main_window)
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

        manager.process_events(event)

    manager.update(time_delta)

    manager.draw_ui(window)

    pygame.display.update()
