import pygame

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

    # Start the game loop
    while True:
        # Set up event listeners defined in game_functions
        gf.check_events(ship)

        # Update object states
        ship.update_position()

        # Redraw the screen during each pass
        gf.update_screen(ai_settings, screen, ship)


run_game()