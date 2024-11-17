#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuPrincipal.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #desenhar imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Lucky", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            self.menu_text(50, "The Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 163))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 300 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 300 + 30 * i))
            pygame.display.flip()

            # Verifica todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('saindo...')
                    pygame.quit()  # fecha janela
                    quit()  # termina pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # Tecla para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                       return MENU_OPTION[menu_option]


