from smart_home.devices.adjustable_device import AdjustableDevice


class Humidifier(AdjustableDevice):
    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name, initial_level)

    def humidify(self, step: float = 0.1):
        self.increase_level(step)

    def dehumidify(self, step: float = 0.1):
        self.decrease_level(step)