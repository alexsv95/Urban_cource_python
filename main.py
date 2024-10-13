
class Human:
    def __init__(self, name, group):
        print('Сработал инит Human')
        self.name = name
        super().__init__(group)
        super().about()

    def print_info(self):
        print(f'Меня зовут {self.name}, я из {self.place}')

class StudentGroup:
    def __init__(self, group):
        print('Сработал инит StudentGroup')
        self.group = group

    def about(self):
        print(f'Я учусь в группе {self.group}')

class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        print('Сработал дочерний инит')
        super().__init__(name, group)
        self.name = name
        self.place = place
        super().print_info()
        # super().__init__(group)


student1 = Student('Alex', 'Казань', '125')

