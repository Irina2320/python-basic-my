def num_line(num):
    if num == 1:
        print(num)
        return 2
    else:
        print(num_line(num - 1))
        return num + 1


num = int(input('Введите num: '))
num_line(num)
