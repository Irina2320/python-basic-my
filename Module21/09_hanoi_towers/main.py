step = 0

def hanoi(level, start=1, stop=3):
    global step
    if level == 1:
        step += 1
        print(f'Шаг {step}: Переложить диск {level} со стержня номер {start} на стержень номер {stop} штырь')
    else:
        tmp = 6 - start - stop
        hanoi(level-1, start, tmp)
        step += 1
        print(f'Шаг {step}: Переложить диск {level} со стержня номер {start} на стержень номер {stop} штырь')
        hanoi(level-1, tmp, stop)


hanoi(int(input('Введите количество дисков: ')))


# Видел решение в 3 строчки из чата скиллбокса, но до конца его не понял