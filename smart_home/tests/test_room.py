import pytest

from smart_home.rooms.room import Room
from smart_home.rooms.zone import Zone
from smart_home.managers.controller_manager import ControllerManager

def test_append_zone():
    room = Room("test_room")
    controllerManager = ControllerManager({})
    zone = Zone("test_zone", controllerManager)
    room.append_zone(zone)
    assert len(room.zones) == 1