import random
from abc import ABC

from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.interfaces.sensor_interface import SensorInterface


class Sensor(SensorInterface, ABC):
    def __init__(self, name: str, value: float = 0.0, naturally_decrease: bool = True, min_value: float = 0.0, max_value: float = 100.0):
        self.name = name
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.naturally_decrease = naturally_decrease

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value < self.min_value:
            self.value = self.min_value
        elif value > self.max_value:
            self.value = self.max_value
        else:
            self.value = value

    def update(self, device: SwitchableDevice):
        if device.get_state():
            if self.naturally_decrease:
                if isinstance(device, AdjustableDevice):
                    self.set_value(self.get_value() + device.get_level() * 5)
                else:
                    self.set_value(self.value + 5)
            else:
                if isinstance(device, AdjustableDevice):
                    self.set_value(self.get_value() - device.get_level() * 5)
                else:
                    self.set_value(self.value - 5)
        elif self.naturally_decrease:
            self.set_value(self.value - random.random() * 10)
        else:
            self.set_value(self.value + random.random() * 10)
