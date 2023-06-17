from typing import List

from smart_home.controllers.controller import Controller


class ControllerManager:    # Solid Principle: Single Responsibility
    def __init__(self):
        self.controllers = {}

    def add_controller(self, controller: Controller):
        self.controllers[controller.name] = controller

    def get_controller(self, name: str) -> Controller:
        return self.controllers[name]

    def get_controllers(self) -> List[Controller]:
        return list(self.controllers.values())