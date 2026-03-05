import pygame, sys, random
from game import Game

pygame.init()

# This is the game window
# (width, height)
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("BEPIS")
clock = pygame.time.Clock()
game = Game()

# Game loop
while True:
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing stuff?
    screen.fill((44, 44, 127))
    game.draw(screen)

    # Update positions for game objects
    pygame.display.update()
    clock.tick(60)