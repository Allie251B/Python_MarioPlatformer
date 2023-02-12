import pygame
from help import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()
        self.import_char_assets()
        self.frame_index = 0
        self.animation_speed = 0.08
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.health = 100
        self.max_health = self.health
        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.5
        self.jumping_height = -15
        self.status = 'idle'
        self.facing_right = True
        self.on_floor = False
        self.on_left = False
        self.on_right = False
        self.jump_sound = pygame.mixer.Sound('./backgrounds/sound/jump.wav')
        self.jump_sound.set_volume(0.1)

    def get_input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_floor:
            self.jumping()

    def get_state(self) -> None:
        if self.direction.y < 0:
            self.status = 'jump'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def animate(self) -> None:
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        mirrored = pygame.transform.flip(image, True, False)
        if self.facing_right:
            self.image = image
        else:
            self.image = mirrored

        if self.on_floor and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_floor and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_floor:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)


    def apply_gravity(self) -> None:
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jumping(self) -> None:
        self.direction.y = self.jumping_height
        self.jump_sound.play()

    def import_char_assets(self) -> None:
        character_path = './backgrounds/sprites/player1/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'death': [], 'hit': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def bonus_power_up(self, bonus_type: str) -> None:
        if bonus_type == 'Health':
            self.health += 20
            if self.health > self.max_health:
                self.health = self.max_health
        elif bonus_type == 'Diamond':
            self.speed += 2
        self.kill()

    def update(self) -> None:
        self.get_input()
        self.get_state()
        self.apply_gravity()
        self.animate()
