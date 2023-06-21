from smart_home.rooms.zone import Zone


class Room:
    def __init__(self, name: str, room_type: str = "liveable"):
        self.name = name
        self.type = room_type
        self.zones = []

    def add_zone(self, zone: Zone):
        self.zones.append(zone)

    def append_zone(self, zone):
        self.zones.append(zone)
