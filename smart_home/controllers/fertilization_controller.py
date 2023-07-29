from smart_home.controllers.controller import Controller
from smart_home.sensors.fertilization_sensor import FertilizationSensor


class FertilizationController(Controller):
    name = "FertilizationController"

    def __init__(self, desired_nutrient_content: float = 70):
        super().__init__()
        self.desired_nutrient_content = desired_nutrient_content
        self.logger.info(f"Created controller {self.name} with desired nutrient content "
                         f"{self.desired_nutrient_content}")

    def control_fertilization(self):
        self.logger.info(f"Controlling fertilization with desired nutrient content "
                         f"{self.desired_nutrient_content}")
        if len(self.sensors) is not 0:
            sensor_value = self.getStrategy().calculate_value(self.sensors, FertilizationSensor)

            for device in self.devices:
                if sensor_value < self.desired_nutrient_content:
                    device.fertilize(1)
                elif sensor_value >= self.desired_nutrient_content:
                    if device.get_state():
                        device.stop_fertilizing()
                for sensor in self.sensors:
                    sensor.update(device)

    def update(self):
        self.logger.info(f"Updating {self.name}..")
        self.control_fertilization()
