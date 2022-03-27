# Stimulation.py

import toga
from toga.style import Pack
from toga.style.pack import COLUMN

# main game button actions
def racer_handler(widget):
    print("Type Racer game initiated.")

def book_handler(widget):
    print("Bookworm game initiated.")

def editor_handler(widget):
    print("Editor game initiated.")

def kiddo_handler(widget):
    print("Find the Kiddo game initiated.")

def paint_handler(widget):
    print("Paint Picking game initiated.")

def change_handler(widget):
    print("Quick Change game initiated.")

def blind_handler(widget):
    print("Blind Date game initiated.")

def build(app):

    #container for the game section "English"
    english_box = toga.Box()
    english_box2 = toga.Box()
    english_Main = toga.Box(style=Pack(direction=COLUMN))
    
    english_label = toga.Label("English Games")

    #buttons for games
    racer = toga.Button('Type Racer', on_press=racer_handler)
    racer.style.height = 60
    racer.style.width = 100
    racer.style.padding_top = 10
    racer.style.padding_left = 10
    racer.style.flex = 0

    editor = toga.Button('Editor', on_press=editor_handler)
    editor.style.height = 60
    editor.style.width = 100
    editor.style.padding_top = 10
    editor.style.padding_left = 10
    editor.style.flex = 0

    book = toga.Button('Bookworm', on_press=book_handler)
    book.style.height = 60
    book.style.width = 100
    book.style.padding_top = 10
    book.style.padding_left = 10
    book.style.flex = 0

    #add buttons to containers
    english_box.add(racer, editor)
    english_box2.add(book)
    #combine label with game button containers
    english_Main.add(english_label, english_box, english_box2)

    #container for game section "Focus"
    focus_box = toga.Box()
    focus_Main = toga.Box(style=Pack(direction=COLUMN))

    focus_label = toga.Label("Focus Games")

    #buttons for games
    kiddo = toga.Button('Find the Kiddo', on_press=kiddo_handler)
    kiddo.style.height = 60
    kiddo.style.width = 100
    kiddo.style.padding_top = 10 
    kiddo.style.padding_left = 10
    kiddo.style.flex = 0
//
    paint = toga.Button('Paint Picking', on_press=paint_handler)
    paint.style.height = 60
    paint.style.width = 100
    paint.style.padding_top = 10
    paint.style.padding_left = 10
    paint.style.flex = 0

    #add buttons to containers
    focus_box.add(kiddo, paint)
    #combine label with game button containers
    focus_Main.add(focus_label, focus_box) 

    #container for the game section "Memory"
    memory_box = toga.Box()
    memory_box2 = toga.Box()
    memory_Main = toga.Box(style=Pack(direction=COLUMN))
    
    memory_label = toga.Label("Memory Games")

    #buttons for games
    blind2 = toga.Button('Blind Date', on_press=blind_handler)
    blind2.style.height = 60
    blind2.style.width = 100
    blind2.style.padding_top = 10
    blind2.style.padding_left = 10
    blind2.style.flex = 0

    kiddo2 = toga.Button('Find the Kiddo', on_press=kiddo_handler)
    kiddo2.style.height = 60
    kiddo2.style.width = 100
    kiddo2.style.padding_top = 10
    kiddo2.style.padding_left = 10
    kiddo2.style.flex = 0

    paint2 = toga.Button('Paint Picking', on_press=paint_handler)
    paint2.style.height = 60
    paint2.style.width = 100
    paint2.style.padding_top = 10
    paint2.style.padding_left = 10
    paint2.style.flex = 0

    #add buttons to containers
    memory_box.add(blind2, kiddo2)
    memory_box2.add(paint2)
    #combine label with game button containers
    memory_Main.add(memory_label, memory_box, memory_box2)

    #container for game section "Number"
    number_box = toga.Box()
    number_Main = toga.Box(style=Pack(direction=COLUMN))

    number_label = toga.Label("Number Games")

    #buttons for games
    change = toga.Button('Quick Change', on_press=change_handler)
    change.style.height = 60
    change.style.width = 100
    change.style.padding_top = 10
    change.style.padding_left = 10
    change.style.flex = 0

    blind = toga.Button('Blind Date', on_press=blind_handler)
    blind.style.height = 60
    blind.style.width = 100
    blind.style.padding_top = 10
    blind.style.padding_left = 10
    blind.style.flex = 0

    #add buttons to containers
    number_box.add(change, blind)
    #combine label with game button containers
    number_Main.add(number_label, number_box) 

    split1 = toga.SplitContainer(direction=toga.SplitContainer.VERTICAL)
    split1.content = [english_Main, focus_Main]

    split2 = toga.SplitContainer(direction=toga.SplitContainer.VERTICAL)
    split2.content = [memory_Main, number_Main]

    split3 = toga.SplitContainer(direction=toga.SplitContainer.HORIZONTAL)
    split3.content = [split1, split2]

    main_screen = toga.ScrollContainer(content=split3)
    
    return split3

def main():
    return toga.App(
        'Stimulation',
        'org.capstone.Stimulation',
        author='Black Rams',
        description="Stimulation is the product of our Capstone project.",
        startup=build
    )

if __name__ == '__main__':
    main().main_loop()
