import random


class MyFirstException(Exception):
    pass


total_sum = 0

while total_sum < 777:
    try:
        number = int(input('Введите число: '))
        total_sum += number
        with open('out_file.txt', 'a') as out_file:
            out_file.write(str(number) + '\n')
        if random.randint(1, 13) == 13:
            raise MyFirstException()
    except MyFirstException:
        print('Вас постигла неудача!')
        break
    except ValueError:
        print('Необходимо ввести число!')
else:
    print('Вы набрали необходимое количество очков!')