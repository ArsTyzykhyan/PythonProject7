def custom_write(file_name, strings):
    """
    Записывает в файл file_name все строки из списка strings, каждая на новой строке.
    Возвращает словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка.
    """
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as f:
        for i, string in enumerate(strings):
            strings_positions[(i + 1, f.tell())] = string
            f.write(string + '\n')
    return strings_positions

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)