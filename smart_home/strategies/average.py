from smart_home.interfaces.strategy_interface import Strategy


class Average(Strategy):
    def calculate_value(self, data: []) -> float:
        #iterate over list and return average value
        sum: float = 0
        number_of_sensors: int = len(data)
        for sensor in data:
            sum += sensor.get_value()

        return sum / number_of_sensors