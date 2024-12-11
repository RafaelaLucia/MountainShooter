from code.Const import ENTITY_SPEED
from code.enemy import Enemy


class EnemySpecial(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_direction = 1
        self.vertical_speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        self.rect.centery += self.vertical_direction * self.vertical_speed

        screen_height = 600
        if self.rect.top <= 0:
            self.vertical_direction = 1
            self.vertical_speed = ENTITY_SPEED[self.name] * 3
        elif self.rect.bottom >= screen_height:
            self.vertical_direction = -1
            self.vertical_speed = ENTITY_SPEED[self.name]
