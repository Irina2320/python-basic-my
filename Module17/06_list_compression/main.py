import random

my_list = [random.randint(0, 2) for _ in range(int(input('Количество чисел в списке: ')))]
print('Список до сжатия:', my_list)

tik = 0
for i in range(len(my_list)):
    if my_list[i] == 0:
        my_list.append(my_list.pop(i))
        tik += 1

print('Список в процессе сжатия:', my_list)

for _ in range(tik):
    my_list.pop()

print('Список после сжатия:', my_list)
