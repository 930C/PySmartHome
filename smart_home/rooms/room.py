from smart_home.rooms.zone import Zone


class Room:
    def __init__(self, name: str, room_type: str = "liveable"):
        self.name = name
        self.type = room_type
        self.zones = []

    def append_zone(self, zone):
        self.zones.append(zone)
