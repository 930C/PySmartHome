from smart_home.controllers.controller import Controller
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class ClimateController(Controller):
    name = 'ClimateController'

    def __init__(self):
        super().__init__()
        self.logger.info(f'ClimateController {self.name} created')

    def control_climate(self, desired_temperature: float):
        self.logger.info(f'Controlling climate with desired temperature {desired_temperature}')

        for sensor in self.sensors:
            if sensor.get_value() < desired_temperature:
                for device in self.devices:
                    device.switch_on()
                    if isinstance(device, TemperatureControlInterface):
                        device.heat()
            elif sensor.get_value() > desired_temperature:
                for device in self.devices:
                    device.switch_on()  # TODO: Li muss überprüfen welche devices an oder aus gehen soll
                    if isinstance(device, TemperatureControlInterface):
                        device.cool()

    def update(self):
        self.logger.info(f'Updating {self.name}..')
        # TODO: muss befüllt werden mit Logik
