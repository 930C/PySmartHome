from smart_home.devices.device import Device

class Sensor(Device):
    def __init__(self, device_id, name, value):
        super().__init__(device_id, name)
        self.value = value

    def get_value(self):
        return self.value
