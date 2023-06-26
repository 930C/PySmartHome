from smart_home.logging.logger import setup_logger
from smart_home.sensors.sensor import Sensor


class FertilizationSensor(Sensor):
    logger = setup_logger('FertilizationSensor')

    def __init__(self, name, initial_value: float = 10):
        super().__init__(name, initial_value)
        self.logger.info(f'Created sensor {self.name} with initial value {self.value}')
