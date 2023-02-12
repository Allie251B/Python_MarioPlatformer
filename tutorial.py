import pygame
from maps import block_size

begin_guide = pygame.image.load('./backgrounds/sprites/tutorial/temp.png')
end_guide = pygame.image.load('./backgrounds/sprites/tutorial/done.png')

items = {
    'Begin': begin_guide,
    'Ending': end_guide
}


class Guide(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, guide_type: str) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.guide_type = guide_type
        self.image = items[self.guide_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y-150)

    def update(self, x_move: int) -> None:
        self.rect.x += x_move
