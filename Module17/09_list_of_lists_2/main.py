nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print('Ответ:', [num3 for num1 in nice_list
                     for num2 in num1
                     for num3 in num2])
