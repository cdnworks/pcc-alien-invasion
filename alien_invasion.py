import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from ship import Ship
from game_stats import GameStats

def run_game():
    ''' Initialize pygame, settings and the screen object'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance of the game stat tracker
    stats = GameStats(ai_settings)

    # Create the player ship
    ship = Ship(ai_settings, screen)

    # Make a group of aliens, and populate the group
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Bullets are pygame Sprites, so we can manage them as a 'Group'
    # Create a group to store bullets in
    bullets = Group()


    # Start the game loop
    while True:
        # Set up event listeners defined in game_functions
        gf.check_events(ai_settings, screen, ship, bullets)

        # If the game is still valid:
        if stats.game_active:
            # Update object states
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        

        # Redraw the screen during each pass
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()