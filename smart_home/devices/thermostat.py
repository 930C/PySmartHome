from .device import Device

#Liskov Substitution Principle (LSP) -> Subklasse kann Funktionalität von Superklasse überschreiben
#Single Responsibility Principle (SRP) -> Unterklasse definiert spezifisches Verhalten des devices
class Thermostat(Device):
    def __init__(self, device_id, name, temperature=20.5):
        super().__init__(device_id, name)
        self.temperature = temperature
