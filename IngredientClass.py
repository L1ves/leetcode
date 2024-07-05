from abc import ABC, abstractmethod
class Ingredient(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

class Vegetable(Ingredient):
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight
    def get_name(self):
        return f"{self.type}"
    def get_quantity(self):
        return f"{self.weight} кг"
class Fruit(Ingredient):
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight
    def get_name(self):
        return f"{self.type}"

    def get_quantity(self):
        return f"{self.weight} кг"

# from abc import ABC, abstractmethod
# class Ingredient(ABC):
#     def __init__(self, type, weight):
#         self.type = type
#         self.weight = weight
#     @abstractmethod
#     def get_name(self):
#         pass
#
#     @abstractmethod
#     def get_quantity(self):
#         pass
#
# class Vegetable(Ingredient):
#     def get_name(self):
#         return f"{self.type}"
#     def get_quantity(self):
#         return f"{self.weight} кг"
# class Fruit(Ingredient):
#     def get_name(self):
#         return f"{self.type}"
#
#     def get_quantity(self):
#         return f"{self.weight} кг"
