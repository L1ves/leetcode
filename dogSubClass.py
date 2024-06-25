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
        return super().speak(sound)

class Taksa(Dog):
    def speak(self, sound="Tyaf-Tyaf"):
        return super().speak(sound)
class BullDog(Dog):
    def speak(self, sound="Buf-Buff"):
        return super().speak(sound)


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)