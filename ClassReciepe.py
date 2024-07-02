class Recipe:
    def __init__(self, reciepe, ingredients):
        self.reciepe = reciepe
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f"Ингредиенты для {self.reciepe}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"Сегодня мы готовим {self.reciepe}.")
        print(f"Выполняем инструкцию по приготовлению блюда {self.reciepe}...")
        print(f"Блюдо {self.reciepe} готово!")

