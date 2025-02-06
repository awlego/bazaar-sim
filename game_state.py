from player import Player

class GameState():

    def __init__(self):
        self.game_over = False
        self.current_time_ms = 0
        self.tick_step_ms = 100
        self.players: list[Player] = []
    
    def tick(self, delta_time_ms):
        self.current_time_ms += delta_time_ms

        for player in self.players:
            for item in player.board.items:
                item.tick(delta_time_ms)
            
    def start(self):
        while not self.game_over:
            self.tick(self.tick_step_ms)
            if self.current_time_ms >= 30 * 1000:
                self.game_over = True

    def get_player(self) -> Player:
        return self.players[0]
    
    def get_opponent(self) -> Player:
        return self.players[1]
    
