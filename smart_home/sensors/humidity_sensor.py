from smart_home.sensors.sensor import Sensor


class HumiditySensor(Sensor):
    def __init__(self, name, initial_value: float = 50):
        super().__init__(name, initial_value)
