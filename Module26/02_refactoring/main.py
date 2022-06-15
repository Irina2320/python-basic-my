list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def generator():
    for number_1 in list_1:
        for number_2 in list_2:
            print(f'{number_1} * {number_2} =', end=' ')
            yield number_1 * number_2


for result in generator():
    print(result)
    if result == to_find:
        print('Found!!!')
        break


