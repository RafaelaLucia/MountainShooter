import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE, C_RED


class GameOver:
    def __init__(self, window: Surface, player_score: list[int]):
        self.window = window
        self.player_score = player_score
        self.bg_image = pygame.image.load("./asset/gameover.png").convert()
        self.bg_music = "./asset/game_over_music.wav"

    def run(self):
        pygame.mixer.music.load('./asset/fail.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        large_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", 40)
        small_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", 20)

        title_text = "Game Over"
        title_surf = large_font.render(title_text, True, C_RED)
        title_rect = title_surf.get_rect(center=(WIN_WIDTH - 250, WIN_HEIGHT / 4))

        lines = ["Pressione R para Reiniciar", "ou S para Sair"]
        line_spacing = 25
        y_position = WIN_HEIGHT / 2

        while True:
            self.window.blit(self.bg_image, (0, 0))
            self.window.blit(title_surf, title_rect)

            for line in lines:
                line_surf = small_font.render(line, True, C_WHITE)
                line_rect = line_surf.get_rect(center=(WIN_WIDTH - 250, y_position))
                self.window.blit(line_surf, line_rect)
                y_position += line_spacing

            y_position = WIN_HEIGHT / 2

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pygame.mixer_music.stop()
                        return "restart"
                    if event.key == pygame.K_s:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
