class Settings():
    '''A Class to store all the settings for Alien Invasion'''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 100)

        # Player ship settings
        self.ship_speed_factor = 0.5

