def my_zip(interp1, interp2):
    min_len = min(len(interp1), len(interp2))
    return ((interp1[i], interp2[i]) for i in range(min_len))



my_list = [1, 2, 3]
my_string = 'abcd'
my_dict = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4}

for i in my_zip(my_list, my_string):
    print(i)

# Как посмотреть, циклом я пользовался только в генераторе... Возможно я не так понял задание