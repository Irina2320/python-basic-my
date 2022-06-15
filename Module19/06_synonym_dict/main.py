synonyms_dict = {}

for i in range(int(input('Введите количество пар слов: '))):
    print(i+1, 'пара: ', end='')
    synonyms = input().split(' - ')
    synonyms_dict[synonyms[0]] = synonyms[1]

flag = False

while True:
    word = input('\nВведите слово: ').capitalize()
    for i in synonyms_dict.items():
        if word in i:
            i = list(i)
            i.remove(word)
            print('Синоним:', i[0])
            flag = True
            break
    else:
        print('Такого слова в словаре нет.')
    if flag:
        break

# Не придумал, как кроме флага, выходить из цикла в цикле. Если есть способ лучше - напишите плиз)
