
class Vehicle:
    __COLOR_VARIANTS = ['Blue', 'Gray', 'Red', 'Black']
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        if isinstance(owner, str):
            self.owner = owner
        if isinstance(model, str):
            self.__model = model
        if isinstance(color, str):
            self.__color = color
        if isinstance(engine_power, int):
            self.__engine_power = engine_power

    def get_model(self) -> str:
        return f'Модель: {self.__model}'

    def get_horsepower(self) -> str:
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self) -> str:
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if isinstance(new_color, str):
            for color in self.__COLOR_VARIANTS:
                if new_color.lower() == color.lower():
                    self.__color = new_color
                    break
            else:
                print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['Blue', 'Gray', 'Red', 'Black']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
print(vehicle1.get_model())