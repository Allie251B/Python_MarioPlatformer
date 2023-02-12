import pygame
from maps import block_size
from player import Player

health = pygame.image.load('./backgrounds/items/heartBonus.png')
diamond = pygame.image.load('./backgrounds/items/diamondBonus.png')

items = {
    'Health': health,
    'Diamond': diamond
}


class Bonus(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, bonus_type: str) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.bonus_type = bonus_type
        self.image = items[self.bonus_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + block_size//2, y + (block_size - self.image.get_height()))

    def update(self, x_move: int) -> None:
        self.rect.x += x_move
