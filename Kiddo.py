#File for Find the Kiddo game code
#
#TTU Capstone Project Spring 2022
#@author = amcvaney - Abi McVaney

import random
import pygame
from pygame.locals import *
import sys
import pygame_gui
from button import Button
import time
from pygame_gui.core import ObjectID
import Stimulation as S
#import pyautogui

pygame.init()

class Game:

    screen = pygame.display.set_mode()
    globalx = screen.get_width()
    globaly = screen.get_height()

    #these are making dimensions of the pygame_gui boc to pop up
    width,height= 400,400
    screen = pygame.display.set_mode((globalx,globaly))

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
    events = pygame.event.get()
  
    boyImg = pygame.image.load('images/boy.jpeg').convert()
    boy = pygame.image.load('images/boy.jpeg')
    boy = pygame.transform.scale(boy, (150,150))  
    rect = boy.get_rect()

    while True:

        pygame.time.Clock().tick(1) #this will count how long the red square will show for user to memorize.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exec(open("Stimulation.py").read(), globals(), globals())
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
                #this will generate a box to appear 
                sx,sy = random.randint(0,4)*globalx//5 , random.randint(0,4)*globaly//5
                squares.append([sx,sy])

            else:
                #this is restricting the red box to be in the bounds & of red 
                pygame.draw.rect(screen,(255,0,0),((squares[i][0]+2,squares[i][1]+2),(globalx//5-2,globaly//5-2)))                
                boyImg = screen.blit(boy, (sx,sy))
                generatesquare = False
                hidesquare = True

        pygame.display.update()



