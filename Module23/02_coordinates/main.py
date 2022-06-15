import random


def function1(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def function2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


def finding_coordinates():
    try:
        with open('coordinates.txt', 'r') as file:
            for line in file:
                nums = line.split()
                result1 = str(function1(int(nums[0]), int(nums[1])))
                result2 = str(function2(int(nums[0]), int(nums[1])))
                number = str(random.randint(0, 100))
                with open('result.txt', 'a') as file_2:
                    results = sorted([result1, result2, number])
                    file_2.write(' '.join(results) + '\n')
    except ZeroDivisionError:
        print('Ошибка работы генератора! В результате рандомизации получилось деление на "0"')


finding_coordinates()
