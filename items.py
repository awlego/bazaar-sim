from item import ActivatableItem, Item
from behaviors import DamageBehavior, HealBehavior, ShieldBehavior, BurnBehavior, PoisonBehavior
from typing import Optional, TypedDict
from game_protocols import GameStateProtocol

class ItemConfig(TypedDict):
    name: str
    tags: list[str]
    cooldown_ms: Optional[int]
    damage: Optional[float]
    heal: Optional[float]

class ItemFactory:

    def __init__(self, game_state: GameStateProtocol):
        self.game_state = game_state
        self.BEHAVIOR_MAPPING = {
            "damage": DamageBehavior,
            "heal": HealBehavior,
            "shield": ShieldBehavior,
            "burn": BurnBehavior,
            "poison": PoisonBehavior,
        }

    def create(self, config: ItemConfig) -> Item:
        if not config.get("name") or not config.get("tags"):
            raise ValueError("Item must have name and tags")

        item = None
        if "cooldown_ms" in config and config["cooldown_ms"] is not None:
            item = ActivatableItem(config["name"], config["tags"], config["cooldown_ms"])
        else:
            item = Item(config["name"], config["tags"])

        if isinstance(item, ActivatableItem):
            for behavior_name, behavior_class in self.BEHAVIOR_MAPPING.items():
                if behavior_name in config:
                    item.add_behavior(behavior_class, self.game_state, config)

        return item

if __name__ == "__main__":
    from game_state import GameState
    game_state = GameState()
    item_factory = ItemFactory(game_state)

    item_config = {
        "name": "Health Potion",
        "tags": ["healing"],
        "cooldown_ms": 3000,
        "heal": 50
    }
    item = item_factory.create(item_config)

    item_config2 = {
        "name": "Rusty Sword",
        "tags": ["weapon"],
        "cooldown_ms": 4000,
        "damage": 10
    }
    sword = item_factory.create(item_config2)
