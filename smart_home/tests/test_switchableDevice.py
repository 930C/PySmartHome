import pytest

from smart_home.devices.switchable_device import SwitchableDevice

def test_turn_on():
    device = SwitchableDevice("test_device")
    device.turn_on()
    assert device.state == True

def test_turn_off():
    device = SwitchableDevice("test_device")
    device.turn_on()
    assert device.state == True
    device.turn_off()
    assert device.state == False

def test_get_state():
    device = SwitchableDevice("test_device")
    assert device.get_state() == False
    device.turn_on()
    assert device.get_state() == True