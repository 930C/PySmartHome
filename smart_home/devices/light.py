from .device import Device

#Liskov Substitution Principle (LSP) -> Subklasse kann Funktionalität von Superklasse überschreiben
#Single Responsibility Principle (SRP) -> Unterklasse definiert spezifisches Verhalten des devices
class Light(Device):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.color = 0xFFFFFF
        self.brightness = 100
    