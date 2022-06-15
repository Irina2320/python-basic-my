def summ_numbers(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ


def count_numbers(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count



n = int(input('\nВведите число: '))
print('Сумма цифр:', summ_numbers(n))
print ('Кол-во цифр в числе: ', count_numbers(n))
print('Разность суммы и кол-ва цифр:', summ_numbers(n) - count_numbers(n))
