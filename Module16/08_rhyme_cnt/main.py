people = int(input('Кол-во человек: '))
people_count = list(range(1, people + 1))
num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', num, 'человек')
index_del = 0


while len(people_count) > 1:
    print('\nТекущий круг людей:', people_count)
    index_start = index_del % len(people_count)
    print('Начало счёта с номера', people_count[index_start])
    index_del = (index_start + num - 1) % len(people_count)
    print('Выбывает человек под номером', people_count[index_del])
    people_count.remove(people_count[index_del])

print('\nОстался человек под номером', people_count[0])
