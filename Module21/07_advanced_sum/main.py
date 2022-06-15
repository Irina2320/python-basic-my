def sum(*args):
    summ = 0
    for element in args:
        if isinstance(element, list):
            for num in element:
                if isinstance(num, list):
                    summ += sum(num)
                else:
                    summ += num
        else:
            summ += element
    return summ


print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))


