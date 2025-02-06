from abc import ABC, abstractmethod
from behaviors import Behavior
from game_types import GameStateProtocol

class Item(ABC):
    def __init__(self, name, tags):
        self.name = name
        self.tags = tags
        self.triggers: list[callable[[], None]] = []

    def trigger(self):
        # default implementation does nothing, aka no trigger
        pass

    def __str__(self):
        for variable in vars(self):
            print(f"{variable}: {getattr(self, variable)}")

    def add_behavior(self, behavior_class: type[Behavior], game_state: GameStateProtocol, item_config: dict):
        '''adds the actual actionable behavior to the item'''
        behavior = behavior_class(game_state=game_state, item_config=item_config)
        self._behaviors.append(behavior)

class ActivatableItem(Item):
    def __init__(self, name, tags, cooldown_ms):
        super().__init__(name, tags)
        self.cooldown_ms = cooldown_ms
        self.charge_ms = 0
        self.pending_activations = []
        self._hasted = False
        self._slowed = False
        self._frozen = False
        self._cached_speed_multiplier = 1.0
        self._behaviors: list[Behavior] = []
    
    @property
    def hasted(self) -> bool:
        return self._hasted

    @hasted.setter
    def hasted(self, value: bool):
        if self._hasted != value:
            self._hasted = value
            self._recalculate_speed_multiplier()

    @property
    def slowed(self) -> bool:
        return self._slowed

    @slowed.setter
    def slowed(self, value: bool):
        if self._slowed != value:
            self._slowed = value
            self._recalculate_speed_multiplier()

    @property
    def frozen(self) -> bool:
        return self._frozen

    @frozen.setter
    def frozen(self, value: bool):
        if self._frozen != value:
            self._frozen = value
            self._recalculate_speed_multiplier()

    def _recalculate_speed_multiplier(self):
        """Recalculate and cache the speed multiplier."""
        multiplier = 1.0
        if self._hasted:
            multiplier *= 2.0
        if self._slowed:
            multiplier *= 0.5
        if self._frozen:
            multiplier = 0
        self._cached_speed_multiplier = multiplier

    @property
    def speed_multiplier(self) -> float:
        """The current speed multiplier based on status effects."""
        return self._cached_speed_multiplier

    def activate(self):
        for behavior in self._behaviors:
            behavior.execute()

    def charge_ms(self, time_ms):
        self.charge_ms += time_ms

    def tick(self, delta_time_ms):
        self.charge_ms += delta_time_ms * self.speed_multiplier
        while self.charge_ms >= self.cooldown_ms:
            self.pending_activations.append(self.activate)
            self.charge_ms -= self.cooldown_ms
        
        if self.pending_activations:
            # only one activation allowed per game tick
            self.pending_activations.pop(0)()

