def reverse(n):
    n_lokal1 = ''
    n_lokal2 = ''
    flag = False
    for i in str(n):
        if i == '.':
            n_lokal1 += '.'
            flag = True
            continue
        if flag == False:
            n_lokal1 = i + n_lokal1
        else:
            n_lokal2 = i + n_lokal2
    return float(n_lokal1 + n_lokal2)




while True:
    n1 = float(input('\nВведите первое число: '))
    n2 = float(input('Введите второе число: '))
    print('\nПервое число наоборот:', reverse(n1))
    print('Второе число наоборот:', reverse(n2))
    print('Сумма:', reverse(n1) + reverse(n2))
