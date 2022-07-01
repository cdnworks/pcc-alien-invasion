class Settings():
    '''A Class to store all the settings for Alien Invasion'''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Player ship settings
        self.ship_speed_factor = 0.5

        # Player bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3

