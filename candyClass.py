class Candy:
    def __init__(self, name: str, price: float, weight: int):
        self.name = name
        self.price = price
        self.weight = weight

class Chocolate(Candy):
    def __init__(self, name, price, weight, cocoa_percentage: int, chocolate_type: str):
        super().__init__(name, price, weight)
        self.chocolate_type = chocolate_type
        self.cocoa_percentage = cocoa_percentage
class Gummy(Candy):
    def __init__(self, name, price, weight, flavor: str, shape: str):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.shape = shape

class HardCandy(Candy):
    def __init__(self, name, price, weight, flavor, filled):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.filled = filled
