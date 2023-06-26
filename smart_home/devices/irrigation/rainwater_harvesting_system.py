# Schalte dies ein, wenn es Regnet
# Schalte dies aus, wenn es nicht Regnet weil der Tank voll ist
# Der Tank ist wegen Mücken und Algen abgedeckt
from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.logging.logger import setup_logger


class RainwaterHarvestingSystem(SwitchableDevice):
    logger = setup_logger('RainwaterHarvestingSystem')

    def __init__(self, name: str):
        super().__init__(name)
        self.logger.info(f'Rainwater harvesting system {name} created')