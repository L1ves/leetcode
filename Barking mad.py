# Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.
#
# snoopy.bark() #return "Woof"
# scoobydoo.bark() #undefined

class Dog():
    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        return f"Woof"


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")