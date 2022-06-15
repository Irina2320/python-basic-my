year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))

print('Года от', year1, 'до', year2, 'с тремя одинаковыми цифрами:')
for i in range(year1, year2 + 1):
    year = i
    n1 = i % 10
    i //= 10
    n2 = i % 10
    i //= 10
    n3 = i % 10
    i //= 10
    n4 = i % 10
    i //= 10
    if n1 == n2:
        if n1 == n3:
            print(year)
            continue
        elif n1 == n4:
            print(year)
            continue
    elif n2 == n3:
        if n3 == n4:
            print(year)
            continue