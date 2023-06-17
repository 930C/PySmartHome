from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class RollerBlind(AdjustableDevice, TemperatureControlInterface):
    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name, initial_level)

    def cool(self):
        self.increase_level(0.1)

    def heat(self):
        self.decrease_level(0.1)

    # cool and heat does not conform SOLID principle because it is not a part of the interface
    # we can fix this by creating a new interface for temperature control and implement it in the classes that need it: Fan, Heater, RollerBlinds
    # call it TemperatureControl
