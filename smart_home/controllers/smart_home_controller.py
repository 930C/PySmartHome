from smart_home.config.config_loader import ConfigLoader, DeviceFactory
from smart_home.controllers.controller import Controller
from smart_home.logging.logger import setup_logger
from smart_home.managers.controller_manager import ControllerManager
from smart_home.rooms.room import Room
from smart_home.rooms.zone import Zone
import time


class SmartHomeController:
    logger = setup_logger('SmartHomeController')

    def __init__(self, config_file_path: str):
        self.rooms = []
        self.load_rooms(config_file_path)
        self.logger.info(f'Created SmartHomeController with config file {config_file_path}')

    # TODO: Auslagern
    def load_rooms(self, config_file_path: str) -> None:
        self.logger.info('Loading rooms..')
        config_data = ConfigLoader.load_config(config_file_path)

        for room_info in config_data.get('rooms', []):
            self.logger.info(f'Loading room: {room_info["name"]}, type: {room_info["type"]}')
            room = Room(room_info['name'], room_info['type'])
            for zone_info in room_info.get('zones', []):
                controller_manager = ControllerManager({})
                self.logger.info(f'Loading zone: {zone_info["name"]}')
                for device_info in zone_info.get('devices', []):
                    self.logger.info(f'Loading device: {device_info["name"]}. Type: {device_info["type"]}')
                    device = DeviceFactory.create_device(device_info)

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
                    self.logger.debug(f'Loading sensor: {sensor_info["name"]}. Type: {sensor_info["type"]}')
                    sensor = DeviceFactory.create_sensor(sensor_info)

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
            self.logger.info(f'Added room: {room.name} to SmartHomeController')

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
            self.logger.info('Updated SmartHomeController..')

