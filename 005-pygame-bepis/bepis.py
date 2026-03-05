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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key in [pygame.K_UP, pygame.K_z, pygame.K_q]:
                game.rotate_block()

    # Drawing stuff?
    screen.fill((44, 44, 127))
    game.draw(screen)

    # Update positions for game objects
    pygame.display.update()
    clock.tick(60)