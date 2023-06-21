from abc import ABC

from smart_home.interfaces.sensor_interface import SensorInterface


class Sensor(SensorInterface, ABC):
    def __init__(self, name: str, value: float = 0.0):
        self.name = name
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
