from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.interfaces.humidity_control_interface import HumidityControlInterface
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class Fan(AdjustableDevice, TemperatureControlInterface, HumidityControlInterface):

    def __init__(self, name: str, initial_level: float = -1.0):
        super().__init__(name, initial_level, -1.0, 0.0)
        self.logger.info(f'Fan {name} created with initial level {initial_level}')

    def cool(self, step: float = -0.1):
        self.logger.info(f'Cooling {self.name} with step {step}')
        if not self.get_state():
            self.turn_on()
        self.increase_level(step)

    def heat(self, step: float = 0.1):
        self.logger.info(f'Cooling {self.name} stopped')

        if self.get_state():
            self.turn_off()

    def humidify(self, step: float = 0.1):
        self.logger.info(f'Humidifying {self.name} with {step} amount')
        if not self.get_state():
            self.turn_on()
        self.decrease_level(step)

    def dehumidify(self, step: float = 0.1):
        self.logger.info(f'Dehumidifying {self.name} with {step} amount')
        if not self.get_state():
            self.turn_on()
        self.increase_level(step)