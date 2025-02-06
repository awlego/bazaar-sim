from game_types import GameStateProtocol
from abc import ABC, abstractmethod

class Behavior(ABC):
    def __init__(self, game_state: GameStateProtocol, item_config: dict):
        print(game_state, item_config)
        self.game_state = game_state
        self.config = item_config
    
    @property
    def config(self) -> dict:
        return self._config

    @config.setter
    def config(self, value: dict):
        self._config = value
        self._validate_config()
    
    def _validate_config(self):
        if not self._config:
            raise ValueError("Behavior must have a config")
        if not self._config.get("name") or not self._config.get("tags"):
            raise ValueError("Behavior must have a name and tags")

    @abstractmethod
    def execute(self):
        pass

class DamageBehavior(Behavior):
    def __init__(self, game_state: GameStateProtocol, item_config: dict):
        super().__init__(game_state, item_config)
        self._damage = item_config['damage']
    
    def execute(self):
        opponent = self.game_state.get_opponent()
        opponent.health = max(0, opponent.health - self._damage)

    def _validate_config(self):
        super()._validate_config()
        if not self._config.get("damage"):
            raise ValueError("Damage behavior config must have a damage field")

class HealBehavior(Behavior):
    def __init__(self, game_state: GameStateProtocol, item_config: dict):
        super().__init__(game_state, item_config)
        self._heal = item_config['heal']
    
    def execute(self):
        player = self.game_state.get_player()
        player.health = min(player.max_health, player.health + self._heal)

    def _validate_config(self):
        super()._validate_config()
        if not self._config.get("heal"):
            raise ValueError("Heal behavior config must have a heal field")