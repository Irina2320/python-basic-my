letters = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
text = input('Введите текст: ')

def is_vowels(letter):
    for i in letters:
        if i == letter:
            return True


vowels = [i for i in text if is_vowels(i)]
print('Список гласных букв:', vowels, '\nДлина списка:', len(vowels))


#  Нужно отнести кольцо в Мордор!