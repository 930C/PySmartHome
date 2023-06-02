from smart_home.devices.device import Device


class DeviceController:
    def __init__(self, device):
        self.device = device

    def toggle_device(self):
        if isinstance(self.device, Device):
            self.device.toggle()
        else:
            raise Exception("Device does not support toggling.")
