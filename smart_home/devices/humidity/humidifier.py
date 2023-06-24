from smart_home.devices.adjustable_device import AdjustableDevice


class Humidifier(AdjustableDevice):
    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name, initial_level, -1.0, 1.0)

    def humidify(self, level: float = 0.5):
        self.set_level(level)
        if not self.get_state():
            self.turn_on()
        print("Humidifying ", self.name, " with ", self.get_level(), " amount")

    def dehumidify(self, level: float = -0.5):
        self.set_level(level)
        if not self.get_state():
            self.turn_on()
        print("Dehumidifying ", self.name, " with ", self.get_level(), " amount")
