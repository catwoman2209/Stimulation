#File for Find the Kiddo game code
#
#TTU Capstone Project Spring 2022
#@author = amcvaney - Abi McVaney

import pygame
from pygame.locals import *
import sys
import pygame_gui
from button import Button
import time
import random
import sys

pygame.init()

screen = pygame.display.set_mode()
globalx = screen.get_width()
globaly = screen.get_height()

background = pygame.image.load('images/background.jpg')
background = pygame.transform.scale(background, (globalx, globaly))

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

#these are making dimensions of the pygame_gui boc to pop up
width,height= 400,400
screen = pygame.display.set_mode((globalx,globaly))

class Game:
    def start_screen(self):

            running = True

            while running is True:
                screen.blit(background, (0, 0))

                pygame.display.set_caption("Start Screen")

                start_menu_pos = pygame.mouse.get_pos()

                TITLE_TEXT = get_font(100).render(
                    "TYPE RACER", True, "#e1ff00")
                TITLE_RECT = TITLE_TEXT.get_rect(center=(globalx/2, globaly/5))

                MENU_TEXT = get_font(30).render(
                    "CLICK START TO BEGIN", True, "#000000")
                MENU_RECT = MENU_TEXT.get_rect(center=(globalx/2, globaly/3))

                START_BUTTON = Button(image=pygame.image.load("images/Start.png"), pos=(self.w/2, self.h/2),
                                    text_input="START", font=get_font(40), base_color="#6766cc", hovering_color="Green")

                EXIT_BUTTON = Button(image=pygame.image.load("images/Restart.png"), pos=(self.w/2, self.h/1.5),
                                    text_input="EXIT", font=get_font(35), base_color="#6766cc", hovering_color="Green")


                screen.blit(TITLE_TEXT, TITLE_RECT)
                screen.blit(MENU_TEXT, MENU_RECT)

                for button in [START_BUTTON, EXIT_BUTTON]:
                    button.changeColor(start_menu_pos)
                    button.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if START_BUTTON.clicked(start_menu_pos):
                            self.startgame()
                        if EXIT_BUTTON.clicked(start_menu_pos):
                            exec(open("Stimulation.py").read(), globals(), globals())

                pygame.display.update()
            



    def reset_button(self):
        while True:
            reset_menu_pos = pygame.mouse.get_pos()

            RESET_BUTTON = Button(image=pygame.image.load("images/Restart.png"), pos=(self.w/2, self.h/1.6),
                                text_input="RESET", font=get_font(35), base_color="#6766cc", hovering_color="Green")

            EXIT_BUTTON = Button(image=pygame.image.load("images/Restart.png"), pos=(self.w/2, self.h/1.3),
                                 text_input="RETURN", font=get_font(35), base_color="#6766cc", hovering_color="Green")

            for button in [RESET_BUTTON, EXIT_BUTTON]:
                button.changeColor(reset_menu_pos)
                button.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if RESET_BUTTON.clicked(reset_menu_pos):
                            self.startgame()
                        if EXIT_BUTTON.clicked(reset_menu_pos):
                            self.start_screen()

            pygame.display.update()

    for i in range(5):
        #these are making dimensions of the lines in the pygame_gui box
        pygame.draw.line(screen,(255,255,255),(globalx//5 * i,0),(globalx//5 * i,globaly))
        pygame.draw.line(screen,(255,255,255),(0,globaly//5 * i),(globalx, globaly//5 * i))

    generatesquare = True
    hidesquare = False
    squares=[]
    corrects = 0
    clicks = 0
    i = 0
    display_surface = pygame.display.set_mode((globalx,globaly))
    #pygame.display.set_caption('Image')
    boy = pygame.image.load('images/boy.jpeg')

    while True:
        pygame.time.Clock().tick(1) #this will count how long the red square will show for user to memorize.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN: #this is signaling the computer to move forward once user has clicked down
                if clicks+1 < len(squares):
                    x,y = event.pos
                    if squares[clicks][0]<=x<=squares[clicks][0]+globalx//5 and squares[clicks][1]<=y<=squares[clicks][1]+globaly//5:
                        #squares.clear()
                        clicks+=1
                else:
                    corrects+=1
                    generatesquare = True 
                    clicks=0

        if hidesquare:
            #this is restricting the red box to be in the bounds of the red 
            pygame.draw.rect(screen ,(0,0,0),((squares[i][0]+2,squares[i][1]+2),(globalx//5-2,globaly//5-2)))
            if i+1 <len(squares):
                i+=1
                generatesquare=True
            else:
                i=0
            hidesquare=False

        if generatesquare: 
            if len(squares)<=corrects:
                #this will generate a red box to appear
                sx,sy = random.randint(0,4)*globalx//5 , random.randint(0,4)*globaly//5
                squares.append([sx,sy])
            else:
                #this is restricting the red box to be in the bounds & of red 
                pygame.draw.rect(screen ,(255,0,0),((squares[i][0]+2,squares[i][1]+2),(globalx//5-2,globaly//5-2)))
                generatesquare = False
                hidesquare = True

        pygame.display.update()
