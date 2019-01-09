Super Mario Bros Terminal game.
===============================

Introduction
------------

This game is written using basic python libraries.It has been tested on
**ONLY** linux based OSs.

Running the program
-------------------

-   Run the program:
-   'python3 main.py'

Controls:
---------

-   d right
-   a left
-   f bullet
-   w up jump
-   q quit
-   r restart

Structure
---------

OO\_concepts
------------

The game exhibits the following features: - It demonstrates
**Inheritance**. The main player and enemy classes are inherited from
the Person class. The pistol,coin and cake class are inerited from the
collectable class.

-   It demonstrates **Encapsulation**.Classes for each object in the
    game has been made.

-   It demonstrates **Polymorphism** and **Abstraction**

Details about gameplay
----------------------

-   The game has 2 modes: -- Easy mode with 1 enemy per screen,less
    number of blocks, pipes and powerups. -- Hard mode with 2 enemies
    per screen and more number of obstacles.

Movement
--------

-   left,right,jump
-   gravity effect
-   player mode dependent jump -- Normal mode denoted by "m". In this
    mode mario is not able to break the blocks (Only the block shifts up
    and down). In this mode,the player is able to jump only 2 block. --
    Big mode denoted by "M". In this mode mario is able to break
    blocks.In this mode, the player is able to jump 4 blocks. -- Super
    mode denoted by "S". In this mode we get the shooting mode.jump
    length is same as Big Mode.

Obstacles
=========

-   enemies move left and right automatcally
-   enemies with different speeds.
-   enemies chase the player.
-   score, distance of mario is displayed.

Score
=====

-   score by coin = 1
-   score by powerup = 5
-   score by killing = 10

Background
==========

-   scenery changes and mario always remains at center.
-   different scenes contain clouds,stairs
-   able to go back and forth in the complete map

Bonus
=====

-   color using ANSI color codes for terminal
-   sound using aplay command
-   smart enemies which chase the player, move fast as number of enemies
    decreases.
-   Game can be played in variable screen sizes also.    

Enemies
=======

-   random follow
-   can be by jumping and bullet.

Coins
=====

-   randomly generated
-   denoted by '\*'
-   need to break bricks to obtain coins

Powerups
========

-   power ups diappear if jumped on same block
-   random powr ups throught the level
-   pop up out of bricks
-   2 types
-   '@' for transition from m -\> M
-   '\$' for transition from M -\> S
-   transiton from m -\> S not possible

File structure
--------------

.
├── bulletclass.py
├── cake.py
├── clouds.py
├── coins.py
├── collectable_objects.py
├── color.py
├── config.py
├── ending.py
├── flag_1.py
├── main_mario_4.py
├── mario_player.py
├── NonBlockingInput.py
├── person.py
├── pistol.py
├── poles.py
├── Readme.md
├── requirements.txt
├── scene.py
├── small_enemy.py
├── sound
│   ├── breakblock.wav
│   ├── coin.wav
│   ├── collision.wav
│   ├── fireball.wav
│   ├── fireworks.wav
│   ├── gameover.wav
│   ├── jump.wav
│   ├── mariodie.wav
│   ├── powerup_appear.wav
│   ├── powerup_take.wav
│   ├── Read.txt
│   ├── reset.wav
│   ├── stomp.wav
│   └── theme.wav
├── start_screen.py
└── main.py

1 directory, 35 files
