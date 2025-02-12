from typing import Protocol, List
from dataclasses import dataclass

class BoardProtocol(Protocol):
    @property
    def items(self) -> List['ItemProtocol']:
        ...
    def add_item(self, item: 'ItemProtocol') -> None:
        ...
    def remove_item(self, item: 'ItemProtocol') -> None:
        ...

class ItemProtocol(Protocol):
    name: str
    tags: List[str]
    def trigger(self) -> None:
        ...
    def tick(self, delta_time_ms: float) -> None:
        ...

class PlayerProtocol(Protocol):
    health: int
    max_health: int
    shield: int
    burn: int
    poison: int
    board: BoardProtocol

class GameStateProtocol(Protocol):
    def get_player(self) -> PlayerProtocol:
        ...
    def get_opponent(self) -> PlayerProtocol:
        ...
    def get_owner(self, item: ItemProtocol) -> PlayerProtocol:
        ...
    def get_owners_opponent(self, item: ItemProtocol) -> PlayerProtocol:
        ...

