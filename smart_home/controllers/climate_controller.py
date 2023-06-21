from smart_home.controllers.controller import Controller
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class ClimateController(Controller):
    name = 'ClimateController'

    def __init__(self):
        super().__init__()

    def control_climate(self, desired_temperature: float, desired_humidity: float):
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
        print("ClimateController update")
        # TODO: muss befüllt werden mit Logik
