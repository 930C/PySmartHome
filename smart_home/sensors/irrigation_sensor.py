from smart_home.sensors.sensor import Sensor


class IrrigationSensor(Sensor):
    measures = "irrigation"

    def __init__(self, name, initial_value: float = 10):
        super().__init__(name, initial_value)
