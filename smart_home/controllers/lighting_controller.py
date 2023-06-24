from smart_home.controllers.controller import Controller


class LightingController(Controller):
    name = 'LightingController'

    def __init__(self):
        super().__init__()

    def control_lighting(self, desired_brightness: float):
        for sensor in self.sensors:
            if sensor.read() < desired_brightness:
                for device in self.devices:
                    device.switch_on()
            elif sensor.read() > desired_brightness:
                for device in self.devices:
                    device.switch_off()

    def update(self):
        print("LightingController update")
