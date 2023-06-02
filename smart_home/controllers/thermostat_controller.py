from smart_home.controllers.device_controller import DeviceController
from smart_home.devices.thermostat import Thermostat


class ThermostatController(DeviceController):
    def __init__(self, thermostat):
        if not isinstance(thermostat, Thermostat):
            raise Exception("Invalid device type for Thermostat.")
        super().__init__(thermostat)

    def change_temperature(self, temperature):
        self.device.change_temperature(temperature)
