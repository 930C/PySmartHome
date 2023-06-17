from abc import abstractmethod

from smart_home.interfaces.switchable_device_interface import SwitchableDeviceInterface


class AdjustableDeviceInterface(SwitchableDeviceInterface):

        @abstractmethod
        def set_level(self, value: float):  # -> float 0.0 - 1.0
            pass

        @abstractmethod
        def get_level(self):
            pass
