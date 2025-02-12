from player import Player
from game_protocols import ItemProtocol

class GameState():

    def __init__(self):
        self.game_over = False
        self.current_time_ms = 0
        self.tick_step_ms = 1000
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
            print(self)

    def get_player(self) -> Player:
        return self.players[0]
    
    def get_opponent(self) -> Player:
        return self.players[1]
    
    def get_owner(self, item: ItemProtocol) -> Player:
        return item.owner
    
    def get_owners_opponent(self, item: ItemProtocol) -> Player:
        if item.owner == self.get_player():
            return self.get_opponent()
        else:
            return self.get_player()
    
    def __str__(self):
        string = ""
        if len(self.players) == 2:
            string += f"Time: {self.current_time_ms / 1000}s:"
            string += f"    p0 hp: {self.players[0].health}"
            string += f"    p1 hp: {self.players[1].health}"
        return string
        
