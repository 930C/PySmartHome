from smart_home.controllers.controller import Controller


class LightingController(Controller):
    name = 'LightingController'

    def __init__(self):
        super().__init__()
        self.logger.info(f'Created controller {self.name}')

    def control_lighting(self, desired_brightness: float):
        self.logger.info(f'Controlling lighting with desired brightness {desired_brightness}')
        if len(self.sensors) is not 0:
            sensor_value = self.getStrategy().calculate_value_of_all_data(self.sensors)

            if sensor_value < desired_brightness:
                for device in self.devices:
                    device.switch_on()
            elif sensor_value > desired_brightness:
                for device in self.devices:
                    device.switch_off()

    def update(self):
        self.logger.info(f'Updating {self.name}..')
