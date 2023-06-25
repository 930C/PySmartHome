import pytest

from smart_home.devices.adjustable_device import AdjustableDevice

def test_set_level_regular():
    device = AdjustableDevice("test_device")
    device.set_level(0.5)
    assert device.value == 0.5

def test_set_level_to_low():
    device = AdjustableDevice("test_device")
    device.set_level(-0.5)
    assert device.value == 0.0

def test_set_level_to_high():
    device = AdjustableDevice("test_device")
    device.set_level(1.5)
    assert device.value == 1.0

def test_get_level():
    device = AdjustableDevice("test_device")
    assert device.get_level() == 1.0

def test_increase_level():
    device = AdjustableDevice("test_device", 0.1)
    device.increase_level(0.5)
    assert device.value == 0.6

def test_decrease_level():
    device = AdjustableDevice("test_device", 0.5)
    device.decrease_level(0.1)
    assert device.value == 0.4