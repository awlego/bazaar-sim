from player import Player
from game_protocols import ItemProtocol

class GameState():

    def __init__(self):
        self.game_over = False
        self.current_time_ms = 0
        self.tick_step_ms = 500
        self.players: list[Player] = []
    
    def tick(self, delta_time_ms):
        self.current_time_ms += delta_time_ms

        for player in self.players:
            # TODO should burn/poison tick the moment it's applied?
            for item in player.board.items:
                item.tick(delta_time_ms)
            player.tick(delta_time_ms)        
            
    def start(self):
        while not self.game_over:
            self.tick(self.tick_step_ms)
            if self.current_time_ms >= 30 * 1000:
                self.game_over = True
            print(self)
        print("Game over")
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
        
    def end_game(self):
        self.game_over = True
    
    def __str__(self):
        string = ""
        if len(self.players) == 2:
            string += "Time: %4s s | p0 hp:%-7i shield:%-7i burn:%-7i poison:%-7i" % \
                (str(self.current_time_ms / 1000), self.players[0].health, self.players[0].shield, self.players[0].burn, self.players[0].poison)
            
            string += "\n             | p1 hp:%-7i shield:%-7i burn:%-7i poison:%-7i\n" % \
                (self.players[1].health, self.players[1].shield, self.players[1].burn, self.players[1].poison)
            

        return string
        
