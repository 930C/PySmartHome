from abc import ABC

from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.interfaces.adjustable_device_interface import AdjustableDeviceInterface


class AdjustableDevice(SwitchableDevice, AdjustableDeviceInterface, ABC):

    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name)
        self.min_level = 0.0
        self.max_level = 1.0
        self.value = initial_level

    def set_level(self, value: float):
        if value < self.min_level or value > self.max_level:
            raise ValueError("Value out of range")
        self.value = value

    def get_level(self):
        return self.value

    def increase_level(self, value: float):
        self.set_level(self.value + value)

    def decrease_level(self, value: float):
        self.set_level(self.value - value)
