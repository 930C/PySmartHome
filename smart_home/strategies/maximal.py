from smart_home.interfaces.strategy_interface import Strategy


class Maximal(Strategy):
    def calculate_value(self, data: []) -> float:
        # iterate over list and return maximal value
        max: float = 0
        for sensor in data:
            if sensor.get_value() > max:
                max = sensor.get_value()

        return max