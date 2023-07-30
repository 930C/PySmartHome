from smart_home.sensors.sensor import Sensor


class FertilizationSensor(Sensor):
    measures = "fertilization"

    def __init__(self, name, initial_value: float = 10):
        super().__init__(name, initial_value)
