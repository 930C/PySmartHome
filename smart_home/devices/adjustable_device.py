from abc import ABC

from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.interfaces.adjustable_device_interface import AdjustableDeviceInterface


class AdjustableDevice(SwitchableDevice, AdjustableDeviceInterface, ABC):
    def __init__(self, name: str, initial_level: float = 1.0, min_level: float = 0.0, max_level: float = 1.0):
        super().__init__(name)
        self.min_level = min_level
        self.max_level = max_level
        self.value = initial_level
        self.logger.info(f'AdjustableDevice {name} created with initial level {initial_level}, min level {min_level} '
                         f'and max level {max_level}')

    def set_level(self, value: float):
        self.logger.info(f'Setting level of {self.name} to {value}')

        if value < self.min_level:
            self.logger.info(f'Level of {self.name} is lower than min level {self.min_level}. Setting level to '
                             'min level')
            self.value = self.min_level
        elif value > self.max_level:
            self.logger.info(f'Level of {self.name} is higher than max level {self.max_level}. Setting level to '
                             'max level')
            self.value = self.max_level
        else:
            self.value = value

    def get_level(self):
        self.logger.info(f'Getting level of {self.name}: {self.value}')
        return self.value

    def increase_level(self, value: float):
        self.logger.info(f'Increasing level of {self.name} by {value}')
        self.set_level(self.value + value)

    def decrease_level(self, value: float):
        self.logger.info(f'Decreasing level of {self.name} by {value}')
        self.set_level(self.value - value)
