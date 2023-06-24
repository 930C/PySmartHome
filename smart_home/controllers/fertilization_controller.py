from smart_home.controllers.controller import Controller


class FertilizationController(Controller):
    name = "FertilizationController"

    def __init__(self, desired_nutrient_content: float = 70):
        super().__init__()
        self.desired_nutrient_content = desired_nutrient_content

    def control_fertilization(self):
        for sensor in self.sensors:
            print(sensor.name, " value: ", sensor.get_value())
            if sensor.get_value() < self.desired_nutrient_content:
                # TODO: Wenn KI-Daten da je nach dessen Ansage düngen
                for device in self.devices:
                    device.fertilize(1)
                    sensor.update(device)
            elif sensor.get_value() >= self.desired_nutrient_content:
                for device in self.devices:
                    if device.get_state():
                        device.stop_fertilizing()
                    sensor.update(device)

    def update(self):
        self.control_fertilization()
