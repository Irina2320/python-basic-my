def slicer(input_tuple, num):
    if input_tuple.count(num) == 1:
        return input_tuple[input_tuple.index(num):]
    elif input_tuple.count(num) > 1:
        return input_tuple[input_tuple.index(num):
                           input_tuple.index(num) + input_tuple[input_tuple.index(num) + 1:].index(num) + 2]
    else:
        return ()


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), int(input('Введите число '))))
