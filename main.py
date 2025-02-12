from board import Board
from player import Player
from game_state import GameState
from items import ItemFactory

if __name__ == "__main__":
    
    game_state = GameState()
    item_factory = ItemFactory(game_state)

    item_config = {
        "name": "Health Potion",
        "tags": ["healing"],
        "cooldown_ms": 3000,
        "heal": 10
    }
    health_potion = item_factory.create(item_config)

    item_config2 = {
        "name": "Rusty Sword",
        "tags": ["weapon"],
        "cooldown_ms": 4000,
        "damage": 50
    }
    rusty_sword = item_factory.create(item_config2)
   

    p1 = Player(health=100, max_health=100, shield=0, burn=0, poison=0, board=Board(), game_state=game_state)
    p2 = Player(health=100, max_health=100, shield=0, burn=0, poison=0, board=Board(), game_state=game_state)
    p1.board.add_item(rusty_sword)
    p2.board.add_item(health_potion)
    game_state.players.append(p1)
    game_state.players.append(p2)

    game_state.start()
