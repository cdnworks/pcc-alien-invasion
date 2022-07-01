import sys

import pygame

from bullet import Bullet
from alien import Alien

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
    elif event.key == pygame.K_q:
        sys.exit()

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

def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''
    Redraw the screen and other objects during each pass
    '''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen) 
    #Calling draw() on a group (like aliens), pygame automatically draws each
    # element in the group at the position defined by it's rect attribute

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

def get_number_aliens_x(ai_settings, alien_width):
    '''Determine the number of aliens that fit in a row.'''
    available_space_x = ai_settings.screen_width -2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    '''Create an alien and place it in the row.'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    '''Fill the screen with aliens'''
    # Create an alien and find the number of aliens in a row. (based on screen)
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    # Create the first row of aliens
    for alien_number in range(number_aliens_x):
        #Create an alien and place it in the row
        create_alien(ai_settings, screen, aliens, alien_number)
