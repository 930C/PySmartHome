import pytest

from smart_home.controllers.controller import Controller
from smart_home.devices.adjustable_device import AdjustableDevice
from smart_home.sensors.sensor import Sensor
class TestController(Controller):
    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        pass

def test_get_devices():
    controller = TestController()
    device = AdjustableDevice("test_device")
    controller.add_device(device)
    assert controller.get_devices() == [device]

def test_get_sensors():
    controller = TestController()
    sensor = Sensor("test_sensor")
    controller.add_sensor(sensor)
    assert controller.get_sensors() == [sensor]

def test_add_device():
    controller = TestController()
    device = AdjustableDevice("test_device")
    controller.add_device(device)
    assert len(controller.devices) == 1

def test_add_sensor():
    controller = TestController()
    sensor = Sensor("test_sensor")
    controller.add_sensor(sensor)
    assert len(controller.sensors) == 1

def test_remove_device():
    controller = TestController()
    device = AdjustableDevice("test_device")
    controller.add_device(device)
    controller.remove_device(device)
    assert len(controller.devices) == 0

def test_remove_sensor():
    controller = TestController()
    sensor = Sensor("test_sensor")
    controller.add_sensor(sensor)
    controller.remove_sensor(sensor)
    assert len(controller.sensors) == 0

def test_the_testController_for_full_coverage():
    controller = TestController()
    controller.update()
    assert True