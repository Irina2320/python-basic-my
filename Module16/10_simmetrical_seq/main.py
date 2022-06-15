num_count = int(input('Кол-во чисел: '))
numbers = []
tik = 0
list_2 = []

for i in range(num_count):
    numbers.append(int(input('Число: ')))
print('Последовательность: ', numbers)


def pallindrom(numbers):
    index = 1
    for i in range(len(numbers)):
        if index + i > len(numbers):
            return True
        if numbers[i] == numbers[-index]:
            index += 1
        else:
            return False


while True:
    if pallindrom(numbers):
        print('Нужно приписать чисел:', tik)
        print('Сами числа:', list_2)
        break
    else:
        list_2.insert(0, numbers[0])
        numbers.pop(0)
        tik += 1
