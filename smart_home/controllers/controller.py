from abc import ABC, abstractmethod

from smart_home.logging.logger import setup_logger


class Controller(ABC):
    logger = setup_logger('Controller')
    name = 'Controller'

    def __init__(self):
        self.devices = []
        self.sensors = []
        self.logger.info(f'Created controller {self.name}')

    def get_devices(self):
        self.logger.info(f'Getting devices of {self.name}..')
        return self.devices

    def get_sensors(self):
        self.logger.info(f'Getting sensors of {self.name}..')
        return self.sensors

    def add_device(self, device):
        self.logger.info(f'Adding device: {device.name} to {self.name}')
        self.devices.append(device)

    def add_sensor(self, sensor):
        self.logger.info(f'Adding sensor: {sensor.name} to {self.name}')
        self.sensors.append(sensor)

    def remove_device(self, device):
        self.logger.info(f'Removing device: {device.name} from {self.name}')
        self.devices.remove(device)

    def remove_sensor(self, sensor):
        self.logger.info(f'Removing sensor: {sensor.name} from {self.name}')
        self.sensors.remove(sensor)

    @abstractmethod
    def update(self):
        self.logger.info(f'Updating {self.name}..')
        pass
