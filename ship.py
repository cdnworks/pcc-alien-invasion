from turtle import screensize
import pygame

class Ship():
    '''
    This class manages the properties and behaviors of the player's
    ship in the game.
    '''
    def __init__(self, ai_settings, screen):
        '''
        Initialize the ship and set it's starting location on the screen
        '''
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get it's rect
        # a rect is the rectangular area around a given surface (object)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a float value for the ship's center
        self.center = float(self.rect.centerx)

        # Flags and status
        self.moving_right = False
        self.moving_left = False


    def update_position(self):
        '''
        Update the ship's position based on the movement flags' status
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update the rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        '''
        Draw the ship.bmp at it's current location, i.e. wherever it's rect is
        '''
        self.screen.blit(self.image, self.rect)