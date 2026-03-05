import pygame, sys, random
from grid import Grid
from blocks import *

pygame.init()

# This is the game window
# (width, height)
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("BEPIS")

clock = pygame.time.Clock()
game_grid = Grid()

# for i in range(30):
#    game_grid.GRID[random.randint(0, 19)][random.randint(0, 9)] = random.randint(1, 6)
# game_grid.print_grid()

block = ZBlock()

# Game loop
while True:
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing stuff?
    screen.fill((44, 44, 127))
    game_grid.draw(screen)
    block.draw(screen)

    # Update positions for game objects
    pygame.display.update()
    clock.tick(60)