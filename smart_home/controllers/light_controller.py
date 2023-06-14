from smart_home.devices.light import Light
from smart_home.controllers.device_controller import DeviceController

#Interface Segregation Principle (ISP) -> jeder Controller nutzt nur benötigten Methoden (schmales Interface)
class LightController(DeviceController):
    def __init__(self, light):
        if not isinstance(light, Light):
            raise Exception("Invalid device type for LightController.")
        super().__init__(light)

    def change_color(self, color):
        self.device.color = color

    def change_brightness(self, brightness):
        if 0 <= brightness <= 100:
            self.device.brightness = brightness
        else:
            raise Exception("Brightness value must be between 0 and 100.")
