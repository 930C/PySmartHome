import os.path
import time
import json
from typing import List

from smart_home.KI.floraGPT_adapter import PlantCareAdapter
from smart_home.commands.plant_care_command import PlantCareCommand
from smart_home.config.config_loader import ConfigLoader, DeviceFactory
from smart_home.controllers.controller import Controller
from smart_home.logging.logger import LoggerFactory
from smart_home.managers.controller_manager import ControllerManager
from smart_home.rooms.room import Room
from smart_home.rooms.zone import Zone
from smart_home.sensors.fertilization_sensor import FertilizationSensor
from smart_home.sensors.humidity_sensor import HumiditySensor
from smart_home.sensors.irrigation_sensor import IrrigationSensor
from smart_home.sensors.temperature_sensor import TemperatureSensor


class SmartHomeController:
    sensor_measures = {
        TemperatureSensor: 'temperature',
        HumiditySensor: 'humidity',
        FertilizationSensor: 'fertilization',
        IrrigationSensor: 'irrigation',
    }

    controller_influences = {
        'temperature': "ClimateController",
        'humidity': "ClimateController",
        'fertilization': "FertilizationController",
        'irrigation': "IrrigationController",
    }

    def __init__(self, config_file_path: str):
        self.adapter = None
        self.rooms: List[Room] = []
        self.logger = LoggerFactory.setup_logger('SmartHomeController')
        self.config_file_path = config_file_path
        self.last_config_modification_time = os.path.getmtime(config_file_path)
        self.load_rooms(config_file_path)
        self.logger.info(f'Created SmartHomeController with config file {config_file_path}')
        self.load_zone_data_from_json()

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

    def config_changed(self):
        current_config_modification_time = os.path.getmtime(self.config_file_path)
        if current_config_modification_time != self.last_config_modification_time:
            self.last_config_modification_time = current_config_modification_time
            return True
        return False

    def reload_config(self):
        self.logger.debug(f'Reloading configuration from {self.config_file_path}')
        self.rooms = []  # Verwerfen der alten Zimmer und Controller
        self.load_rooms(self.config_file_path)  # Laden der neuen Zimmer und Controller aus der Konfigurationsdatei
        self.load_zone_data_from_json()  # Laden der vorhandenen Zonendaten in die neuen Controller
        self.logger.debug(f'Reloaded configuration from {self.config_file_path}')

    def start(self):
        self.adapter = PlantCareAdapter()
        try:
            while True:
                time.sleep(5)
                self.logger.info('-' * 100)
                self.logger.debug('Updating SmartHomeController..')

                if self.config_changed():
                    self.logger.warn("CONFIGURATION CHANGED!")
                    self.reload_config()
                    self.logger.info("Configuration reloaded due to detected changes in the configuration file.")

                for room in self.rooms:
                    self.logger.info('Updating room: ' + room.name)
                    for zone in room.zones:
                        self.logger.info('Updating zone: ' + zone.name)

                        for controller in zone.controllerManager.get_controllers():
                            self.logger.info('Updating controller: ' + controller.name)
                            controller.update()

                        care_instruction: PlantCareCommand = self.adapter.getPlantCareInstructions("kein Bild")
                        care_instruction.execute(zone.controllerManager)
                self.logger.info('Updated SmartHomeController.')

                self.save_zone_data_to_json()  # Save zone data to json after every update
                self.logger.info("Saved zone data to json.")
        except KeyboardInterrupt:
            self.logger.info('KeyboardInterrupt received. Exiting.')
            exit(0)

    def load_zone_data_from_json(self):
        filename = "resources/zone_data.json"
        try:
            with open(filename, "r") as file:
                data = json.load(file)

                room_dict = {room.name: room for room in self.rooms}
                for room_data in data:
                    room_name = room_data.get("roomName")
                    if room_name in room_dict:
                        room = room_dict.get(room_name)
                        zone_dict = {zone.name: zone for zone in room.zones}
                        for zone_data in room_data.get("zones"):
                            zone_name = zone_data.get("zoneName")
                            if zone_name in zone_dict:
                                zone = zone_dict.get(zone_name)
                                for sensor in zone.controllerManager.get_sensors():
                                    saved_sensor_value = zone_data.get(sensor.measures)
                                    if saved_sensor_value is not None:
                                        sensor.value = saved_sensor_value
                                        self.logger.info(f"Set {sensor.name} value to {saved_sensor_value}")

            self.logger.info("Loaded zone data from json.")
        except FileNotFoundError:
            self.logger.error(f"File {filename} not found. Using default values.")

    def save_zone_data_to_json(self):
        filename = "resources/zone_data.json"
        room_data = []
        for room in self.rooms:
            room_entry = {"roomName": room.name, "zones": []}
            for zone in room.zones:
                zone_entry = {"zoneName": zone.name}
                for sensor_class, measure in self.sensor_measures.items():
                    controller = zone.controllerManager.get_controller(self.controller_influences.get(measure))
                    if controller is None:
                        zone_entry[measure] = None
                        continue
                    sensor_value = controller.get_strategy().calculate_value(controller.get_sensors(), sensor_class)
                    zone_entry[measure] = sensor_value
                    self.logger.info(f"Saved zone data for zone {zone.name} and measure {measure} with value {sensor_value}")
                room_entry["zones"].append(zone_entry)
            room_data.append(room_entry)

        with open(filename, 'w') as f:
            json.dump(room_data, f, indent=4)
