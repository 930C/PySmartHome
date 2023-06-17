from smart_home.interfaces.sensor_interface import SensorInterface


class Sensor(SensorInterface):
    def __init__(self, name):
        self.name = name
        self.data = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data