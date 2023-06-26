from smart_home.devices.adjustable_device import AdjustableDevice


# Liskov Substitution Principle (LSP) -> Subklasse kann Funktionalität von Superklasse überschreiben
# Single Responsibility Principle (SRP) -> Unterklasse definiert spezifisches Verhalten des devices
class LEDLight(AdjustableDevice):
    def __init__(self, name):
        super().__init__(name)
        self.color = 0xFFFFFF
        self.logger.info(f'LED light {name} created with color {self.color}')

    def set_color(self, color: int):
        self.logger.info(f'Setting color of {self.name} to {color}')
        self.color = color

    def get_color(self):
        self.logger.info(f'Getting color of {self.name}: {self.color}')
        return self.color
