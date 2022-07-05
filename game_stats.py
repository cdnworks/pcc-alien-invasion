class GameStats():
    '''
    This class tracks various statistics for the game, such as 
    point totals, player lives, etc.
    '''

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        '''initialize tracked statistics here'''
        self.ships_left = self.ai_settings.ship_limit