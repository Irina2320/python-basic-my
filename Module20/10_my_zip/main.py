def my_zip():
    result = list()
    for i in range(min(len(my_string), len(my_tuple))):
        result.append(tuple([my_string[i], my_tuple[i]]))
    return result

my_string = list(input('Строка: '))
my_tuple = tuple(input('Кортеж чисел (ввод без скобок, числа идут через ", "): ').split(', '))


print(type(my_zip()))
for i in my_zip():
    print(i)
