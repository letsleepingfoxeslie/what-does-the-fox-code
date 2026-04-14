import pygame, sys, random
from game import Game

pygame.init()

# This is the game window
# (width, height)
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("BEPIS")
clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Game loop
while True:
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.is_game_over:
                game.is_game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.is_game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.is_game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.is_game_over:
                game.move_down()
            if event.key in [pygame.K_UP, pygame.K_z, pygame.K_q] and not game.is_game_over:
                game.rotate_block()

        # Custom event: every 200ms (by default... as of this commit)
        if event.type == GAME_UPDATE and not game.is_game_over:
            game.move_down()

    # Drawing stuff?
    screen.fill((44, 44, 127))
    game.draw(screen)

    # Update positions for game objects
    pygame.display.update()
    clock.tick(60)