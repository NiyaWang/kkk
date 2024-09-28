class Figure:
    def __init__(self, color, *sides):
        self._sides = []
        self._color = list(color)
        self.filled = False

        if self._is_valid_sides(*sides):
            self._sides = list(sides)
        else:
            self._sides = [1] * self.sides_count  # default sides

    @property
    def sides_count(self):
        return 0

    def get_color(self):
        return self._color

    def _is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)  # Периметр для фигур с замкнутыми гранями

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    @property
    def sides_count(self):
        return 1

    def __len__(self):
        return self._sides[0]  # Длина окружности

    def get_square(self):
        radius = self._sides[0] / (2 * math.pi)
        return math.pi * (radius ** 2)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides = [new_sides[0]]  # Установим единственную сторону



class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    @property
    def sides_count(self):
        return 3

    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1 and isinstance(sides[0], (int, float)) and sides[0] > 0:
            self._sides = [sides[0]] * self.sides_count  # 12 одинаковых сторон
        else:
            self._sides = [1] * self.sides_count  # По умолчанию

    @property
    def sides_count(self):
        return 12

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], (int, float)) and new_sides[0] > 0:
            self._sides = [new_sides[0]] * self.sides_count  # 12 одинаковых сторон
        # Если передано больше или меньше одного значения, не изменяем

    def get_volume(self):
        return self._sides[0] ** 3




circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)
print(circle1.get_sides())  # [15]

# Проверка периметра (круга):
print(len(circle1))  # 10

# Проверка объёма (куба):
print(cube1.get_volume())  # 216