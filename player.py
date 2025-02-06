from dataclasses import dataclass
from game_types import BoardProtocol

@dataclass
class Player:
    health: int
    max_health: int
    shield: int
    burn: int
    poison: int
    board: BoardProtocol
