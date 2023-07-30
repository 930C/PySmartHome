import random
from abc import ABC

from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.interfaces.sensor_interface import SensorInterface
from smart_home.logging.logger import LoggerFactory


class Sensor(SensorInterface, ABC):
    def __init__(self, name: str, value: float = 0.0, naturally_decrease: bool = True, min_value: float = 0.0, max_value: float = 100.0):
        self.name = name
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.naturally_decrease = naturally_decrease
        self.logger = LoggerFactory.setup_logger(self.name)
        self.logger.info(f'Created sensor {self.name} with value {self.value}, naturally decrease set to '
                         f'{self.naturally_decrease}, min value {self.min_value} and max value {self.max_value}')

    def get_value(self):
        self.logger.debug(f'Getting value of {self.name}: {self.value}')
        return self.value

    def set_value(self, value):
        self.logger.debug(f'Setting value of {self.name} from {self.value} to {value}')

        if value < self.min_value:
            self.logger.debug(f'Value of {self.name} is too low. Setting to {self.min_value}')
            self.value = self.min_value
        elif value > self.max_value:
            self.logger.debug(f'Value of {self.name} is too high. Setting to {self.max_value}')
            self.value = self.max_value
        else:
            self.value = value

    def update(self, device: SwitchableDevice):
        self.logger.debug(f'Updating {self.name} with {device.name}')

        if device.get_state():
            if self.naturally_decrease:
                if isinstance(device, AdjustableDevice):
                    self.set_value(self.get_value() + device.get_level() * 5)
                    self.logger.debug(f'Changing {self.name} by {device.get_level() * 5} to {self.value}')
                else:
                    self.set_value(self.value + 5)
                    self.logger.debug(f'Changing {self.name} by 5 to {self.value}')
            else:
                if isinstance(device, AdjustableDevice):
                    self.set_value(self.get_value() - device.get_level() * 5)
                    self.logger.debug(f'Changing {self.name} by {device.get_level() * 5} to {self.value}')
                else:
                    self.set_value(self.value - 5)
                    self.logger.debug(f'Changing {self.name} by 5 to {self.value}')
        elif self.naturally_decrease:
            random_number = random.random() * 5
            self.set_value(self.value - random_number)
            self.logger.debug(f'Changing {self.name} by {random_number} to {self.value}')
        else:
            random_number = random.random() * 10
            self.set_value(self.value + random_number)
            self.logger.debug(f'Changing {self.name} by {random_number} to {self.value}')
