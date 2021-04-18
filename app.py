
# import pygame and initialize packages
import pygame

# importing pygame.locals for key coordinates
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_f,
    K_r,
    K_u,
    K_l,
    K_b,
    K_d,
    KMOD_SHIFT
)

# initialize pygame
pygame.init()

# setting up screen constants (width and height)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# variable to keep game loop running
running = True

# Main Game Loop
while running:

    # loop that looks at every event in the queue
    for event in pygame.event.get():

        if event.type == KEYDOWN:  # check if user hit a key

            # getting mods for shift + key
            mods = pygame.key.get_mods()

            # check what key was hit
            if event.key == K_ESCAPE:  # escape key -> stop loop
                running = False
            elif event.key == K_f and mods & KMOD_SHIFT:  # SHIFT + F -> front counter rotation
                print("SHIFT + F KEY")
            elif event.key == K_r and mods & KMOD_SHIFT:  # SHIFT + R -> right counter rotation
                print("SHIFT + R KEY")
            elif event.key == K_u and mods & KMOD_SHIFT:  # SHIFT + U -> upper counter rotation
                print("SHIFT + U KEY")
            elif event.key == K_l and mods & KMOD_SHIFT:  # SHIFT + L -> left counter rotation
                print("SHIFT + L KEY")
            elif event.key == K_b and mods & KMOD_SHIFT:  # SHIFT + B -> back counter rotation
                print("SHIFT + B KEY")
            elif event.key == K_d and mods & KMOD_SHIFT:  # SHIFT + D -> down counter rotation
                print("SHIFT + D KEY")
            elif event.key == K_f:  # f key -> front rotation
                print("F KEY")
            elif event.key == K_r:  # r key -> right rotation
                print("R KEY")
            elif event.key == K_u:  # u key -> upper rotation
                print("U KEY")
            elif event.key == K_l:  # l key -> left rotation
                print("L KEY")
            elif event.key == K_b:  # b key -> back rotation
                print("B KEY")
            elif event.key == K_d:  # d key -> down rotation
                print("D KEY")

        elif event.type == QUIT:  # check if user clicked window close button
            running = False

# quit
pygame.quit()
