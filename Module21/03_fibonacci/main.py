def fibonachi(deep):
    if deep == 1:
        return 1, 1
    else:
        num1, num2 = fibonachi(deep-1)
        num1, num2 = num2, num1 + num2
        return num1, num2

deep = int(input('Введите позицию числа в ряде Фибоначчи: '))

print(fibonachi(deep)[0])



# Пример 1:
# Введите позицию числа в ряде Фибоначчи: 6
# Введите позицию числа в ряде Фибоначчи: 10
# Число: 55
# ```

