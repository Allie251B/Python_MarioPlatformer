# Mario-like Platformer
##### A 2D platformer game, inspired by classic Mario

---


## Overview

This is a simple platformer game created using the Pygame library in Python.
\
A platformer, or platform video game, 
is one that traditionally features two-dimensional graphics 
in which players control characters who jump or and runs between 
different platforms on the screen. 
\
Тhe game currently supports different difficulty levels, background music, 
sound effects. The player can move, jump, 
and collect bonuses as well as jump on an enemy to kill them.

---

## Requirements

1. Clone or download the repository.
```
$ git clone https://github.com/Allie251B/Python_MarioPlatformer.git
```
2. Install the Pygame library using `pip install pygame`.
```
$ pip install -r requirements.txt
```

---
## How to run
1. Navigate to the repository and run the file `main.py` or
```
$ python main.py
```
2. Select the difficulty level you wish to play from the prompt.
3. Click on the game window in your taskbar.
---
## Features
The game supports three levels with different difficulty:
* Easy
* Mid
* Hard 

Each level has a different map layout, background, background music and enemy/bonus placement.
The game also has player movement:
* Running right - `Right arrow key`
* Running left - `Left arrow key`
* Jumping - `Spacebar`

Also supported:
* Camera movement
* Collision with objects (floor, enemies, bonuses) 
* Player animations 
* Enemy movement
* Sound effects
* "Game over" screen if a player falls off the map

---
## User interaction

When running `main.py` the program initializes prompt dialogue with the user.
\
From there the user can choose what difficulty he wants to play at.
\
If the input is incorrect the game will not start and the user will be asked to type the difficulty again.
\
After choosing level difficulty a game window is open in the taskbar.
\
At the beginning of the map a "Guide" is spawned explain how the game works.
\
If the player drops off the map the game is over and the player has to run the code again.
\
The level is finished if the second "Guide" is reached. 
---
## Notes
* The game may not work correctly if the required files or images are moved or deleted.
* The game's music and sound effects may not play correctly on all systems.
---
## Future improvements
* Additional levels and obstacles
* Functioning bonuses.
* Damage from enemies


## Demo
A very short and laggy [demo](https://youtu.be/Ii3KuxVWZto) of the actual gameplay