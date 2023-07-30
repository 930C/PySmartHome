from typing import List

from smart_home.controllers.controller import Controller
from smart_home.devices.lights.led_light import LEDLight


class LightingController(Controller):
    name = 'LightingController'

    def __init__(self):
        super().__init__()
        self.devices: List[LEDLight] = []
        self.logger.info(f'Created controller {self.name}')

    def control_lighting(self, desired_brightness: float):
        self.logger.info(f'Controlling lighting with desired brightness {desired_brightness}')
        if len(self.sensors) != 0:
            sensor_value = self.get_strategy().calculate_value_of_all_data(self.sensors)

            if sensor_value < desired_brightness:
                for device in self.devices:
                    device.turn_on()
            elif sensor_value > desired_brightness:
                for device in self.devices:
                    device.turn_off()

    def update(self):
        self.logger.info(f'Updating {self.name}..')
