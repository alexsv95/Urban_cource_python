from math import pi, sqrt

from numpy.matlib import empty


class Figure():
    sides_count = 0
    def __init__(self, color: list, *sides: int):
        if self.__is_valid_color(*color):
            self.__color = color
        self.filled = True
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        elif self.__is_valid_sides(*sides):
            self.__sides = [*sides]

    def get_color(self) -> list:
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) <= self.sides_count:
            for i in sides:
                if i <= 0 or not isinstance(i, int):
                    return False
                else:
                    return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    def __len__(self):
        return sum(self.__sides)




class Circle(Figure):
    sides_count = 1
    def __init__(self, color: list, *sides: int):
        super().__init__(color, *sides)
        self.__radius = self.__calculation_radius()

    def get_square(self):
        square = pi * self.__radius ** 2
        return square

    def __calculation_radius(self):
        radius = len(self) / (pi * 2)
        return radius



class Triangle (Figure):
    sides_count = 3

    def get_square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [*sides] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3




circle1 = Circle([200, 200, 100], 10)
print(circle1.get_sides())

triangle1 = Triangle([200, 200, 100], 6)
print(triangle1.get_sides())
print(triangle1.get_square())

cube1 = Cube([200, 200, 100], 6)
print(cube1._Cube__sides)
print(cube1._Figure__sides)
print(cube1.get_sides())
print(cube1.get_volume())
