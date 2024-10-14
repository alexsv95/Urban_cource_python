
def custom_write(file_name, strings):
    string_position = {}
    num_line = 0
    for i in strings:
        file = open(file_name, 'a', encoding='UTF-8')
        num_line += 1
        num_byte = file.tell()
        string_position[(num_line, num_byte)] = i
        file.write(f'{i}\n')
        file.close()
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

