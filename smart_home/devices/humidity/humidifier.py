from smart_home.devices.adjustable_device import AdjustableDevice


class Humidifier(AdjustableDevice):
    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name, initial_level, -1.0, 1.0)
        self.logger.info(f'Humidifier {name} created with initial level {initial_level}')

    def humidify(self, level: float = 0.5):
        self.logger.info(f'Humidifying {self.name} with {level} amount')
        self.set_level(level)
        if not self.get_state():
            self.turn_on()

    def dehumidify(self, level: float = -0.5):
        self.logger.info(f'Dehumidifying {self.name} with {level} amount')
        self.set_level(level)
        if not self.get_state():
            self.turn_on()
