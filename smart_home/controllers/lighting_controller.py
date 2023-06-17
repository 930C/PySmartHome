from smart_home.controllers.controller import Controller


class LightingController(Controller):
    def __init__(self, devices: list, sensors: list):
        super().__init__(devices, sensors)

    def control_lighting(self, desired_brightness: float):
        for sensor in self.sensors:
            if sensor.read() < desired_brightness:
                for device in self.devices:
                    device.switch_on()
            elif sensor.read() > desired_brightness:
                for device in self.devices:
                    device.switch_off()