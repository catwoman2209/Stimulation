import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID

pygame.init()

pygame.display.set_caption("Stimulation")
window = pygame.display.set_mode((800, 600))

manager = pygui.UIManager((800, 600), "/Users/ctaylor/pyqt_proj/menu_theme.json")
manager.get_theme().load_theme('panel.json')

main_background = pygui.elements.UIPanel(relative_rect=pygame.Rect((0, 50), (800, 550)),
                                        manager=manager,
                                        starting_layer_height=1,
                                        object_id=ObjectID(class_id='@main_panel'))

toolbar = pygui.elements.UIPanel(relative_rect=pygame.Rect((0,0), (800, 60)),
                                manager=manager,
                                starting_layer_height=1,
                                object_id=ObjectID(class_id='@toolbar'))

#menu buttons for the games
blind_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((90, 100), (200, 100)),
                                            text='Blind Date',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

book_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((300, 100), (200, 100)),
                                            text='Bookworm',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

editor_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((510, 100), (200, 100)),
                                            text='Editor',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

kiddo_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((90, 210), (200, 100)),
                                            text='Find the Kiddo',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

maze_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((300, 210), (200, 100)),
                                            text='Maze Runner',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

paint_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((510, 210), (200, 100)),
                                            text='Paint Picker',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

change_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((90, 320), (200, 100)),
                                            text='Quick Change',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

space_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((300, 320), (200, 100)),
                                            text='Space Oddity',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

racer_menu_button = pygui.elements.UIButton(relative_rect=pygame.Rect((510, 320), (200, 100)),
                                            text='Type Racer',
                                            manager=manager,
                                            container=main_background,
                                            object_id=ObjectID(class_id='@game_menu_buttons'))

clock = pygame.time.Clock()
is_running = True
flag = 0

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        #event handllers for game menu buttons
        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == blind_menu_button:
                print('Blind Date game launched')
                exec(open("Blind.py").read())
                

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == book_menu_button:
                print('Bookworm game launched')
                exec(open("Book.py").read())

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == editor_menu_button:
                print('Editor game launched')
                exec(open("Editor.py").read())

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == kiddo_menu_button:
                print('Find the Kiddo game launched')
                exec(open("Kiddo.py").read())

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == maze_menu_button:
                print('Maze Runner game launched')
                exec(open("Maze.py").read())

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == paint_menu_button:
                print('Paint Picker game launched')
                exec(open("Paint.py").read())

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == change_menu_button:
                print('Quick Change game launched')
                exec(open("Change.py").read())

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == space_menu_button:
                print('Space Oddity game launched')
                exec(open("Space.py").read())

        if event.type == pygui.UI_BUTTON_PRESSED:
            if event.ui_element == racer_menu_button:
                print('Type Racer game launched')
                exec(open("Racer.py").read())

        manager.process_events(event)

    manager.update(time_delta)

    manager.draw_ui(window)

    pygame.display.update()