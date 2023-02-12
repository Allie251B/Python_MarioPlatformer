import pygame
from blocks import Block
from maps import block_size, screen_width, screen_height
from player import *
from player2 import Player2
from tutorial import Guide
from enemy import Enemy
from bonuses import *


class Level:
    def __init__(self, layout: list[str], surface: pygame.Surface) -> None:
        self.display_surface = surface
        self.setup(layout)
        self.world_shift = 0
        self.current_x = 0
        self.bonus_sound = pygame.mixer.Sound('./backgrounds/sound/bonus2.wav')
        self.bonus_sound.set_volume(0.2)
        self.hit_sound = pygame.mixer.Sound('./backgrounds/sound/hit.wav')
        self.hit_sound.set_volume(0.2)
        self.death_sound = pygame.mixer.Sound('./backgrounds/sound/death_new.wav')
        self.death_sound.set_volume(0.2)

    def setup(self, layout: list[str]) -> None:
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()               #Group()
        self.guide = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.bonus = pygame.sprite.Group()

        bonus_sprite = Bonus(2240, 320, 'Health')
        self.bonus.add(bonus_sprite)

        bonus_sprite = Bonus(4928, 384, 'Diamond')
        self.bonus.add(bonus_sprite)

        bonus_sprite = Bonus(10368, 384, 'Diamond')
        self.bonus.add(bonus_sprite)

        bonus_sprite = Bonus(7872, 512, 'Health')
        self.bonus.add(bonus_sprite)

        guide_sprite = Guide(512, 534, 'Begin')
        self.guide.add(guide_sprite)

        guide_sprite2 = Guide(12104, 584, 'Ending')
        self.guide.add(guide_sprite2)

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * block_size
                y = row_index * block_size

                if col == 'X':
                    block = Block((x, y), block_size)
                    self.blocks.add(block)
                if col == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if col == 'M':
                    enemy_sprite = Enemy((x, y))
                    self.enemy.add(enemy_sprite)

    def scroll_x(self) -> None:
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 2) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    def horizont_collision(self) -> None:
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_collision(self) -> None:
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.blocks.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_floor = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        if player.on_floor and player.direction.y < 0 or player.direction.y > 1:
            player.on_floor = False

    def run(self) -> None:
        # map
        self.blocks.update(self.world_shift)
        self.bonus.update(self.world_shift)
        self.blocks.draw(self.display_surface)
        self.bonus.draw(self.display_surface)
        self.scroll_x()
        self.guide.update(self.world_shift)
        self.guide.draw(self.display_surface)

        # player
        self.player.update()
        self.vertical_collision()
        self.horizont_collision()
        self.player.draw(self.display_surface)
        self.enemy.update(self.world_shift)
        self.enemy.draw(self.display_surface)

        for bonus in self.bonus:
            if pygame.sprite.spritecollide(self.player.sprite, self.bonus, True):
                self.bonus_sound.play()
                bonus.kill()

        for enemy in self.enemy:
            player_rect = self.player.sprite.rect
            enemy_rect = enemy.rect

            # Check if the bottom of the player sprite intersects with the top of the enemy sprite
            if enemy_rect.top <= player_rect.bottom <= enemy_rect.top + enemy_rect.height and \
                    player_rect.right > enemy_rect.left and \
                    player_rect.left < enemy_rect.right:
                self.hit_sound.play()
                enemy.kill()

            elif enemy_rect.midleft == player_rect.midright:
                pass

        if self.player.sprite.rect.bottom > self.display_surface.get_height():
            # Load the game over image
            game_over_image = pygame.image.load("./backgrounds/buttons/gameover.png").convert_alpha()
            game_over_rect = game_over_image.get_rect()
            game_over_rect.center = (self.display_surface.get_width() // 2, self.display_surface.get_height() // 2)
            self.display_surface.blit(game_over_image, game_over_rect)
            self.death_sound.play()
            # Update the display
            pygame.display.update()
