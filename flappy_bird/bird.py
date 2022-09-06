import pygame
import setuptools

GRAVITY = 5


class Bird:
    def __init__(self):
        self.dead = False
        self.x = 70
        self.y = 350
        self.jump_speed = 10
        self.jump_time = 0
        self.selected_sprite = 0
        self.gravity = 5
        self.hitbox = pygame.Rect(65, 50, 50, 50)
        self.sprites = [
            pygame.image.load("../assets/1.png").convert_alpha(),
            pygame.image.load("../assets/2.png").convert_alpha(),
            pygame.image.load("../assets/dead.png")
        ]

    def jump(self):
        self.jump_time = 30
        self.jump_speed = 10

    def update(self):
        self._update_sprite()
        self._update_physics()

    def kill(self):
        self.dead = True

    def sprite(self) -> pygame.Surface:
        return self.sprites[self.selected_sprite]

    def position(self) -> (int, int):
        return self.x, self.y

    def _update_sprite(self):
        if self.dead:
            self.selected_sprite = 2
        elif self.jump_time:
            self.selected_sprite = 1
        else:
            self.selected_sprite = 0

    def _update_physics(self):
        if self.jump_time:
            self.jump_speed -= .8
            self.y -= self.jump_speed
            self.jump_time -= -.8
        else:
            self.y += self.gravity
            self.gravity += 0.1
        self.hitbox[1] = self.y