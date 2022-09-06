import pygame
import random

# todo order
pygame.font.init()
screen = pygame.display.set_mode((400, 708))

from flappy_bird.bird import Bird
from flappy_bird.pipes import Pipes


class FlappyBird:
    def __init__(self):
        self.background = pygame.image.load("../assets/background.png").convert()
        self.font = pygame.font.SysFont("Arial", 50)
        self.bird = Bird()
        self.pipes = Pipes()
        self.counter = 0
        self.offset = random.randint(-110, 110)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(50)
            if self.user_has_clicked() and not self.bird.dead:
                self.bird.jump()
            self.bird.update()
            self.pipes.update()
            if self.bird_hit_wall():
                self.bird.kill()
            if self.bird_is_out_of_screen():
                self.reset_game()
            if self.player_passed_pipe():
                self.counter += 1
                self.pipes = Pipes()
            self.render()

    def player_passed_pipe(self):
        return self.pipes.x < -80

    def bird_is_out_of_screen(self) -> bool:
        return not 0 < self.bird.hitbox[1] < 720

    def bird_hit_wall(self) -> bool:
        p1, p2 = self.pipes.hitboxes()
        return p1.colliderect(self.bird.hitbox) or p2.colliderect(self.bird.hitbox)

    def reset_game(self):
        self.bird = Bird()
        self.pipes = Pipes()
        self.counter = 0

    def render(self):
        screen.fill((255, 255, 255))
        screen.blit(self.background, (0, 0))
        screen.blit(
            self.font.render(str(self.counter), -1, (255, 255, 255)),
            (200, 50)
        )
        screen.blit(*self.pipes.get_upper_pipe())
        screen.blit(*self.pipes.get_bottom_pipe())
        screen.blit(self.bird.sprite(), self.bird.position())
        pygame.display.update()

    def user_has_clicked(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            return event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN
        return False


if __name__ == "__main__":
    FlappyBird().run()
