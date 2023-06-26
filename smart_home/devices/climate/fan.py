from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface
from smart_home.logging.logger import setup_logger


class Fan(AdjustableDevice, TemperatureControlInterface):
    logger = setup_logger('Fan')

    def __init__(self, name: str, initial_level: float = 1.0):
        super().__init__(name, initial_level)
        self.logger.info(f'Fan {name} created with initial level {initial_level}')

    def cool(self, step: float = 0.1):
        self.logger.info(f'Cooling {self.name} with step {step}')
        self.increase_level(step)

    def heat(self, step: float = 0.1):
        self.logger.info(f'Heating {self.name} with step {step}')
        self.decrease_level(step)
