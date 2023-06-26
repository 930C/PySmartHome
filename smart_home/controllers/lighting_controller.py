from smart_home.controllers.controller import Controller
from smart_home.logging.logger import setup_logger


class LightingController(Controller):
    logger = setup_logger('LightingController')
    name = 'LightingController'

    def __init__(self):
        super().__init__()
        self.logger.info(f'Created controller {self.name}')

    def control_lighting(self, desired_brightness: float):
        self.logger.info(f'Controlling lighting with desired brightness {desired_brightness}')
        for sensor in self.sensors:
            if sensor.read() < desired_brightness:
                for device in self.devices:
                    device.switch_on()
            elif sensor.read() > desired_brightness:
                for device in self.devices:
                    device.switch_off()

    def update(self):
        self.logger.info(f'Updating {self.name}..')
