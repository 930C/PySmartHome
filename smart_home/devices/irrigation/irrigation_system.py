from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.logging.logger import setup_logger


class IrrigationSystem(SwitchableDevice):
    logger = setup_logger('IrrigationSystem')

    def __init__(self, name: str):
        super().__init__(name)
        self.logger.info(f'Irrigation system {name} created')
