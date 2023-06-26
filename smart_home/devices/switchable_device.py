from abc import ABC

from smart_home.interfaces.switchable_device_interface import SwitchableDeviceInterface
from smart_home.logging.logger import setup_logger


class SwitchableDevice(SwitchableDeviceInterface, ABC):
    logger = setup_logger('SwitchableDevice')

    def __init__(self, name: str):
        self.name = name
        self.state = False
        self.logger.info(f'SwitchableDevice {name} created')

    def turn_on(self):
        self.state = True
        self.logger.info(f'{self.name} turned on')

    def turn_off(self):
        self.state = False
        self.logger.info(f'{self.name} turned off')

    def get_state(self):
        self.logger.info(f'Getting state of {self.name}: {self.state}')
        return self.state

