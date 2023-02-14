class BaseDog:
    """Создание и подготовка к работе базового класса Собака"""
    def __init__(self, name: str, size: float, purpose: list):
        """
        :param name: имя собаки
        :param size: высота в холке собаки в метрах
        :param purpose: назначение собаки
        """
        self.name = name
        self.size = size
        self.purpose = purpose

    @property
    def name(self):
        """Создание геттера для атрибута name"""
        return self._name

    @name.setter
    def name(self, name: str):
        """Создание cеттера для атрибута name с проверкой name на то, что он состоит из 1-200 букв"""
        if not name.isalpha():
            raise TypeError("Имя должно состоять из букв!")
        if len(name) > 200:
            raise ValueError("Длина имени должна не превышать 200 букв!")
        self._name = name

    @property
    def size(self):
        """Создание геттера для атрибута size"""
        return self._size

    @size.setter
    def size(self, size: float):
        """Создание cеттера для атрибута size с проверкой size на то, что он является положительным числом с
        плавающей точкой, не большим 2"""
        if not isinstance(size, float):
            raise TypeError("Высота в холке должна быть типа float!")
        if size <= 0 or size > 2:
            raise ValueError("Высота в холке должна быть положительной величиной и не превышать 2 м!")
        self._size = size

    @property
    def purpose(self):
        """Создание геттера для атрибута purpose"""
        return self._purpose

    @purpose.setter
    def purpose(self, purpose: list):
        """Создание cеттера для атрибута purpose с проверкой purpose на то, что он является одной из заданных в
        списке purposes строк"""
        purposes = ['охотничья', 'служебная', 'терьер', 'декоративная', 'пастушья']
        if purpose not in purposes:
            raise ValueError("Неверное назначение!")
        self._purpose = purpose

    def __str__(self) -> str:
        """Создание метода, выводящего информацию о собаке в удобочитаемом формате"""
        return f"Собака: {self._name}. Высота в холке: {self._size} м. Назначение: {self._purpose}."

    def __repr__(self) -> str:
        """Создание метода, выводящего «официальный» текстовый образ объекта, который можно использовать для
        воссоздания этого объекта"""
        return f"{self.__class__.__name__}(name={self._name!r}, size={self._size!r}, purpose={self._purpose})"

    def size_in_feet(self) -> float:
        """Создание метода, переводящего значение высоты собаки в холке size из метров в футы; на случай
        использования информации на территориях, использующих американскую систему измерения"""
        return self.size * 3.28084

    def capitalize_name(self) -> str:
        """Создание метода, переводящего имя собаки name в слово, начинающееся с заглавной буквы с последующими
        строчными буквами; на случай, если будет ошибочно занесено иное"""
        return self.name.capitalize()


class FrenchBulldog(BaseDog):
    """Создание и подготовка к работе производного класса Французский бульдог"""
    def __init__(self, name: str, size: float, purpose: list):
        """
        :param name: наследуется от базового класса Собака
        :param size: наследуется от базового класса Собака
        :param purpose: наследуется от базового класса Собака
        """
        super().__init__(name, size, purpose)


class AfghanHound(BaseDog):
    """Создание и подготовка к работе производного класса Афганская борзая"""
    def __init__(self, name: str, size: float, purpose: list, tail_length: float, tail_shape: list):
        """
        :param name: наследуется от базового класса Собака
        :param size: наследуется от базового класса Собака
        :param purpose: наследуется от базового класса Собака
        :param tail_length: длина хвоста собаки в метрах
        :param tail_shape: форма хвоста собаки
        """
        super().__init__(name, size, purpose)
        self.tail_length = tail_length
        self.tail_shape = tail_shape

    @property
    def tail_length(self):
        """Создание геттера для атрибута tail_length"""
        return self._tail_length

    @tail_length.setter
    def tail_length(self, tail_length: float):
        """Создание cеттера для атрибута tail_length с проверкой tail_length на то, что он является положительным
        числом с плавающей точкой, не большим 1"""
        if not isinstance(tail_length, float):
            raise TypeError("Длина хвоста должна быть типа float!")
        if tail_length <= 0 or tail_length > 1:
            raise ValueError("Высота в холке должна быть положительной величиной и не превышать 1 м!")
        self._tail_length = tail_length

    @property
    def tail_shape(self):
        """Создание геттера для атрибута tail_shape"""
        return self._tail_shape

    @tail_shape.setter
    def tail_shape(self, tail_shape: list):
        """Создание cеттера для атрибута tail_shape с проверкой tail_shape на то, что он является одним из заданных в
        списке shapes строк"""
        shapes = ['саблевидный', 'крючок', 'полено', 'перо', 'прут', 'серп', 'кольцо', 'двойное кольцо']
        if tail_shape not in shapes:
            raise ValueError("Неверная форма хвоста!")
        self._tail_shape = tail_shape

    def __str__(self) -> str:
        """Перегрузка метода, выводящего информацию о собаке в удобочитаемом строковом формате, так как в вывод
        добавляются два новых параметра: tail_length и _tail_shape"""
        return f"Собака: {self._name}. Высота в холке: {self._size} м. Назначение: {self._purpose}. " \
               f"Длина хвоста: {self._tail_length} м. Форма хвоста: {self._tail_shape}."

    def __repr__(self) -> str:
        """Перегрузка метода, выводящего «официальный» текстовый образ объекта, который можно использовать для
        воссоздания этого объекта, так как в вывод добавляются два новых параметра: tail_length и _tail_shape"""
        return f"{self.__class__.__name__}(name={self._name!r}, size={self._size!r}, purpose={self._purpose!r}, " \
               f"tail_length={self._tail_length!r}, tail_shape={self._tail_shape})"

    def capitalize_name(self) -> str:
        """Перегрузка метода, переводящего имя собаки name в слово, начинающееся с заглавной буквы с последующими
        строчными буквами. Теперь метод переводит имя собаки name в слово, состоящее из одних заглавных букв. Это
        сделано с целью визуального выделения охотничьих пород собак среди других"""
        return self.name.upper()


dog1 = FrenchBulldog('арни', 0.381, 'декоративная')
dog2 = AfghanHound('Шелли', 0.607, 'охотничья', 0.303, 'серп')

print(dog1.__str__())
print(dog1.__repr__())
print(round(dog1.size_in_feet(), 2), 'ф.,', dog1.capitalize_name())

print()

print(dog2.__str__())
print(dog2.__repr__())
print(round(dog2.size_in_feet(), 2), 'ф.,', dog2.capitalize_name())
