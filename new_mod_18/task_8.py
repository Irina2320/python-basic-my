first_string = list(input('Первая строка: '))
second_string = list(input('Вторая строка: '))
tik = 0

for i in range(len(first_string)):
    if first_string == second_string:
        print('Первая строка получается из второй со сдвигом', tik)
        break
    else:
        first_string.insert(0, first_string.pop())
        tik +=1
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

