from smart_home.config.config_loader import ConfigLoader, DeviceFactory
from smart_home.controllers.controller import Controller
from smart_home.managers.controller_manager import ControllerManager
from smart_home.rooms.room import Room
from smart_home.rooms.zone import Zone


class SmartHomeController:
    def __init__(self, config_file_path: str):
        self.rooms = []
        self.load_rooms(config_file_path)

    # TODO: Auslagern
    def load_rooms(self, config_file_path: str) -> None:
        config_data = ConfigLoader.load_config(config_file_path)

        for room_info in config_data.get('rooms', []):
            room = Room(room_info['name'], room_info['type'])
            for zone_info in room_info.get('zones', []):
                controllerManager = ControllerManager({})
                for device_info in zone_info.get('devices', []):
                    device = DeviceFactory.create_device(device_info)

                    controller_class = DeviceFactory.controller_classes.get(type(device), Controller)
                    if controllerManager.controllers.get(controller_class.name) is None:
                        controller = controller_class()
                        controller.add_device(device)
                        controllerManager.add_controller(controller)
                    else:
                        controller = controllerManager.controllers.get(controller_class.name)
                        controller.add_device(device)

                # TODO: Eigene Sensor Factory?
                for sensor_info in zone_info.get('sensors', []):
                    sensor = DeviceFactory.create_sensor(sensor_info)

                    controller_class = DeviceFactory.sensor_controller_classes.get(type(sensor), Controller)
                    if controllerManager.controllers.get(controller_class.name) is None:
                        controller = controller_class()
                        controller.add_sensor(sensor)
                        controllerManager.add_controller(controller)
                    else:
                        controller = controllerManager.controllers.get(controller_class.name)
                        controller.add_sensor(sensor)

                zone = Zone(zone_info['name'], controllerManager)

                room.append_zone(zone)
            self.rooms.append(room)

    def update(self):
        for room in self.rooms:
            for zone in room.zones:
                zone.update()
