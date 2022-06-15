import os


def get_path() -> None:
    """
    Функция для получения от пользователя имени искомого элемента и пути к директории,
    с которой должен начаться поиск.
    Для начала поиска с корня диска, на котором запущена программа достаточно нажать "Enter".
    При некорректно введенном пути поиск начинается с корня диска
    Полученный путь и искомый элемент передаём в функцию gen_files_path
    """

    search_element = input('Введите искомый элемент (с указанием расширения, например ".txt"): ')
    path = input('Введите путь (через пробел) до директории с поиском\n'
                 'Для поиска из корня диска нажмите Enter\n'
                 'Ожидание ввода: ')
    path = os.path.sep.join(path.split())
    if os.path.exists(path):
        print('Указанный путь корректный!')
    elif os.path.exists(os.path.sep + path):
        path = os.path.sep + path
        print("Путь немного допилили")
    else:
        print(os.getcwd().split(os.path.sep))
        path = os.getcwd().split(os.path.sep)[0] + os.path.sep

    print(f"Начинаем поиск с: '{path}'\n")
    gen_files_path(path, search_element)


def gen_files_path(path, search_element) -> None:
    """
    Функция для перебора элементов из указанного пути и поиска нужного элемента

    dirs_amount: счетчик просмотренных папок
    files_amount: счетчик просмотренных файлов

    :param path: Путь, с которого начинаем искать.
    :param search_element: Имя искомого элемента

    """
    message_flag = None
    dirs_amount = 0
    files_amount = 0

    for dir_path, dir_names, file_names in os.walk(path):
        for dir_name in sorted(dir_names):
            print("Каталог:", os.path.join(dir_path, dir_name))
            dirs_amount += 1
            if dir_name == search_element:
                message_flag = os.path.join(dir_path, dir_name)
                break
        if not message_flag:
            for file_name in file_names:
                print("Файл:", os.path.join(dir_path, file_name))
                files_amount += 1
                if file_name == search_element:
                    message_flag = os.path.join(dir_path, file_name)
                    break

        if message_flag:
            print(f'\nЯ задолбался!\n'
                  f'Я перебрал {dirs_amount} папок и пересмотрел {files_amount} файлов\n'
                  f"\nИскомый элемент находится по адресу: \n{message_flag}")
            break
    else:
        print(f"Файл '{search_element}' по адресу '{path}' найти не удалось\n"
              f'Но я старался!\n'
              f'Я перебрал {dirs_amount} папок и пересмотрел {files_amount} файлов')


get_path()
