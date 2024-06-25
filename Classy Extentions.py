Task

#Your task is to complete the Cat class which Extends Animal and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'

from preloaded import Animal


class Cat(Animal):
    def speak(self):
        return f'{self.name} meows.'
