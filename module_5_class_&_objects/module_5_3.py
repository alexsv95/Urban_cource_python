# Задача "Магические здания"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to_floor(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(
                f'{new_floor}-го этажа в доме "{self.name}" не существует, самый высокий этаж {self.number_of_floors}')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    '''Задача "Магические здания"'''
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    '''Задача "Нужно больше этажей"'''
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        return House(self.name, self.number_of_floors + other)

    def __radd__(self, other):
        return House(self.name, self.number_of_floors + other)

    def __iadd__(self, other):
        return House(self.name, self.number_of_floors + other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)
#
h2 = 10 + h2 # __radd__
print(h2)
#
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__