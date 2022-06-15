total_sum = 0


def calculator(data):
    number1, operand, number2 = tuple(data.split())
    number1, number2 = int(number1), int(number2)
    if operand == '+':
        return number1 + number2
    elif operand == '-':
        return number1 + number2
    elif operand == '*':
        return number1 * number2
    elif operand == '/':
        return number1 / number2
    elif operand == '//':
        return number1 // number2
    elif operand == '%':
        return number1 % number2
    else:
        raise ValueError()


with open('calc.txt', 'r') as calculator_file:
    for string in calculator_file:
        while True:
            try:
                total_sum += calculator(string)
            except (ValueError, ZeroDivisionError):
                message = 'Обнаружена ошибка в строке: ' + string + 'Хотите исправить? '
                if input(message).lower() in ('yes', 'y', "да", "д", 'естественно!', 'ну конечно!'):
                    string = input('Введите исправленную строку: ')
                else:
                    break
            else:
                break

print('Сумма результатов:', total_sum)

