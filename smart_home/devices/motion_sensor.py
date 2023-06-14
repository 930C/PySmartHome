from smart_home.devices.sensor import Sensor


# Motion Sensor (Bewegungsmelder)
# wenn sich jemand im Raum bewegt, bekommt er die Value 1, ansonsten 0.
#Liskov Substitution Principle (LSP) -> Subklasse kann Funktionalität von Superklasse überschreiben
class MotionSensor(Sensor):
    def __init__(self, device_id, name, value=0):
        super().__init__(device_id, name, value)
