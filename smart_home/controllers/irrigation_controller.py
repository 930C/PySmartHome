from smart_home.controllers.controller import Controller


class IrrigationController(Controller):
    name = 'IrrigationController'

    def __init__(self):
        super().__init__()

    def control_irrigation(self, desired_moisture: float):
        for sensor in self.sensors:
            if sensor.read() < desired_moisture:
                for device in self.devices:
                    device.switch_on()
            elif sensor.read() > desired_moisture:
                for device in self.devices:
                    device.switch_off()
