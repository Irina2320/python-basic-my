import os


def file_reader(text, path, name):
    os.chdir(path)
    file = open(name, 'w')
    file.write(text)
    file.close()
    file = open(name, 'r')
    print('''Файл успешно сохранён!\n
    Содержимое файла:\n''', file.read())
    file.close()


input_text = input('Введите строку: ')
general_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
general_path = os.path.sep + os.path.sep.join(general_path)
print(general_path)
if not os.path.exists(general_path):
    print('Такого пути не существует!')
else:
    file_name = input('Введите имя файла: ') + '.txt'
    if file_name in os.listdir(general_path):
        question = input('Вы действительно хотите перезаписать файл? ').lower()
        if question in ('yes', 'y', 'да'):
            file_reader(input_text, general_path, file_name)
        else:
            print('Файл не будет перезаписан')
    else:
        file_reader(input_text, general_path, file_name)
