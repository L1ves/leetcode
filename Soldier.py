RANKS = ["рядовой", "ефрейтор", "младший сержант", "сержант", "старший сержант",
         "прапорщик", "старший прапорщик"]
class Soldier:
    def __init__(self, name, rank, service_number):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def get_rank(self):
        return self.__rank

    def confirm_service_number(self, service_number):
        return self.__service_number == service_number

    def up_rank(self):
        ...

    def down_rank(self):
        ...