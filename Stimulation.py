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
                
        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == book_menu_button:
                print('Bookworm game launched')
                stack.move_window_to_front(instruction_window)
                flag = 2

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == editor_menu_button:
                print('Editor game launched')
                stack.move_window_to_front(instruction_window)
                flag = 3

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == kiddo_menu_button:
                print('Find the Kiddo game launched')
                stack.move_window_to_front(instruction_window)
                flag = 4

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == maze_menu_button:
                print('Maze Runner game launched')
                stack.move_window_to_front(instruction_window)
                flag = 5

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == paint_menu_button:
                print('Paint Picker game launched')
                stack.move_window_to_front(instruction_window)
                flag = 6

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == change_menu_button:
                print('Quick Change game launched')
                stack.move_window_to_front(instruction_window)
                flag = 7

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == space_menu_button:
                print('Space Oddity game launched')
                stack.move_window_to_front(instruction_window)
                flag = 8

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == racer_menu_button:
                print('Type Racer game launched')
                stack.move_window_to_front(instruction_window)
                flag = 9

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == back_button:
                stack.move_window_to_front(main_window)

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
