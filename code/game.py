#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        #self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)), pygame.RESIZABLE)
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.FULLSCREEN)

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1], MENU_OPTION[2]]: #Jogos opções
                level = Level(self.window, 'Level 01', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]: #Sair
                pygame.quit()
                quit()
            else:
                pass

