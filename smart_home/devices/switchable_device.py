from abc import ABC

from smart_home.interfaces.switchable_device_interface import SwitchableDeviceInterface


class SwitchableDevice(SwitchableDeviceInterface, ABC):
    def __init__(self, name: str):
        self.name = name
        self.state = False

    def turn_on(self):
        self.state = True
        print(f"{self.name} turned on")

    def turn_off(self):
        self.state = False
        print(f"{self.name} turned off")

    def get_state(self):
        return self.state

