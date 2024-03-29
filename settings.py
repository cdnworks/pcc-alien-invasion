class Settings():
    '''A Class to store all the settings for Alien Invasion'''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Player ship settings
        self.ship_limit = 3

        # Player bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3
        self.bullets_destroyed_on_hit = True

        # Alien settings
        self.fleet_drop_speed = 10

        # Level difficulty scaling
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # Misc settings
        self.reset_timer = 1

    def initialize_dynamic_settings(self):
        ''' Initialize settings that change over time in game'''
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.25

        # fleet_direction of 1 moves right, -1 moves left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        ''' Increases game speed settings and point values'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


