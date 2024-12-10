import pygame

from code import enemy
from code.enemy import Enemy
from code.entity import Entity


class Explosion(Entity):
    def __init__(self, position: tuple):
        # Passa o nome 'Explosion' e a posição para a classe pai (Entity)
        super().__init__(name='Explosion', position=position)

        # Carregar a imagem da explosão
        self.image = pygame.image.load('./asset/Explosion.png')  # Substitua pelo caminho correto da imagem
        self.rect = self.image.get_rect(center=position)
        self.lifetime = 20  # Quantos quadros a explosão vai durar

    def update(self):
        # Atualizar o estado da explosão, reduzindo o lifetime
        self.lifetime -= 1
        if self.lifetime <= 0:
            return False  # A explosão deve ser removida
        return True

    def move(self):
        pass
