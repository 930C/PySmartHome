from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class Heater(AdjustableDevice, TemperatureControlInterface):
    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name, initial_level)

    def heat(self):
        self.increase_level(0.1)

    def cool(self):
        self.decrease_level(0.1)