from abc import ABC


class Controller(ABC):
    name = 'Controller'

    def __init__(self):
        self.devices = []
        self.sensors = []

    def get_devices(self):
        return self.devices

    def get_sensors(self):
        return self.sensors

    def add_device(self, device):
        self.devices.append(device)

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def remove_device(self, device):
        self.devices.remove(device)

    def remove_sensor(self, sensor):
        self.sensors.remove(sensor)

    def update(self):
        pass
