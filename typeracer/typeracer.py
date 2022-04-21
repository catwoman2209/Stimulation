import pygame
from pygame.locals import *
import sys
from button import Button
import time
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('images/background.jpg')
background = pygame.transform.scale(background, (800, 600))


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


class Game:

    def __init__(self):
        self.w = 800
        self.h = 600
        self.reset = True
        self.active = False
        self.input_text = ''
        self.sentence = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.wpm = 0
        self.end = False
        self.defaultTextColor = "#000000"
        self.open_img = pygame.image.load('images/getready.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

    def start_screen(self):
        while True:
            screen.blit(background, (0, 0))

            pygame.display.set_caption("Start Screen")

            start_menu_pos = pygame.mouse.get_pos()

            MENU_TEXT = get_font(30).render(
                "CLICK START TO BEGIN", True, "#000000")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

            START_BUTTON = Button(image=pygame.image.load("images/Start.png"), pos=(self.w/2, self.h/2),
                                  text_input="START", font=get_font(40), base_color="Blue", hovering_color="Green")

            screen.blit(MENU_TEXT, MENU_RECT)

            for button in [START_BUTTON]:
                button.changeColor(start_menu_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_BUTTON.clicked(start_menu_pos):
                        self.startgame()

            pygame.display.update()

    def reset_button(self):
        while True:
            reset_menu_pos = pygame.mouse.get_pos()

            RESET_BUTTON = Button(image=pygame.image.load("images/Restart.png"), pos=(self.w/2, self.h/1.3),
                                  text_input="RESET", font=get_font(35), base_color="#6766cc", hovering_color="Green")

            for button in [RESET_BUTTON]:
                button.changeColor(reset_menu_pos)
                button.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if RESET_BUTTON.clicked(reset_menu_pos):
                            self.startgame()

            pygame.display.update()

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        f = open('assets/sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def show_results(self, screen):

        if(not self.end):
            self.total_time = time.time() - self.time_start

            count = 0
            for i, c in enumerate(self.sentence):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.sentence)*100

            self.wpm = len(self.input_text) * 60 / (5*self.total_time)
            self.end = True
            print(self.total_time)
            self.results = 'Time:'+str(round(self.total_time)) + " seconds | Typing Accuracy: " + str(
                round(self.accuracy)) + "%" + '| Wpm: ' + str(round(self.wpm))

            pygame.display.update()

    def startgame(self):

        self.reset_game()
        self.running = True

        while(self.running):

            game_over = False

            clock = pygame.time.Clock()

            screen.fill((0, 0, 0), (50, 250, 700, 50))
            pygame.draw.rect(screen, (255, 192, 25), (50, 250, 700, 50), 2)

            self.draw_text(screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if(x >= 50 and x <= 650 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(screen)
                            self.draw_text(screen, self.results,
                                           350, 28, self.defaultTextColor)
                            game_over = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            if game_over is True:
                self.reset_button()

            pygame.display.update()

        clock.tick(60)

    def reset_game(self):

        screen.blit(self.open_img, (0, 0))
        pygame.display.update()

        pygame.time.wait(750)  #this is how long the get ready screen is shown
        time.sleep(1)

        self.reset = False
        self.end = False
        self.input_text = ''
        self.sentence = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        self.sentence = self.get_sentence()

        if (not self.sentence):
            self.reset_game()

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        msg = "GO!!!"
        text = get_font(70).render(msg, 1, "#FF0000")
        text_rect = text.get_rect(center=(self.w/2, 130))
        screen.blit(text, text_rect)

        self.draw_text(screen, self.sentence, 230, 28, self.defaultTextColor)
        pygame.display.update()


Game().start_screen()
