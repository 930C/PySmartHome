from smart_home.controllers.controller import Controller
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface


class ClimateController(Controller):
    def __init__(self, devices: list, sensors: list):
        super().__init__(devices, sensors)

    def control_climate(self, desired_temperature: float, desired_humidity: float):
        for sensor in self.sensors:
            if sensor.read() < desired_temperature:
                for device in self.devices:
                    device.switch_on()
                    if isinstance(device, TemperatureControlInterface):
                        device.heat()
            elif sensor.read() > desired_temperature:
                for device in self.devices:
                    device.switch_on()  # TODO: Jo muss überprüfen welche devices an oder aus gehen soll
                    if isinstance(device, TemperatureControlInterface):
                        device.cool()
