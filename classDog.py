class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.color = coat_color
    def __str__(self):
        return f"{self.name}s age is {self.age}"


class Car:
    def __init__(self, color: str, mileage: int = 0):
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f"The {self.color} car has {self.mileage} miles."

    def drive(self, new_mileage: int):
        self.mileage += new_mileage


class Dog:
    species =  "Canis familiaris"

    def __init__(self, name, age, bread):
        self.name = name
        self.age = age
        self.bread = bread
    def __str__(self):
        return f"{self.name}s age is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussel(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Taksa(Dog):
    def speak(self, sound="Tyaf-Tyaf"):
        return f"{self.name} says {sound}"

class BullDog(Dog):
    def speak(self, sound="Buf-Buff"):
        return f"{self.name} says {sound}"

