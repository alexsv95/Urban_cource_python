# Задача "Developer - не только разработчик"

class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to_floor(self, new_floor: int):
        if new_floor > self.number_of_floor:
            print(f'{new_floor}-го этажа в доме "{self.name}" не существует, самый высокий этаж {self.number_of_floor}')
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to_floor(5)
h2.go_to_floor(10)