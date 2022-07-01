import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''This class manages bullets fired from the player ship'''

    def __init__(self, ai_settings, screen, ship):
        '''Create a bullet object at the ship's current position'''
        super().__init__() # Inherit properties from Sprite
        self.screen = screen

        # Create a bullet rect at (0, 0), then set the correct position
        # i.e. at the nose of the ship
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''Move the bullet up the screen with time'''
        # In pygame, the cartesian coordinate system starts at the origin
        # in the top left corner of the screen surface.
        # The coordinate values increase positively as you go right
        # and downward on the screen.
        # so subtracting a value from the y position, 
        # causes the object to go 'up'
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        '''Draw the bullet to the screen surface'''
        pygame.draw.rect(self.screen, self.color, self.rect)