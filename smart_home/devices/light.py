from .device import Device


class Light(Device):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.color = 0xFFFFFF
        self.brightness = 100
    