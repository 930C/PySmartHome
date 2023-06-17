from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class Fan(AdjustableDevice, TemperatureControlInterface):
    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name, initial_level)

    def cool(self, step: float = 0.1):
        self.increase_level(step)

    def heat(self, step: float = 0.1):
        self.decrease_level(step)