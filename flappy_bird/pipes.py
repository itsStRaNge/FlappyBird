import random

import pygame


class Pipes:
    UPPER_PIPE = pygame.image.load("../assets/bottom.png").convert_alpha()
    BOTTOM_PIPE = pygame.image.load("../assets/top.png").convert_alpha()

    def __init__(self):
        self.gap = 150
        self.x = 400
        self.offset = random.randint(-110, 110)

    def update(self):
        self.x -= 2

    def hitboxes(self) -> (pygame.Rect, pygame.Rect):
        upper_rect = pygame.Rect(
            self.x,
            360 + self.gap - self.offset + 10,
            Pipes.UPPER_PIPE.get_width() - 10,
            Pipes.UPPER_PIPE.get_height()
        )
        bottom_rect = pygame.Rect(
            self.x,
            0 - self.gap - self.offset - 10,
            Pipes.BOTTOM_PIPE.get_width() - 10,
            Pipes.BOTTOM_PIPE.get_height()
        )
        return upper_rect, bottom_rect

    def get_upper_pipe(self):
        return Pipes.UPPER_PIPE, (self.x, 360 + self.gap - self.offset)

    def get_bottom_pipe(self):
        return Pipes.BOTTOM_PIPE, (self.x, 0 - self.gap - self.offset)