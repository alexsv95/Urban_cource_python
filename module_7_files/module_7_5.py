import os
import time

directory = os.walk('.')
for root, dirs, files in directory:
    for f in files:
        file_path = os.path.join(root, f)
        file_size = os.stat(f).st_size
        file_time = os.stat(f).st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        print(f'Обнаружен файл: {f}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {formatted_time}')


