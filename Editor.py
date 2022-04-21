#File for Editor game code
import pygame
import pygame_gui as pygui
from pygame_gui.core import ObjectID
import random

sentence = [["There is some good in this world, and it’s worth fighting for."],
            ["It is only with the heart that one can see rightly; what is essential is invisible to the eye."],
            ["I am no bird; and no net ensnares me: I am a free human being with an independent will, which I now exert to leave you."],
            ["Beware; for I am fearless, and therefore powerful."],
            ["The only way out of the labyrinth of suffering is to forgive."],
            ["This above all: To thine own self be true, And it must follow, as the night the day, Thou canst not then be false to any man."],
            ["I took a deep breath and listened to the old brag of my heart: I am, I am, I am."],
            ["Love is or it ain’t. Thin love ain’t love at all."],
            ["We accept the love we think we deserve."],
            ["And so we beat on, boats against the current, borne back ceaselessly into the past."],
            ["Ever’body’s askin’ that. ‘What we comin’ to?’ Seems to me we don’t never come to nothin’. Always on the way."],
            ["Whatever our souls are made of, his and mine are the same."],
            ["There are years that ask questions and years that answer."],
            ["I am not afraid of storms, for I am learning how to sail my ship."],
            ["All happy families are alike; each unhappy family is unhappy in its own way."],
            ["Memories warm you up from the inside. But they also tear you apart."],
            ["It is nothing to die; it is dreadful not to live."],
            ["Who controls the past controls the future. Who controls the present controls the past."],
            ["Life is to be lived, not controlled; and humanity is won by continuing to play in face of certain defeat."],
            ["Last night I dreamt I went to Manderley again."],
            ["It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."],
            ["Tomorrow I’ll think of some way to get him back. After all, tomorrow is another day."],
            ["Why, sometimes, I’ve believed as many as six impossible things before breakfast."],
            ["Don’t ever tell anybody anything. If you do, you start missing everybody."],
            ["It does not do to dwell on dreams and forget to live."],
            ["You pierce my soul. I am half agony. Half hope. Tell me not that I am too late, that such precious feelings are gone for ever."],
            ["I had the epiphany that laughter was light, and light was laughter, and that this was the secret of the universe."],
            ["There are some things you learn best in calm, and some in storm."],
            ["When you play the game of thrones you win or you die."],
            ["The world breaks everyone, and afterward, many are strong at the broken places."],
            ["Once upon a time there was a boy who loved a girl, and her laughter was a question he wanted to spend his whole life answering."],
            ["Very few castaways can claim to have survived so long at sea as Mr. Patel, and none in the company of an adult Bengal tiger."],
            ["Anyone who ever gave you confidence, you owe them a lot."],
            ["Isn’t it nice to think that tomorrow is a new day with no mistakes in it yet?"],
            ["You forget what you want to remember, and you remember what you want to forget."],
            ["It was a pleasure to burn."],
            ["The past is not dead. In fact, it’s not even past."],
            ["He has put a knife on the things that held us together and we have fallen apart."],
            ["Nowadays people know the price of everything and the value of nothing."],
            ["Time is the longest distance between two places."],
            ["The voice of the sea is seductive, never ceasing, whispering, clamoring, murmuring, inviting the soul to wander in abysses of solitude."],
            ["We dream in our waking moments, and walk in our sleep."],
            ["The place where you made your stand never mattered. Only that you were there… and still on your feet."],
            ["But soft! What light through yonder window breaks? It is the east, and Juliet is the sun."],
            ["My advice is, never do tomorrow what you can do today. Procrastination is the thief of time."],
            ["So many things are possible just as long as you don’t know they’re impossible."],
            ["I can’t stand it to think my life is going so fast and I’m not really living it."]]


def get_sentence():
    #initializing the arrays and strings used to parse
    sentence_array = []
    sentence_array2 = []
    word_array = []
    letter_array = []
    word_string = ""
    jumble_string = ""
    letter_string = ""

    sentence_array = random.choice(sentence)
    word_array = str.split(sentence_array[0])
    word_string = random.choice(word_array)

    while len(word_string)>8:
        word_string = random.choice(word_array)
    while len(word_string)<3:
        word_string = random.choice(word_array)

    original = word_string
    for character in word_string:
        if character.isalpha() == False:
            word_string = word_string.replace(character, "")

    correct = word_string

    while word_string:
        position = random.randrange(len(word_string))
        jumble_string += word_string[position]
        word_string = word_string[:position] + word_string[(position + 1):]

    while correct == jumble_string:
        jumble_string = ""
        word_string = correct
        while word_string:
            position = random.randrange(len(word_string))
            jumble_string += word_string[position]
            word_string = word_string[:position] + word_string[(position + 1):]

    sentence_array2 = list(map(lambda word_string: word_string.replace(original, jumble_string), sentence_array))

    return [sentence_array[0], sentence_array2[0], correct]


def main():
    array = []
    array = get_sentence()
    return array

    