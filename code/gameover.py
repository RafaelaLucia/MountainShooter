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
        # Carregar e tocar a música de fundo
        pygame.mixer.music.load('./asset/fail.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        # Configurações de fonte
        large_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", 40)
        small_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", 20)

        # Texto do título
        title_text = "Game Over"
        title_surf = large_font.render(title_text, True, C_RED)
        title_rect = title_surf.get_rect(center=(WIN_WIDTH - 250, WIN_HEIGHT / 4))

        # Texto de instruções dividido em duas linhas
        lines = ["Pressione R para Reiniciar", "ou S para Sair"]
        line_spacing = 25  # Espaçamento entre as linhas
        y_position = WIN_HEIGHT / 2

        # Loop principal da tela de Game Over
        while True:
            self.window.blit(self.bg_image, (0, 0))  # Desenhar imagem de fundo
            self.window.blit(title_surf, title_rect)  # Desenhar título

            # Renderizar as instruções linha por linha
            for line in lines:
                line_surf = small_font.render(line, True, C_WHITE)
                line_rect = line_surf.get_rect(center=(WIN_WIDTH - 250, y_position))
                self.window.blit(line_surf, line_rect)
                y_position += line_spacing  # Move para a próxima linha

            # Resetar posição inicial para as próximas iterações do loop
            y_position = WIN_HEIGHT / 2

            # Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Reiniciar o jogo
                        pygame.mixer_music.stop()
                        return "restart"
                    if event.key == pygame.K_s:  # Sair do jogo
                        pygame.quit()
                        sys.exit()

            # Atualizar display
            pygame.display.flip()
