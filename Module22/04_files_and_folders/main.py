import os

size = 0
dirs_count = 0
files_count = 0


def general_data(path):
    global size
    global dirs_count
    global files_count
    for file in os.listdir(path):
        local_path = os.path.join(path, file)
        if os.path.isdir(local_path):
            dirs_count += 1
            general_data(local_path)
        elif os.path.isfile(local_path):
            size += os.path.getsize(local_path)
            files_count += 1


general_path = os.path.abspath(os.path.join('..', '..', 'Module14'))
general_data(general_path)

print('Смотрим директорию:', os.path.abspath(os.path.join('..', '..', 'Module14')))
size = size/1024
print('Размер каталога (в Кб):', size)
print('Количество подкаталогов:', dirs_count)
print('Количество файлов:', files_count)
