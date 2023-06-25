from abc import ABC

from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.interfaces.adjustable_device_interface import AdjustableDeviceInterface


class AdjustableDevice(SwitchableDevice, AdjustableDeviceInterface, ABC):

    def __init__(self, name: str, initial_level: float = 1.0, min_level: float = 0.0, max_level: float = 1.0):
        super().__init__(name)
        self.min_level = min_level
        self.max_level = max_level
        self.value = initial_level

    def set_level(self, value: float):
        if value < self.min_level:
            self.value = self.min_level
        elif value > self.max_level:
            self.value = self.max_level
        else:
            self.value = value

    def get_level(self):
        return self.value

    def increase_level(self, value: float):
        self.set_level(self.value + value)

    def decrease_level(self, value: float):
        self.set_level(self.value - value)
