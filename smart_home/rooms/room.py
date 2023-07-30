from typing import List

from smart_home.logging.logger import LoggerFactory
from smart_home.rooms.zone import Zone


class Room:

    def __init__(self, name: str, room_type: str = "liveable"):
        self.name = name
        self.type = room_type
        self.zones: List[Zone] = []
        self.logger = LoggerFactory.setup_logger(name)
        self.logger.info(f'Created room {self.name} of type {self.type}')

    def append_zone(self, zone):
        self.logger.info(f'Adding zone {zone.name} to room {self.name}')
        self.zones.append(zone)

    def get_zones(self) -> list[Zone]:
        return self.zones
