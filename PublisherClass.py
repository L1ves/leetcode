class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f"{self.name} ({self.location})"

    def publish(self, message):
        print(f"Готовим '{message}' к публикации в {self.get_info()}")


class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, title, author):
        print(f"Передаем рукопись '{title}', написанную автором {author} в {self.get_info()}")


class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, main_article):
        print(f"Печатаем свежий номер со статьей '{main_article}' на главной странице в издательстве {self.get_info()}")

