import pygame
from pygame.locals import *
import sys
import pygame_gui
from button import Button
import time
import random



screen = pygame.display.set_mode()
globalx = screen.get_width()
globaly = screen.get_height()

background = pygame.image.load('images/background.jpg')
background = pygame.transform.scale(background, (globalx, globaly))


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


class Game:

    def __init__(self):
        self.w = globalx
        self.h = globaly
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
                        pygame.quit()
                        sys.exit()

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
            self.results = 'Time: '+str(round(self.total_time)) + " seconds | Typing Accuracy: " + str(
                round(self.accuracy)) + "%" + '| Wpm: ' + str(round(self.wpm))

            pygame.display.update()

    def startgame(self):

        self.reset_game()
        self.running = True

        while(self.running):

            game_over = False

            clock = pygame.time.Clock()

            screen.fill((0, 0, 0), (globalx/5, 250, globalx/1.75, 50))
            pygame.draw.rect(screen, (255, 192, 25), (globalx/5, 250, globalx/1.75, 50), 2)

            self.draw_text(screen, self.input_text, globalx/7, 26, (250, 250, 250))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if(x >= globalx/4 and x <= 1000 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(screen)
                            self.draw_text(screen, self.results,
                                           450, 40, self.defaultTextColor)
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

        return False

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

        msg = "When you click in the black box your time begins!"  #Head text
        text = get_font(30).render(msg, 1, "#e1ff00")
        text_rect = text.get_rect(center=(self.w/2, 130))
        screen.blit(text, text_rect)

        msg = "Press 'ENTER' when finished. Type quickly!"
        text = get_font(20).render(msg, 1, "#e1ff00")
        text_rect = text.get_rect(center=(self.w/2, 350))
        screen.blit(text, text_rect)

        self.draw_text(screen, self.sentence, 230, 28, self.defaultTextColor)


        pygame.display.update()

