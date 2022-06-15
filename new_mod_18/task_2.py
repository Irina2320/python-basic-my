my_string = input('Введите строку: ').split()
max_word = 0

for i in range(len(my_string)):
    if len(my_string[i]) > max_word:
        max_word = len(my_string[i])

for i in my_string:
    if len(i) == max_word:
        print('Самое длинное слово:', i)
        print('Длина этого слова:', max_word,)
        break

