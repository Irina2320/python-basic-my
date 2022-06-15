import random

max_num = int(input('Введите максимальное число: '))
my_num = str(random.randint(1, max_num))


while True:
    ask = input('\nНужное число есть среди вот этих чисел: ')
    if ask == 'Помогите!':
        lokal_set = {my_num}
        while len(lokal_set) != 3:
            lokal_set.add(str(random.randint(1, max_num)))
        print('Артём мог загадать следующие числа:', ' '.join(lokal_set))
    else:
        ask = set(ask.split())
        if my_num in ask:
            print('Да')
            if len(ask) == 1:
                print("Ты угадал! ")
                break
        else:
            print('Нет')

