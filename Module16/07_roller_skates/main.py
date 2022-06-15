num_skates = int(input('Кол-во коньков: '))
skates = []
people_size = []
people_with_skates = 0

for i in range(num_skates):
    print('Размер', i + 1, 'пары: ', end= '')
    skates.append(int(input()))
skates.sort()

num_people_size = int(input('\nКол-во людей: '))

for i in range(num_people_size):
    print('Размер ноги', i + 1, 'человека: ', end= '')
    people_size.append(int(input()))
people_size.sort()

for i in people_size:
    for q in skates:
        if i <= q:
            people_with_skates += 1
            skates.remove(q)
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики:', people_with_skates)

