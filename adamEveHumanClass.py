class Human():
    def __init__(self, man=None, woman=None):
        self.man = man
        self.woman = woman


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    Adam = Man()
    Eve = Woman()
    return [Adam, Eve]


# def God():
#     return [Man(), Woman()]
#
#
# class Human(object):
#     pass
#
#
# class Man(Human):
#     pass
#
#
# class Woman(Human):
#     pass