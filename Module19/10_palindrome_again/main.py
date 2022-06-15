my_string = input('Введите строку: ')
my_dict = {}

for i in my_string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

flag = 0
for i in my_dict.values():
      if i%2 != 0:
          flag +=1

if flag > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')

# По идее палиндром имеет право только на одну нечетную букву, остальные должны быть зеркльными. На это и проверял инпут