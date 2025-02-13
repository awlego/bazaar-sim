from game_protocols import BoardProtocol, GameStateProtocol

class Player:
    BURN_RATE_MS = 500
    POISON_RATE_MS = 1000

    def __init__(self, health: int, 
                 max_health: int,
                 shield: int,
                 burn: int,
                 poison: int,
                 board: BoardProtocol,
                 game_state: GameStateProtocol):
        self._health = health
        self.max_health = max_health
        self._shield = shield
        self._burn = burn
        self._poison = poison
        self.board = board
        self.board.player = self
        self.game_state = game_state
        self.time_til_burn = Player.BURN_RATE_MS
        self.time_til_poison = Player.POISON_RATE_MS

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        # self._health = max(0, value) # letting health go below 0 so that we let a heal and damage event go off at the same time and cancel correctly.
        
        self._health = min(self.max_health, value)
        if self._health <= 0:
            self.game_state.end_game()

    def set_health_ignoring_shield(self, value):
        '''
        Set the health of the player, ignoring the shield.
        '''
        self._health = value

    @property
    def shield(self):
        return self._shield
    
    @shield.setter
    def shield(self, value):
        self._shield = value

    def take_damage(self, dmg):
        remaining_damage = max(0, dmg - self._shield)  # damage that gets through shield
        shield_damage = min(dmg, self._shield)  # damage absorbed by shield
        self.shield -= shield_damage
        self.health -= remaining_damage

    @property
    def burn(self):
        return self._burn

    @burn.setter
    def burn(self, value):
        # make sure that we never have negative burn
        self._burn = max(0, value)

    @property
    def poison(self):
        return self._poison

    @poison.setter
    def poison(self, value):
        self._poison = max(0, value)

    def tick(self, delta_time_ms):
        self.time_til_burn -= delta_time_ms
        self.time_til_poison -= delta_time_ms

        self.tick_burn()
        self.tick_poison()

    def tick_burn(self):
        if self.time_til_burn <= 0:
            self.take_damage(self.burn)
            self.burn -= 1
            self.time_til_burn += Player.BURN_RATE_MS

    def tick_poison(self):
        if self.time_til_poison <= 0:
            self.health -= self.poison
            self.time_til_poison += Player.POISON_RATE_MS

    
