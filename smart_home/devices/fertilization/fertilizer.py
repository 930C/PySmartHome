from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.logging.logger import setup_logger


class Fertilizer(AdjustableDevice):
    logger = setup_logger('Fertilizer')

    def __init__(self, name: str):
        super().__init__(name)
        self.logger.info(f'Fertilizer {name} created')

    def fertilize(self, amount: float):
        self.logger.info(f'Fertilizing {self.name} with {amount} amount')
        self.set_level(amount)
        if not self.state:
            self.turn_on()
        self.fertilizing()

    def stop_fertilizing(self):
        self.logger.info(f'Stop fertilizing {self.name}')
        self.turn_off()

    def fertilize_once(self, amount: float):
        self.logger.info(f'Fertilizing {self.name} once with {amount} amount')
        self.set_level(amount)
        self.turn_on()
        self.fertilizing()
        self.turn_off()

    def fertilizing(self):
        self.logger.info(f'Fertilizing {self.name} with {self.value} amount')

