import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''
    Respond to key press events
    '''
    if event.key == pygame.K_RIGHT:
        #move the ship right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #move the ship left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    '''
    Respond to key release events
    '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''
    Use listeners for pygame keyboard and mouse events
    '''
    for event in pygame.event.get():
        # event responses go here in this loop
        if event.type == pygame.QUIT:
            sys.exit()
        
        # key press responses
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    '''
    Redraw the screen and other objects during each pass
    '''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    '''
    Update the position of all bullets in the group, and clear old bullets
    '''
    bullets.update()

    # Clear bullets that have gone past the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    '''
    Create a new bullet object and add it to the bullets group
    but first check if there are less bullets than the allowed amount
    on screen
    '''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)