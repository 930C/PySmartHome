from smart_home.devices.adjustable_device import AdjustableDevice


# Liskov Substitution Principle (LSP) -> Subklasse kann Funktionalität von Superklasse überschreiben
# Single Responsibility Principle (SRP) -> Unterklasse definiert spezifisches Verhalten des devices
class LEDLight(AdjustableDevice):
    def __init__(self, name):
        super().__init__(name)
        self.color = 0xFFFFFF

    def set_color(self, color: int):
        self.color = color

    def get_color(self):
        return self.color