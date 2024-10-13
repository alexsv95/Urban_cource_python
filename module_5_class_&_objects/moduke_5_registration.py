from itertools import count


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс регистрации пользователя с атрибутами: Логин и пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            password_valid = User.password_validation(self, password, password_confirm)
            if password_valid:
                self.password = password
            else:
                print('Пароль должен соответствовать следующим требованиям: минимум 8 символов, содержать 1 цифру и 1 букву в верхнем регистре')
        else:
            print("Пароль не совпадает")

    def password_validation(self, password, password_confirm):
        int_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        password_valid = False
        if password_confirm == password:
            if len(password) >= 8:
                for num in password:
                    if num in int_list:
                        password_valid = True
                        break
                    else:
                        password_valid = False
                for word in password:
                    if word == word.upper() and word not in int_list:
                        password_valid = True
                        break
                    else:
                        password_valid = False
        return password_valid

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print("Пользователь не найден")
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password != password2 or User.password_validation(user, password, password2) == False:
                continue
            database.add_user(user.username, user.password)
        print(database.data)