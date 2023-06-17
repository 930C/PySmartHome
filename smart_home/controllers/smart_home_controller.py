from smart_home.config.config_loader import ConfigLoader, DeviceFactory
from smart_home.controllers.climate_controller import ClimateController
from smart_home.controllers.fertilization_controller import FertilizationController
from smart_home.controllers.irrigation_controller import IrrigationController

from smart_home.controllers.lighting_controller import LightingController
from smart_home.managers.controller_manager import ControllerManager
from smart_home.rooms.room import Room
from smart_home.rooms.zone import Zone


class SmartHomeController:
    def __init__(self, config_file_path: str):
        self.rooms = self.load_rooms(config_file_path)

    def load_rooms(self, config_file_path: str):
        config_data = ConfigLoader.load_config(config_file_path)

        for room_info in config_data.get('rooms', []):
            room = Room(room_info['name'], room_info['type'])
            for zone_info in room_info.get('zones', []):
                controllerManager = ControllerManager()

                controllers = []
                climateController = ClimateController([], [])
                fertilizerController = FertilizationController([], [])
                irrigationController = IrrigationController([], [])
                lightController = LightingController([], [])


                for device_info in zone_info.get('devices', []):
                    device = DeviceFactory.create_device(device_info)
                    controller = DeviceFactory.create_controller(device)
                    controller.add_device(device)

                    # TODO: Hier müssen Sie die Controller den Geräten hinzufügen


                    controllerManager.add_controller(controller)



                zone = Zone(zone_info['name'], controllers)

                room.append_zone(zone)


        return rooms


    def update(self):
        for room in self.rooms:
            for zone in room.zones:
                zone.update()
        # Aktualisieren Sie alle Controller
        for controller in self.controllers:
            controller.update()
        # Loggen Sie den aktuellen Zustand
        self.logger.log_state(self.devices)

    def shutdown(self):
        # Schalten Sie alle Geräte sicher aus
        for room in self.rooms:
            for zone in room.zones:
                for controller in zone.controllerManager.controllers:
                    for device in controller.devices:
                        if isinstance(device, SwitchableDevice):
                            device.turn_off()
