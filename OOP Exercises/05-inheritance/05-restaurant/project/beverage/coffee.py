from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.COFFEE_PRICE, self.COFFEE_MILLILITERS)
        self.caffeine = caffeine
