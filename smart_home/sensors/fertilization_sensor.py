from smart_home.sensors.sensor import Sensor


class FertilizationSensor(Sensor):
    def __init__(self, name):
        super().__init__(name, 0)

    def get_value(self):
        self.set_value(self.value + 0.5)
        # TODO: remove this later when KI is there
        return self.value

