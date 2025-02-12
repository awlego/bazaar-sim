from dataclasses import dataclass
from game_protocols import BoardProtocol

# @dataclass
class Player:
    def __init__(self, health: int, 
                 max_health: int,
                 shield: int,
                 burn: int,
                 poison: int,
                 board: BoardProtocol):
        self.health = health
        self.health = health
        self.max_health = max_health
        self.shield = shield
        self.burn = burn
        self.poison = poison
        self.board = board
        self.board.player = self