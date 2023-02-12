import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()
        self.image = pygame.image.load('./backgrounds/sprites/enemy/enemy.png')
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft=pos)
        self.move_direction = 1
        self.move_counter = 0

    def update(self, x_move: int) -> None:
        self.rect.x += x_move
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
