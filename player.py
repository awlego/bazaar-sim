from game_protocols import BoardProtocol, GameStateProtocol

class Player:
    def __init__(self, health: int, 
                 max_health: int,
                 shield: int,
                 burn: int,
                 poison: int,
                 board: BoardProtocol,
                 game_state: GameStateProtocol):
        self._health = health
        self.max_health = max_health
        self.shield = shield
        self.burn = burn
        self.poison = poison
        self.board = board
        self.board.player = self
        self.game_state = game_state

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        # self._health = max(0, value) # letting health go below 0 so that we let a heal and damage event go off at the same time and cancel correctly.
        self._health = min(self.max_health, value)
        if self._health <= 0:
            self.game_state.end_game()
