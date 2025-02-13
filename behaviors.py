from game_protocols import GameStateProtocol, ItemProtocol
from abc import ABC, abstractmethod

class Behavior(ABC):
    def __init__(self, game_state: GameStateProtocol, item_config: dict, parent_item: ItemProtocol):
        self.game_state = game_state
        self.config = item_config
        self.parent_item = parent_item

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
    def __init__(self, game_state: GameStateProtocol, item_config: dict, parent_item: ItemProtocol):
        super().__init__(game_state, item_config, parent_item)
        self._damage = item_config['damage']
    
    def execute(self):
        opponent = self.game_state.get_owners_opponent(self.parent_item)
        opponent.health -= self._damage

    def _validate_config(self):
        super()._validate_config()
        if not self._config.get("damage"):
            raise ValueError("Damage behavior config must have a damage field")


class HealBehavior(Behavior):
    def __init__(self, game_state: GameStateProtocol, item_config: dict, parent_item: ItemProtocol):
        super().__init__(game_state, item_config, parent_item)
        self._heal = item_config['heal']
    
    def execute(self):
        player = self.game_state.get_owner(self.parent_item)
        player.health += self._heal

    def _validate_config(self):
        super()._validate_config()
        if not self._config.get("heal"):
            raise ValueError("Heal behavior config must have a heal field")
        
class ShieldBehavior(Behavior):
    def __init__(self, game_state: GameStateProtocol, item_config: dict, parent_item: ItemProtocol):
        super().__init__(game_state, item_config, parent_item)
        self._shield = item_config['shield']
    
    def execute(self):
        player = self.game_state.get_owner(self.parent_item)
        player.shield += self._shield

    def _validate_config(self):
        super()._validate_config()
        if not self._config.get("shield"):
            raise ValueError("Shield behavior config must have a shield field")
        
class BurnBehavior(Behavior):
    def __init__(self, game_state: GameStateProtocol, item_config: dict, parent_item: ItemProtocol):
        super().__init__(game_state, item_config, parent_item)
        self._burn = item_config['burn']

    def execute(self):
        opponent = self.game_state.get_owners_opponent(self.parent_item)
        opponent.burn += self._burn

    def _validate_config(self):
        super()._validate_config()
        if not self._config.get("burn"):
            raise ValueError("Burn behavior config must have a burn field")

class PoisonBehavior(Behavior):
    def __init__(self, game_state: GameStateProtocol, item_config: dict, parent_item: ItemProtocol):
        super().__init__(game_state, item_config, parent_item)
        self._poison = item_config['poison']

    def execute(self):
        opponent = self.game_state.get_owners_opponent(self.parent_item)
        opponent.poison += self._poison

    def _validate_config(self):
        super()._validate_config()
        if not self._config.get("poison"):
            raise ValueError("Poison behavior config must have a poison field")
