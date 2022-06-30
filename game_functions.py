import sys

import pygame

def check_keydown_events(event, ship):
    '''Respond to key press events'''
    if event.key == pygame.K_RIGHT:
        #move the ship right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #move the ship left
        ship.moving_left = True

def check_keyup_events(event, ship):
    '''Respond to key release events'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    # set listeners for keyboard and mouse events
    for event in pygame.event.get():
        # event responses go here in this loop
        if event.type == pygame.QUIT:
            sys.exit()
        
        # key press responses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    # Redraw the screen during each pass
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()