class Animal:
    def __init__(self, days: int, name: str, health: int, size: str, color: str):
        self.days = days
        self.name = name
        self.health = health
        self.size = size
        self.color = color


class Cow(Animal):
    def __init__(self, days: int, name: str, health: int, size: str, color: str, walk: int, litres: int ):
        super().__init__(days, name, health, size, color)
        self.walk = walk
        self.litres = litres


    def create_milk(self) -> int:
        self.count_of_milk = self.days * self.litres
        return self.count_of_milk
class Horse(Animal):
    def __init__(self, days: int, name: str, health: int, size: str, color: str, hour: int, speed: int = 71):
        super().__init__(days, name, health, size, color)
        self.hour = hour
        #self.distance = distance
        self.speed = speed
    def run(self) -> int:
        self.distance = self.speed * self.hour
        return f"My horse {self.name} can walk {self.distance} in {self.hour}"
class Chicken(Animal):
    def __init__(self, days: int, name: str, health: int, size: str, color: str, create_eags=5 ):
        super().__init__(days, name, health, size, color)
        self.create_eags = create_eags
    def make_eags(self) -> int:
        self.count_eags = self.days * self.create_eags
        return self.count_eags


