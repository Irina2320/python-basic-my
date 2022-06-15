import os


def get_path() -> None:
    """
    Функция для получения от пользователя пути к директории, с которой должен начаться поиск.
    Можно как ввести прописью через пробел весь путь, так и указать на сколько директорий нужно подняться вверх
    относительно директории, из которой запущена программа.
    При некорректно введенном пути поиск начинается на 2 директории выше относительно этой программы
    Полученный путь передаём в функцию collect_all_strings
    """

    path = input('Введите путь (через пробел) до директории с поиском\n'
                 'Или введите числом, на сколько директорий нужно подняться вверх из директории с текущим проектом\n'
                 'Ожидание ввода: ')
    if path.isdigit():
        dirs_count = int(path)
        path = os.path.abspath(os.path.join('..'))

        for _ in range(dirs_count):
            print(os.path.split(path))
            path = os.path.split(path)[0]

    else:
        path = os.path.sep.join(path.split())
        if os.path.exists(path):
            print('Указанный путь корректный!')
        elif os.path.exists(os.path.sep + path):
            path = os.path.sep + path
            print("Путь немного допилили")
        else:

            print("Какая-то проблема... Поднимусь на 2 папки вверх")
            path = os.path.abspath(os.path.join('..', '..'))

    print(f"Начинаем поиск с: '{path}'\n")
    collect_all_strings(path)


def collect_all_strings(path) -> None:
    """
    Функция длч перелопачивания всех файлов с расширением ".ру" и подсчетам количества строк кода,
    игнорируя пустые строки (в который ничего нет, кроме пробелов и '/n')
    и строчки комментариев (строки в которых есть символ "#" или которые заключены в тройные кавычки)
    strings_amount (int): Общее число строк кода
    comments_amount (int): Общее число строк комментариев

    :param path: Путь, c которого начинается поиск.
    """

    strings_amount = 0
    comments_amount = 0

    for dir_path, dir_names, file_names in os.walk(path):

        for file_name in file_names:
            if file_name[-3:] == '.py':
                with open(os.path.join(dir_path, file_name), 'r', encoding='utf-8') as py_file:
                    comment_flag = False
                    strings_in_file = 0
                    comment_in_file = 0
                    for string in py_file:
                        if '#' not in string and len(string[:-1].expandtabs().strip()) > 0:
                            if '"""' in string and not comment_flag:
                                comment_in_file += 1
                                comment_flag = True

                            elif '"""' in string and comment_flag:
                                comment_in_file += 1
                                comment_flag = False

                            if not comment_flag:
                                strings_in_file += 1
                            else:
                                comment_in_file += 1
                    else:
                        print(f'Файл по адресу: {os.path.join(dir_path, file_name)} \n'
                              f'Количество строк в файле: {strings_in_file}\n'
                              f'Количество строк комментариев в файле: {comment_in_file}\n')
                        strings_amount += strings_in_file
                        comments_amount += comment_in_file
    print(f'\nОбщее число строк кода: {strings_amount}\n'
          f'Общее число строк комментариев: {comments_amount}')


get_path()
