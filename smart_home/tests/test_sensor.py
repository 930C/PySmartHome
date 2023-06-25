import pytest
from smart_home.sensors.sensor import Sensor
from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.devices.adjustable_device import AdjustableDevice

def setup_sensor():
    return Sensor("test_sensor", 100.0, True, 50.0, 150.0) 

def test_get_value():
    sensor = setup_sensor()
    assert sensor.get_value() == 100.0

def test_set_value_regular():
    sensor = setup_sensor()
    sensor.set_value(75.0)
    assert sensor.get_value() == 75.0

def test_set_value_too_low():
    sensor = setup_sensor()
    sensor.set_value(25.0)
    assert sensor.get_value() == 50.0

def test_set_value_too_high():
    sensor = setup_sensor()
    sensor.set_value(175.0)
    assert sensor.get_value() == 150.0

def test_update_switched_on_naturally_decrease_adjustable():
    sensor = setup_sensor()
    device = AdjustableDevice("test_device", 0.5, 0.1, 1.0)
    device.turn_on()
    sensor.update(device)
    assert sensor.get_value() == 102.5

def test_update_switched_on_naturally_decrease_switchable():
    sensor = setup_sensor()
    device = SwitchableDevice("test_device")
    device.turn_on()
    sensor.update(device)
    assert sensor.get_value() == 105.0

def test_update_switched_on_not_naturally_decrease_adjustable():
    sensor = setup_sensor()
    device = AdjustableDevice("test_device", 0.5, 0.1, 1.0)
    device.turn_on()
    sensor.naturally_decrease = False
    sensor.update(device)
    assert sensor.get_value() == 97.5

def test_update_switched_on_not_naturally_decrease_switchable():
    sensor = setup_sensor()
    device = SwitchableDevice("test_device")
    device.turn_on()
    sensor.naturally_decrease = False
    sensor.update(device)
    assert sensor.get_value() == 95.0

def test_update_switched_off_naturally_decrease():
    sensor = setup_sensor()
    device = SwitchableDevice("test_device")
    sensor.update(device)
    assert sensor.get_value() < 100.0

def test_update_switched_off_not_naturally_decrease():
    sensor = setup_sensor()
    device = SwitchableDevice("test_device")
    sensor.naturally_decrease = False
    sensor.update(device)
    assert sensor.get_value() > 100.0