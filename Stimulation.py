# Stimulation.py

import toga
from toga.style import Pack
from toga.style.pack import COLUMN


def racer_handler(widget):
    print("Type Racer game initiated.")

def editor_handler(widget):
    print("Editor game initiated."
    )
def kiddo_handler(widget):
    print("Find the Kiddo game initiated."
    )
def paint_handler(widget):
    print("Paint Picking game initiated.")

def build(app):

    english_box = toga.Box()
    english_box2 = toga.Box(style=Pack(direction=COLUMN))
    
    english_label = toga.Label("English Games")

    racer = toga.Button('Type Racer', on_press=racer_handler)
    racer.style.height = 60
    racer.style.width = 100
    racer.style.padding_top = 10
    racer.style.padding_bottom = 10    
    racer.style.padding_left = 10
    racer.style.flex = 0

    editor = toga.Button('Editor', on_press=editor_handler)
    editor.style.height = 60
    editor.style.width = 100
    editor.style.padding = 10
    editor.style.padding_bottom = 10 
    editor.style.padding_left = 10
    editor.style.flex = 0

    english_box.add(racer, editor)
    english_box2.add(english_label, english_box)

    focus_box = toga.Box()
    focus_box2 = toga.Box(style=Pack(direction=COLUMN))

    focus_label = toga.Label("Focus Games")

    kiddo = toga.Button('Find the Kiddo', on_press=kiddo_handler)
    kiddo.style.height = 60
    kiddo.style.width = 100
    kiddo.style.padding_top = 10
    kiddo.style.padding_bottom = 10    
    kiddo.style.padding_left = 10
    kiddo.style.flex = 0

    paint = toga.Button('Paint Picking', on_press=paint_handler)
    paint.style.height = 60
    paint.style.width = 100
    paint.style.padding = 10
    paint.style.padding_bottom = 10 
    paint.style.padding_left = 10
    paint.style.flex = 0

    focus_box.add(kiddo, paint)
    focus_box2.add(focus_label, focus_box) 

    scroll1 = toga.ScrollContainer(content = english_box2)

    split1 = toga.SplitContainer(direction=toga.SplitContainer.HORIZONTAL)
    split1.content = [scroll1, focus_box2]
    

    return split1

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