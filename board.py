from game_protocols import ItemProtocol

class Board():
    def __init__(self):
        self._items: list[ItemProtocol] = []
        self._player = None

    @property
    def items(self) -> list[ItemProtocol]:
        return self._items

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    def add_item(self, item: ItemProtocol):
        item.owner = self.player
        # using a setter so that we can make sure that
        # the owner sets the player/opponent references?

        # hmmm how do I handle when an item that gives +5
        # to items besides it 
        self._items.append(item)

    def remove_item(self, item: ItemProtocol):
        self.items.remove(item)
