nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def list_converter(some_list, new_list=[]):
    for element in some_list:
        if isinstance(element, list):
            for num in element:
                if isinstance(num, list):
                    list_converter(num)
                else:
                    new_list.append(num)
        else:
            new_list.append(element)
    return new_list

print('Ответ:', list_converter(nice_list))

