from abc import ABC, abstractmethod

from smart_home.logging.logger import setup_logger


class Controller(ABC):
    logger = setup_logger(__name__)
    name = 'Controller'

    def __init__(self):
        self.logger.info('Initializing Controller..')
        self.devices = []
        self.sensors = []

    def get_devices(self):
        self.logger.info('Getting devices..')
        return self.devices

    def get_sensors(self):
        self.logger.info('Getting sensors..')
        return self.sensors

    def add_device(self, device):
        self.logger.info('Adding device: ' + device.name)
        self.devices.append(device)

    def add_sensor(self, sensor):
        self.logger.info('Adding sensor: ' + sensor.name)
        self.sensors.append(sensor)

    def remove_device(self, device):
        self.logger.info('Removing device: ' + device.name)
        self.devices.remove(device)

    def remove_sensor(self, sensor):
        self.logger.info('Removing sensor: ' + sensor.name)
        self.sensors.remove(sensor)

    @abstractmethod
    def update(self):
        pass
