my_string = input('Введите строку: ')
start = 0
stop = 0

for i in range(len(my_string)):
    if my_string[i] == 'h':
        start = i
        break

for i in range(len(my_string)):
    if my_string[i] == 'h':
        if i > stop:
            stop = i

print('Развёрнутая последовательность между первым и последним h:', my_string[stop - 1:start:-1])
