list1 = []
list2 = []

for i in range(3):
    print('Введите', i + 1, 'число для первого списка: ', end= '')
    list1.append(int(input()))

for i in range(7):
    print('Введите', i + 1, 'число для второго списка: ', end= '')
    list2.append(int(input()))

print('Первый список:', list1)
print('Второй список:', list2)

for i in list1:
    for q in range(list2.count(i)):
        list2.remove(i)

list1.extend(list2)

print('Новый первый список с уникальными элементами:', list1)

# Ну или объединить списки, сделать множеством, потом опять списком)