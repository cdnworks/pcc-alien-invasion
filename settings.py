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
        self.ship_limit = 3

        # Player bullet settings
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3
        self.bullets_destroyed_on_hit = True

        # Alien settings
        self.alien_speed_factor = 0.25
        self.fleet_drop_speed = 10
        # fleet_direction of 1 moves right, -1 moves left.
        self.fleet_direction = 1

        # Misc settings
        self.reset_timer = 1
