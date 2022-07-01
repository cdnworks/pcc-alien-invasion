import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from ship import Ship

def run_game():
    ''' Initialize pygame, settings and the screen object'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create the player ship
    ship = Ship(ai_settings, screen)
    # Bullets are pygame Sprites, so we can manage them as a 'Group'
    # Create a group to store bullets in
    bullets = Group()

    # Start the game loop
    while True:
        # Set up event listeners defined in game_functions
        gf.check_events(ai_settings, screen, ship, bullets)

        # Update object states
        ship.update()
        gf.update_bullets(bullets)
        

        # Redraw the screen during each pass
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()