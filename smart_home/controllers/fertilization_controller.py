from smart_home.controllers.controller import Controller


class FertilizationController(Controller):
    name = "FertilizationController"
    desired_nutrient_content: float = 1.0

    def __init__(self):
        super().__init__()

    def control_fertilization(self):
        for sensor in self.sensors:
            if sensor.get_value() < self.desired_nutrient_content:
                # TODO: Wenn KI-Daten da je nach dessen Ansage düngen
                for device in self.devices:
                    device.fertilize(1)
            elif sensor.get_value() >= self.desired_nutrient_content:
                for device in self.devices:
                    if device.get_state():
                        device.stop_fertilizing()

    def update(self):
        self.control_fertilization()
