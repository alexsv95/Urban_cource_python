

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')


Alex = Human('Алексей', 'Соснов', 29)

print(Alex.say_info())


class Human_new:

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


users = {'name': 'Alex', 'age': 29}

user1 = Human_new(**users)
print(user1.name)