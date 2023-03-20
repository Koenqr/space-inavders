"""
Koen Kruijt Space Invaders Assaignement

With goodies:
scroller mode (for when you're bored)
"""

import pygame
#from save import *
import os
import time
import sys

from SpaceInvaders import SpaceInvaders

#from xmltodict import parse as import_xml
#from xmltodict import unparse as export_xml

import json


pygame.init()


def createSave(name):
    file = open(name, "x")
    file.write(json.dumps({
                "width": 800,
                "height": 600,
                "fullscreen": False,
                "scroller": False,
                "difficulty": 1,
                "record": 99999999999        
        }))
    file.close()


class Button:
    def __init__(self, text, x, y, width, height, font_size, color=(255, 255, 255), hover_color=(200, 200, 200)):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            text_surface = self.font.render(self.text, True, self.hover_color)
        else:
            text_surface = self.font.render(self.text, True, self.color)

        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width // 2, self.y + self.height // 2)
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos, event):
        mouse_x, mouse_y = mouse_pos

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
                return True
        return False

class mainGame():
    def __init__(self):
        # init game
        self.state = "mainMenu"
        self.setError = None

        # check save file
        self.saveFile = "save.json"
        if not os.path.isfile(self.saveFile):
            createSave(self.saveFile)

        # load save file
        file = open(self.saveFile, "r")
        self.save = json.loads(file.read())
        file.close()
        

        pygame.init()
        pygame.display.set_caption("Space Invaders but its HHS [Koen Kruijt]")
        self.screen = pygame.display.set_mode(
            (int(self.save['width']), int(self.save['height'])))
        self.clock = pygame.time.Clock()

    def main(self):
        while True:
            if self.state == "mainMenu":
                self.mainMenu()
            elif self.state == "game":
                time = self.game()
                if time != None:
                    ftimeseconds = float(time) / 10000000
                    self.save['record'] = min(ftimeseconds, self.save['record'])
                self.state = "mainMenu"
            elif self.state == "options":
                self.options()
            elif self.state == "exit":
                save = open(self.saveFile, "w")
                save.write(json.dumps(self.save))
                save.close
                pygame.quit()
                sys.exit()

    def mainMenu(self):
        font = pygame.font.Font(None, 36)
        start_text = font.render('Press ENTER to start', True, (255, 255, 255))
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (400, 300)
        ftimeseconds = float(self.save['record'])/10000000
        fastest_time = font.render('Fastest time: ' + str(ftimeseconds)[:5], True, (255, 255, 255))
        fastest_time_rect = fastest_time.get_rect()
        fastest_time_rect.center = (400, 350)
        
        settingsButton = Button("Settings", 300, 500, 200, 50, 36)

        while self.state == "mainMenu":
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "exit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state = "game"
                if settingsButton.is_clicked(mouse_pos, event):
                    self.state = "options"
    
            self.screen.fill((0, 0, 0))
            self.screen.blit(start_text, start_text_rect)
            self.screen.blit(fastest_time, fastest_time_rect)
            settingsButton.draw(self.screen, mouse_pos)
            pygame.display.flip()
            self.clock.tick(60)

    def game(self):
        space_invaders = SpaceInvaders(self.screen, self.clock, self.save['difficulty'])
        time = space_invaders.run()
        if time != None:
            self.save['record'] = min(time, self.save['record'])
        self.state = "mainMenu"

    def options(self):
        easy_button = Button("Easy", 300, 200, 200, 50, 36)
        medium_button = Button("Medium", 300, 300, 200, 50, 36)
        hard_button = Button("Hard", 300, 400, 200, 50, 36)

        while self.state == "options":
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "exit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = "mainMenu"

                if easy_button.is_clicked(mouse_pos, event):
                    self.save['difficulty'] = 1
                    self.state = "mainMenu"

                if medium_button.is_clicked(mouse_pos, event):
                    self.save['difficulty'] = 2
                    self.state = "mainMenu"
                if hard_button.is_clicked(mouse_pos, event):
                    self.save['difficulty'] = 3
                    self.state = "mainMenu"
                    
            self.screen.fill((0, 0, 0))
            easy_button.draw(self.screen, mouse_pos)
            medium_button.draw(self.screen, mouse_pos)
            hard_button.draw(self.screen, mouse_pos)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    mainGame().main()


   
		