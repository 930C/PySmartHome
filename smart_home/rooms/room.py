from smart_home.logging.logger import setup_logger
from smart_home.rooms.zone import Zone


class Room:
    logger = setup_logger('Room')

    def __init__(self, name: str, room_type: str = "liveable"):
        self.name = name
        self.type = room_type
        self.zones = []
        self.logger.info(f'Created room {self.name} of type {self.type}')

    def append_zone(self, zone):
        Room.logger.info(f'Adding zone {zone.name} to room {self.name}')
        self.zones.append(zone)
