from smart_home.sensors.sensor import Sensor

#Liskov Substitution Principle (LSP) -> Subklasse kann Funktionalität von Superklasse überschreiben
class TemperatureSensor(Sensor):
    def __init__(self, device_id, name, value=21.5):
        super().__init__(device_id, name, value)
