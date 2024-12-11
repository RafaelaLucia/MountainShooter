import pygame

from code import enemy
from code.enemy import Enemy
from code.entity import Entity


class Explosion(Entity):
    def __init__(self, position: tuple):
        super().__init__(name='Explosion', position=position)

        self.image = pygame.image.load('./asset/Explosion.png')
        self.rect = self.image.get_rect(center=position)
        self.lifetime = 20

    def update(self):
        self.lifetime -= 1
        if self.lifetime <= 0:
            return False
        return True

    def move(self):
        pass
