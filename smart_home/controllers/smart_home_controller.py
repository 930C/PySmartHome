from smart_home.config.config_loader import ConfigLoader, DeviceFactory
from smart_home.controllers.controller import Controller
from smart_home.logging.logger import setup_logger
from smart_home.managers.controller_manager import ControllerManager
from smart_home.rooms.room import Room
from smart_home.rooms.zone import Zone
import time


class SmartHomeController:
    logger = setup_logger(__name__)

    def __init__(self, config_file_path: str):
        self.logger.info('Initializing SmartHomeController..')
        self.rooms = []
        self.load_rooms(config_file_path)

    # TODO: Auslagern
    def load_rooms(self, config_file_path: str) -> None:
        self.logger.info('Loading rooms..')
        config_data = ConfigLoader.load_config(config_file_path)

        for room_info in config_data.get('rooms', []):
            room = Room(room_info['name'], room_info['type'])
            self.logger.info('Loading room: ' + room.name)
            for zone_info in room_info.get('zones', []):
                controller_manager = ControllerManager({})
                self.logger.info('Loading zone: ' + zone_info['name'])
                for device_info in zone_info.get('devices', []):
                    device = DeviceFactory.create_device(device_info)
                    self.logger.info('Loading device: ' + device.name)

                    controller_class = DeviceFactory.controller_classes.get(type(device), Controller)
                    if controller_manager.controllers.get(controller_class.name) is None:
                        controller = controller_class()
                        controller.add_device(device)
                        controller_manager.add_controller(controller)
                    else:
                        controller = controller_manager.controllers.get(controller_class.name)
                        controller.add_device(device)

                    self.logger.info('Added device: ' + device.name + ' to controller: ' + controller.name)
                # TODO: Eigene Sensor Factory?
                for sensor_info in zone_info.get('sensors', []):
                    sensor = DeviceFactory.create_sensor(sensor_info)
                    self.logger.info('Loading sensor: ' + sensor.name)

                    controller_class = DeviceFactory.sensor_controller_classes.get(type(sensor), Controller)
                    if controller_manager.controllers.get(controller_class.name) is None:
                        controller = controller_class()
                        controller.add_sensor(sensor)
                        controller_manager.add_controller(controller)
                    else:
                        controller = controller_manager.controllers.get(controller_class.name)
                        controller.add_sensor(sensor)
                    self.logger.info('Added sensor: ' + sensor.name + ' to controller: ' + controller.name)

                zone = Zone(zone_info['name'], controller_manager)

                room.append_zone(zone)
                self.logger.info('Added zone: ' + zone.name + ' to room: ' + room.name)
            self.rooms.append(room)
            self.logger.info('Added room: ' + room.name)

    def update(self):
        while True:
            self.logger.info('Updating SmartHomeController..')

            for room in self.rooms:
                self.logger.info('Updating room: ' + room.name)
                for zone in room.zones:
                    self.logger.info('Updating zone: ' + zone.name)
                    for controller in zone.controllerManager.get_controllers():
                        self.logger.info('Updating controller: ' + controller.name)
                        controller.update()
            time.sleep(5)
            print(" ")
            self.logger.info('Updated SmartHomeController..')

