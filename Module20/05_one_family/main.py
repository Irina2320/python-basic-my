data = {
    ('Иванов', 'Иван'): 22,
    ('Иванов', 'Степан'): 33,
    ('Иванов', 'Руслан'): 12,
    ('Иванова', 'Наталья'): 45,
    ('Петров', 'Иван'): 25,
    ('Петров', 'Дмитрий'): 55,
    ('Петрова', 'Катя'): 7
}

find_word = input('Введите фамилию: ').capitalize()
if find_word[-1] == 'а':
    find_word = find_word[:-1]
for name, age in data.items():
    if find_word == name[0][:len(find_word)]:
        print(name[0], name[1], age)
