from abc import ABC, abstractmethod
class Starship(ABC):
    @abstractmethod
    def warp_speed(self):
        pass

    @abstractmethod
    def fire_weapon(self):
        pass

    @abstractmethod
    def self_destruct(self):
        pass

class FederationStarship(Starship):
    def warp_speed(self):
        print(f"Включить варп-двигатели!")

    def fire_weapon(self):
        print(f"Выпустить фотонные торпеды!")


    def self_destruct(self):
        print(f"Запускаю систему самоуничтожения...")


class KlingonWarship(Starship):

    def warp_speed(self):
        print(f"Включить маскировочное устройство!")

    def fire_weapon(self):
        print(f"Стрелять из фазеров!")



    def self_destruct(self):
        print(f"Запускаю протокол самоуничтожения...")