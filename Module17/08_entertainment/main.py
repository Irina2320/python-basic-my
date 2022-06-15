import random

N = ['|' for _ in range(int(input('Количество палок: ')))]

for i in range(int(input('Количество бросков: '))):

    start = random.randint(1, len(N))
    stop = random.randint(start, len(N))
    print('Бросок', i + 1, 'Сбиты палки с номера', start, 'по номер', stop)

    for q in range(start - 1, stop):
        N[q] = '.'

print('Результат:', ''.join(N))
