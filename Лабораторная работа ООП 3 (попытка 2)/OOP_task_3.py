class Book:
    """Базовый класс книги"""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Объем {self._pages} страниц."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self._duration} часов."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"


book1 = PaperBook('A Byte of Python', 'Swaroop Chitlur', 164)
book2 = AudioBook('Начала Python', 'Петр Питонов', 999.9)

print(book1.__str__())
print(book1.__repr__())

print()

print(book2.__str__())
print(book2.__repr__())