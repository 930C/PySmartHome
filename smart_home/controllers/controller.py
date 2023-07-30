from abc import ABC, abstractmethod
from typing import List

from smart_home.logging.logger import LoggerFactory
from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.sensors.sensor import Sensor
from smart_home.strategies.average import Average
from smart_home.strategies.maximal import Maximal
from smart_home.strategies.minimal import Minimal
from smart_home.strategies.strategy import Strategy


class Controller(ABC):
    name = 'Controller'

    def __init__(self, strategy: Average | Maximal | Minimal = Average()):
        self.devices: List[SwitchableDevice] = []
        self.sensors: List[Sensor] = []
        self.strategy = strategy
        self.logger = LoggerFactory.setup_logger(self.name)
        self.logger.info(f'Created controller {self.name}')

    def get_devices(self):
        self.logger.debug(f'Getting devices of {self.name}..')
        return self.devices

    def get_sensors(self):
        self.logger.debug(f'Getting sensors of {self.name}..')
        return self.sensors

    def add_device(self, device):
        self.logger.debug(f'Adding device: {device.name} to {self.name}')
        self.devices.append(device)

    def add_sensor(self, sensor):
        self.logger.debug(f'Adding sensor: {sensor.name} to {self.name}')
        self.sensors.append(sensor)

    def remove_device(self, device):
        self.logger.debug(f'Removing device: {device.name} from {self.name}')
        self.devices.remove(device)

    def remove_sensor(self, sensor):
        self.logger.debug(f'Removing sensor: {sensor.name} from {self.name}')
        self.sensors.remove(sensor)

    def get_strategy(self) -> Strategy:
        return self.strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    @abstractmethod
    def update(self):
        self.logger.info(f'Updating {self.name}..')
        pass
