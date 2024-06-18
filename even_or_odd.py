class EvenOrOdd:
    def __call__(self, number: int) -> int:
        return self.even_or_odd(number)
    def __getitem__(self, number: int) -> int:
        return self.even_or_odd(number)
    def even_or_odd(self, number: int) -> int:
        return "Even" if number % 2 == 0 else "Odd"

even_or_odd = EvenOrOdd()


# class EvenOrOdd:
#     def __call__(self, num):
#         return "Even" if num % 2 == 0 else "Odd"
#
#     def __getitem__(self, num):
#         return self(num)
#
# even_or_odd = EvenOrOdd()