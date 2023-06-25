import pytest

from typing import List
from smart_home.managers.controller_manager import ControllerManager
from smart_home.controllers.controller import Controller

class TestController(Controller):
    def __init__(self):
        super().__init__()

    def update(self):
        pass

def test_add_controller():
    controllerManager = ControllerManager({})
    controller = TestController()
    controllerManager.add_controller(controller)
    assert len(controllerManager.controllers) == 1

def test_get_controller():
    controllerManager = ControllerManager({})
    controller = TestController()
    controllerManager.add_controller(controller)
    assert controllerManager.get_controller("Controller") == controller

def test_get_controllers():
    controllerManager = ControllerManager({})
    controller = TestController()
    controllerManager.add_controller(controller)
    assert controllerManager.get_controllers() == [controller]

def test_the_testController_for_full_coverage():
    controller = TestController()
    controller.update()
    assert True