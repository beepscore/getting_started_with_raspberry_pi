#!/usr/bin/env python

# Use python 2.x not 3, because Raspbian PyGame doesn't work with 3.

import pygame

width = 640
height = 480
radius = 100
stroke = 1

radius2 = 10

# initialize Pygame and all of its submodules
pygame.init()

# window is a Pygame 'surface'
window = pygame.display.set_mode((width, height))
window.fill(pygame.Color(0, 0, 0))

# each iteration is like an animation frame
while True:
    for i in range(0, 255):
        xpos = i
        ypos = i
        
        # draw to offscreen buffer
        pygame.draw.circle(window,
                           pygame.Color(255, 0, 0),
                           (width/2, height/2),
                           radius,
                           stroke)
        
        pygame.draw.circle(window,
                           pygame.Color(0, 0, 255),
                           (xpos, ypos),
                           radius2,
                           stroke*2)


        # update view
        pygame.display.update()
        
    # enable close button in Pygame window
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        break
