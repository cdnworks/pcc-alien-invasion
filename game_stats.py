class GameStats():
    '''
    This class tracks various statistics for the game, such as 
    point totals, player lives, etc.
    '''

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # High score shouldnt be reset
        self.high_score = 0

        # The game starts in an inactive state
        self.game_active = False

    def reset_stats(self):
        '''initialize tracked statistics here'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0 # Initialized here so it resets every new game
        self.level = 1