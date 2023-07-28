from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class Heater(AdjustableDevice, TemperatureControlInterface):

    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name, initial_level)
        self.logger.info(f'Heater {name} created with initial level {initial_level}')

    def heat(self):
        self.logger.info(f'Heating {self.name} with step 0.1')
        if not self.get_state():
            self.turn_on()
        self.increase_level(0.1)

    def cool(self):
        self.logger.info(f'Cooling {self.name} with step 0.1')
        if not self.get_state():
            self.turn_on()
        self.decrease_level(0.1)
