my_dikt = {}
for i in list(input('Введите текст: ')):
    if i in my_dikt:
        my_dikt[i] += 1
    else:
        my_dikt[i] = 1
print('Оригинальный словарь частот:')
for i in sorted(my_dikt.keys()):
    print(i, ':', my_dikt[i])

inverted_dikt = {}
for i in my_dikt:
    if my_dikt[i] in inverted_dikt:
        inverted_dikt[my_dikt[i]].append(i)
    else:
        inverted_dikt[my_dikt[i]] = [i]

print('Инвертированный словарь частот:')
for i in sorted(inverted_dikt.keys()):
    print(i, ':', inverted_dikt[i])
