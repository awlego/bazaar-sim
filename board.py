from game_types import ItemProtocol

class Board():
    def __init__(self):
        self._items: list[ItemProtocol] = []

    @property
    def items(self) -> list[ItemProtocol]:
        return self._items

    def add_item(self, item: ItemProtocol):
        self._items.append(item)

    def remove_item(self, item: ItemProtocol):
        self.items.remove(item)
