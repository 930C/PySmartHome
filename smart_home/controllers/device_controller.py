from smart_home.devices.device import Device

#Dependency Inversion Principle (DIP) -> Device Controller nur von Devices abhängig (geringe Abhängigkeiten)
#Interface Segregation Principle (ISP) -> jeder Controller nutzt nur benötigten Methoden (schmales Interface)
class DeviceController:
    def __init__(self, device):
        self.device = device

    def toggle_device(self):
        if isinstance(self.device, Device):
            self.device.toggle()
        else:
            raise Exception("Device does not support toggling.")
