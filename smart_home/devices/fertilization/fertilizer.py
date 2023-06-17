from smart_home.devices.switchable_device import SwitchableDevice


class Fertilizer(SwitchableDevice):
    def __init__(self, name: str):
        super().__init__(name)
