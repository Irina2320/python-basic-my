# Вывод степени числа списка

numbers = [3,7,5]
while True:
    number = int(input('Новое число: '))
    numbers.append(number)
    print('Текущий список чисел: ', numbers)
    for i in numbers:
        print((i*2, i*3, i*4))
    flag = int(input('Продолжить работать? (1/0) '))
    if flag == 0:
        break
print('Работа завершена')
