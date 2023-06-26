from smart_home.controllers.controller import Controller
from smart_home.logging.logger import setup_logger


class FertilizationController(Controller):
    logger = setup_logger("FertilizationController")
    name = "FertilizationController"

    def __init__(self, desired_nutrient_content: float = 70):
        super().__init__()
        self.desired_nutrient_content = desired_nutrient_content
        self.logger.info(f"Created controller {self.name} with desired nutrient content "
                         f"{self.desired_nutrient_content}")

    def control_fertilization(self):
        self.logger.info(f"Controlling fertilization with desired nutrient content "
                         f"{self.desired_nutrient_content}")
        for sensor in self.sensors:
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
        self.logger.info(f"Updating {self.name}..")
        self.control_fertilization()
