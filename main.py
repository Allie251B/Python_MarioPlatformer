import pygame
from sys import exit
from maps import *
from level import Level
from sounds import Sound
from pygame import mixer
from blocks import Block


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

while True:
    level_input = input("What difficulty map do you want to play? (Easy, Mid, Hard): ")
    if level_input == "Easy":
        level = Level(level_map, screen)
        sky = pygame.image.load('backgrounds/sky/sky.jpg').convert()
        mixer.init()
        mixer.music.load('backgrounds/sound/soundtrack.mp3')
        mixer.music.set_volume(0.3)  # Sets volume to 50%
        mixer.music.play()
        break
    elif level_input == "Mid":
        level = Level(level_map2, screen)
        sky = pygame.image.load('backgrounds/sky/sky2.jpg')
        sky = pygame.transform.scale(sky, (screen_width, screen_height))
        mixer.init()
        mixer.music.load('backgrounds/sound/soundtrack2.mp3')
        mixer.music.set_volume(0.3)  # Sets volume to 50%
        mixer.music.play()
        break
    elif level_input == "Hard":
        level = Level(level_map3, screen)
        sky = pygame.image.load('backgrounds/sky/skyboss.jpg')
        sky = pygame.transform.scale(sky, (screen_width, screen_height))
        mixer.init()
        mixer.music.load('backgrounds/sound/FMI.mp3')
        mixer.music.set_volume(0.3)  # Sets volume to 50%
        mixer.music.play()
        break
    else:
        print("Invalid level difficulty...Please input a correct difficulty (Easy, Mid, Hard)")
        continue

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)
