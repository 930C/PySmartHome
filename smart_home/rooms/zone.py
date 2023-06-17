from smart_home.managers.controller_manager import ControllerManager


class Zone:
    def __init__(self, name: str, controllerManager: ControllerManager):
        self.name = name
        self.controllerManager = controllerManager
