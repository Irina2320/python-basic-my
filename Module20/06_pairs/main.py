import random

original_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', original_list)

new_list1 = [tuple(original_list[i : i+2]) for i in range(10) if i%2 == 0]
print('Новый список:', new_list1)


new_list2 = []
for _ in range(5):
    new_list2.append(tuple([original_list.pop(0), original_list.pop(0)]))
print('Новый список:', new_list2)






# Напишите программу, которая инициализирует список из 10 случайных целых чисел, а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
#
# Дополнительно: решите задачу несколькими способами
#
# Пример:
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]