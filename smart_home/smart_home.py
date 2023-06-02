class SmartHome:
    def __init__(self):
        self.devices = []
        self.device_controllers = []

    def add_device(self, device, controller):
        self.devices.append(device)
        self.device_controllers.append(controller)

    def get_devices(self):
        return self.devices

    def get_controllers(self):
        return self.device_controllers

    def get_device_by_id(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None

    def get_controller_for_device(self, device):
        for i in range(len(self.devices)):
            if self.devices[i] == device:
                return self.device_controllers[i]
        return None

    def add_controller(self, controller):
        self.device_controllers.append(controller)

