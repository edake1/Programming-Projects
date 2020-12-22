import pygame

# initialize pygame
pygame.init()

# create screen ....set_mode((height, width))
screen = pygame.display.set_mode((800, 600))
# anything happening in the game window is an EVENT

#Title and icon of window


# game loop
event_running = True
while event_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event_running = False
