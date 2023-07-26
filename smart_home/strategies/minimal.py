from smart_home.interfaces.strategy_interface import Strategy


class Minimal(Strategy):
    def calculate_value(self, data: []) -> float:
        # iterate over list and return minimal value
        min: float = 100
        for sensor in data:
            if sensor.get_value() < min:
                min = sensor.get_value()

        return min