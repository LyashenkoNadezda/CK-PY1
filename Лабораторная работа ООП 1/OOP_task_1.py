import doctest


class SolidWall:
    def __init__(self, hight: int, material: str):
        """
        Создание и подготовка к работе объекта "Прочная стена"

        :param hight: высота стены
        :param material: материал, из которого сделана стена

        Пример:
        >>> wall = SolidWall(10, 'stone')  # инициализация экземпляра класса
        """
        if not isinstance(hight, int):
            raise TypeError('Height must be int!')

        if hight <= 0:
            raise ValueError('Height cannot be 0!')
        self.hight = hight

        if not isinstance(material, str):
            raise TypeError('Material must be a string!')

        if material not in ['wood', 'stone', 'brick', 'cement', 'cardboard', 'clay']:
            raise ValueError('The material is wrong!')
        self.material = material

    def destroy(self, destroy_tool: str) -> None:
        """
        Разрушение стены.

        :param destroy_tool: инструмент для разрушения стены

        :raise ValueError: вызываем ошибку, если инструмент для разрушения стены для этого не подходит

        Пример:
        >>> wall = SolidWall(10, 'stone')
        >>> wall.destroy('hammer')
        """
        if not isinstance(destroy_tool, str):
            raise TypeError('A tool for destroying must be a string!')

    def build(self, build_tool: str, material: str) -> None:
        """
        Создание стены.

        :param build_tool: инструмент для создания стены
        :param material: материал для создания стены

        :raise ValueError: вызываем ошибку, если инструмент для создания стены для этого не подходит
        :raise ValueError: вызываем ошибку, если материал для создания стены для этого не подходит

        Пример:
        >>> wall = SolidWall(10, 'stone')
        >>> wall.build('hammer', 'stone')
        """
        if not isinstance(build_tool, str):
            raise TypeError('A tool for building must be a string!')

        if not isinstance(material, str):
            raise TypeError('A material for building must be a string!')

    def paint(self, paint_tool: str, dye: str) -> None:
        """
        Покраска стены.

        :param paint_tool: инструмент для покраски стены
        :param dye: краска для покраски стены

        :raise ValueError: вызываем ошибку, если инструмент для покраски стены для этого не подходит

        Пример:
        >>> wall = SolidWall(10, 'stone')
        >>> wall.paint('brush', 'white_dye')
        """
        if not isinstance(paint_tool, str):
            raise TypeError('A tool for painting must be a string!')
        if not isinstance(dye, str):
            raise TypeError('A dye must be a string!')


class Stone:
    def __init__(self, weight: int, hight: int, width: int):
        """
        Создание и подготовка к работе объекта "Камень"

        :param weight: вес камня
        :param hight: высота камня
        :param width: ширина камня

        Пример:
        >>> stone = Stone(2, 1, 3)  # инициализация экземпляра класса
        """
        if not isinstance(weight, int):
            raise TypeError('Weight must be int!')

        if weight <= 0:
            raise ValueError('Weight cannot be 0!')
        self.weight = weight

        if not isinstance(hight, int):
            raise TypeError('Height must be int!')

        if hight <= 0:
            raise ValueError('Height cannot be 0!')
        self.hight = hight

        if not isinstance(width, int):
            raise TypeError('Width must be int!')

        if width <= 0:
            raise ValueError('Width cannot be 0!')
        self.width = width

    def throw(self) -> None:
        """
        Бросок камня.

        :raise ValueError: вызываем ошибку, если камень слишком тяжел для броска

        Пример:
        >>> stone = Stone(2, 1, 3)
        >>> stone.throw()
        """
        ...

    def break_stone(self, break_tool: str) -> None:
        """
        Разбиение камня.

        :param break_tool: инструмент для разбиения камня

        :raise ValueError: вызываем ошибку, если инструмент для разбиения камня для этого не подходит

        Пример:
        >>> stone = Stone(2, 1, 3)
        >>> stone.break_stone('hammer')
        """
        if not isinstance(break_tool, str):
            raise TypeError('A tool for breaking a stone must be a string!')


class ACommonCup:
    def __init__(self, weight: int, material: str, volume: int):
        """
        Создание и подготовка к работе объекта "Камень"

        :param weight: вес чашки
        :param material: материал, из которого изготовлена чашка
        :param volume: объем чашки

        Пример:
        >>> cup = ACommonCup(2, 'wood', 3)  # инициализация экземпляра класса
        """
        if not isinstance(weight, int):
            raise TypeError('Weight must be int!')

        if weight <= 0:
            raise ValueError('Weight cannot be 0!')
        self.weight = weight

        if not isinstance(material, str):
            raise TypeError('Material must be a string!')

        if material not in ['wood', 'stone', 'porcelain', 'glass', 'cardboard', 'clay', 'metall']:
            raise ValueError('The material is wrong!')
        self.material = material

        if not isinstance(volume, int):
            raise TypeError('Cup volume must be int!')

        if volume <= 0:
            raise ValueError('Cup volume cannot be 0!')
        self.volume = volume

    def drink_tea(self) -> None:
        """
        Питье из чашки чая.

        :raise ValueError: вызываем ошибку, если чай слишком горячий

        Пример:
        >>> cup = ACommonCup(2, 'wood', 3)
        >>> cup.drink_tea()
        """
        ...

    def break_cup(self, break_tool: str) -> None:
        """
        Разбиение чашки.

        :param break_tool: инструмент для разбиения чашки

        :raise ValueError: вызываем ошибку, если инструмент для разбиения чашки для этого не подходит

        Пример:
        >>> cup = ACommonCup(2, 'wood', 3)
        >>> cup.break_cup('spoon')
        """
        if not isinstance(break_tool, str):
            raise TypeError('A tool for breaking a cup must be a string!')

    def wash(self, wash_tool: str, detergent: str) -> None:
        """
        Мытье чашки.

        :param wash_tool: инструмент для мытья чашки
        :param detergent: моющее средство

        :raise ValueError: вызываем ошибку, если инструмент для мытья чашки для этого не подходит

        Пример:
        >>> cup = ACommonCup(2, 'wood', 3)
        >>> cup.wash('washcloth', 'Fairy')
        """
        if not isinstance(wash_tool, str):
            raise TypeError('A tool for washing a cup must be a string!')
        if not isinstance(detergent, str):
            raise TypeError('A detergent must be a string!')

# TODO Написать 3 класса с документацией и аннотацией типов


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
