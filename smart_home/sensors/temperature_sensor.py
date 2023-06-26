from smart_home.logging.logger import setup_logger
from smart_home.sensors.sensor import Sensor


# Liskov Substitution Principle (LSP) -> Subklasse kann Funktionalität von Superklasse überschreiben
class TemperatureSensor(Sensor):
    logger = setup_logger('TemperatureSensor')

    def __init__(self, name, value=21.5):
        super().__init__(name, value)
        self.logger.info(f'Created sensor {self.name} with initial value {self.value}')
