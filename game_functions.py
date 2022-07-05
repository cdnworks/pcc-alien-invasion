import sys
from time import sleep

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

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    '''
    Update the position of all bullets in the group, and clear old bullets
    '''
    bullets.update()
    # Clear bullets that have gone past the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    ''' Respond to bullet-alien collisions'''
    # Check if any bullets hit an alien
    collisions = pygame.sprite.groupcollide(bullets, aliens,
                                ai_settings.bullets_destroyed_on_hit, True)
    # Respawn aliens if the group has been destroyed
    if len(aliens) == 0:
        # Destroy existing bullets too
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

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

def get_number_rows(ai_settings, ship_height, alien_height):
    '''Determine the number of rows of aliens that fit on the screen.'''
    available_space_y = (ai_settings.screen_height - 
                            (3* alien_height) - ship_height)
    number_rows = int(available_space_y/(2* alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''Create an alien and place it in the row.'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    '''Fill the screen with aliens'''
    # Create an alien and find the number of aliens in a row. (based on screen)
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #Create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    ''' Respond if any aliens have reached an edge of the screen surface'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    ''' Make the fleet descend a row, and change direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    ''' Respond to the player shit being hit by an anlien'''
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # Clear the game screen
        aliens.empty()
        bullets.empty()
        # Create a new alien group and center the ship respawn
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause the game momentarily
        sleep(ai_settings.reset_timer)
    
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    ''' Check if an alien has hit the bottom of the screen'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''
    Check if the fleet is at the screen edge,
    If it is, update the positions of all the aliens in the group
    '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Check for alien and player ship collisions
    # The dokill flag is set to false because we handle it in ship_hit
    if pygame.sprite.spritecollide(ship, aliens, False):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)