file = list(input('Введите строку: '))
new_file = []
tik = 1


for i in range(len(file) - 1):
    if file[i] == file[i + 1]:
        tik += 1
    else:
        new_file.append(file[i])
        new_file.append(str(tik))
        tik = 1
else:
    new_file.append(file[i + 1])
    new_file.append(str(tik))

print('Закодированная строка: ', ''.join(new_file))
