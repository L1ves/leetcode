class Sword:

    def __init__(self, name, blade_length, grip, material='сталь'):
        self.name = name
        self.blade_length = blade_length
        self.material = material
        self.grip = grip
        self.strength = 10
        print(f'Новый меч {name} выкован!')

    def slashing_blow(self):
        self.strength -= 10
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_length}.')

    def piercing_strike(self):
        self.strength -= 5
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    def sharpen(self):
        self.strength = 100
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.')

    # Вот он — новый метод! Именно в нём описывается то, что должно выводиться
    # при печати объекта.
    def __str__(self):
        # Можно задать любую строку, например
        # «Не печатай меня, ведь я — объект!».
        # Но лучше пусть при печати выводится что-то осмысленное,
        # например имя объекта и его основные параметры.
        return (
            f'Меч — «{self.name}». '
            f'Выкован из материала {self.material}, '
            f'длина клинка — {self.blade_length}, '
            f'прочность — {self.strength}.'
        )


katana = Sword('Верный', 1.5,
               'хват двумя руками')
classic_sword = Sword('Дежурный', 1.2,
                      'хват одной рукой')

# Печатаем созданные объекты.
print(katana)
print(classic_sword)