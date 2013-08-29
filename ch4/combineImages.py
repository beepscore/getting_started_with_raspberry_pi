#!/usr/bin/env python

# Use python 2.x not 3, because Raspbian PyGame doesn't work with 3.

# Combine 2 images
# Reference
# Getting Started with Raspberry Pi
# Richardson and Wallace
# <http://shop.oreilly.com/product/0636920023371.do>
# Ch 4

import pygame

width = 450
height = 450

# initialize Pygame and all of its submodules
pygame.init()

# screen is a Pygame 'surface'
screen = pygame.display.set_mode((width, height))

background = pygame.image.load("background.png").convert_alpha()
theremin = pygame.image.load("theremin.png").convert_alpha()
screen.blit(background, (0, 0))
screen.blit(theremin, (135, 50))

while True:
    # update view
    pygame.display.update()

    # enable close button in Pygame window
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        break
