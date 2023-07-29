from smart_home.controllers.controller import Controller
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class ClimateController(Controller):
    name = 'ClimateController'
    temperature = None

    def __init__(self, desired_temperature: float = 21):
        super().__init__()
        self.desired_temperature = desired_temperature
        self.logger.info(f'ClimateController {self.name} with {self.desired_temperature} as desired temperature created')

    def control_climate(self):
        self.logger.info(f'Controlling climate with desired temperature {self.desired_temperature}')
        sensor_value = self.getStrategy().calculate_value(self.sensors)
        self.temperature = sensor_value

        for device in self.devices:
            if not device.get_state:
                device.switch_on()
            if isinstance(device, TemperatureControlInterface):
                if sensor_value < self.desired_temperature:
                    device.heat()
                elif sensor_value > self.desired_temperature:
                    device.cool()

            for sensor in self.sensors:
                sensor.update(device)

    def update(self):
        self.logger.info(f'Updating {self.name}..')
        self.control_climate()

    def get_temperature(self):
        return self.temperature  # Die Temperatur seit dem letzten Update
