from pprint import pprint

name = 'sample.txt'
file = open(name, 'r') # Открытые файла в режиме read
pprint(file.read()) # Вывод содержимого файла в консоль
file.close() # Закрытие файла
file = open(name, 'w') # Открытие файла в режиме write
file.write('Hello') # Замена содержимого открытого файла на 'Hello'
file = open(name, 'a') # Открытие файла в режиме append
file.write('\nIm is programmer') # Добавление содержимого в конец файл, без удаления
file = open(name, 'r') # Открытие файла в режиме append
print(file.tell()) # Расположение курсор до чтения файла = 0
pprint(file.read()) # Вывод содержимого файла в консоль
print(file.tell()) # Расположение курсор после чтения файла = 0
pprint(file.read()) # Вывод содержимого файла в консоль = ПУСТОТА
file.seek(0) # Принудительный сдвиг курсора в самое начало
pprint(file.read()) # Вывод содержимого файла в консоль = Содержимое выводится
