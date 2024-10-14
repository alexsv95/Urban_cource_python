from typing import Union

class Product:
    def __init__(self, name: str, weight: Union[int, float], category: str):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Указан некорректный тип данных')
        if isinstance(weight, (int, float)):
            self.weight = weight
        else:
            raise TypeError('Указан некорректный тип данных')
        if isinstance(category, str):
            self.category = category
        else:
            raise TypeError('Указан некорректный тип данных')

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()

    def add(self, *product):
        for p in product:
            if p.name in self.get_products():
                print(f'Продукт {p.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                p_to_str = str(p)
                file.write(f'{p_to_str}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())