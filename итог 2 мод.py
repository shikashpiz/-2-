class Tree:
    """Базовый класс для всех деревьев."""
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height  # Высота в метрах
        self.age = age  # Возраст в годах

    def __str__(self) -> str:
        return f"{self.name}: высота {self.height} м, возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height}, age={self.age})"

    def grow(self, years: int) -> None:
        """Метод для роста дерева. Увеличивает возраст и высоту."""
        self.age += years
        self.height += years * 0.5  # Примерная скорость роста


class ConiferousTree(Tree):
    """Класс хвойных деревьев, наследуется от Tree."""
    def __init__(self, name: str, height: float, age: int, needle_type: str):
        super().__init__(name, height, age)
        self.needle_type = needle_type  # Тип хвои (например, мягкая, жесткая)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height}, age={self.age}, needle_type={self.needle_type!r})"

    def shed_needles(self) -> str:
        """Метод, описывающий сбрасывание хвои."""
        return f"{self.name} сбрасывает старую хвою."


class DeciduousTree(Tree):
    """Класс лиственных деревьев, наследуется от Tree."""
    def __init__(self, name: str, height: float, age: int, leaf_shape: str):
        super().__init__(name, height, age)
        self.leaf_shape = leaf_shape  # Форма листьев (например, овальная, заостренная)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height}, age={self.age}, leaf_shape={self.leaf_shape!r})"

    def shed_leaves(self) -> str:
        """Метод, описывающий сбрасывание листьев осенью."""
        return f"{self.name} сбрасывает листья осенью."


if __name__ == "__main__":
    pass

if __name__ == "__main__":
    # Write your solution here
    pass
