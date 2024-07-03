class Employee:
    def __init__(self, name, age, salary, bonus=None):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def get_name(self):
        return self.__name  # – возвращает имя сотрудника;

    def get_age(self):
        return self.__age  # – возвращает возраст;

    def get_salary(self):
        return self.__salary  # – возвращает зарплату сотрудника;

    def set_bonus(self, bonus):
        self.__bonus = bonus
        # return self.bonus  # – устанавливает свойство bonus;

    def get_bonus(self):
        return self.__bonus  # – возвращает бонус для сотрудника;

    def get_total_salary(self):
        return self.__salary + self.__bonus  # – возвращает общую зарплату сотрудника (оклад + бонус)