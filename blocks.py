import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], size: int) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_move: int):
        self.rect.x += x_move
