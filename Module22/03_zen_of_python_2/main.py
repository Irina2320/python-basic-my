import os

letters = dict()
word_count = 1
word_flag = False
letter_count = 0
string_count = 0
rare_letter = ''


zen = open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r')
for string in zen:
    string_count += 1
    for symbol in string.lower():
        if symbol.isalpha():
            letter_count += 1
            word_flag = True
            if symbol in letters:
                letters[symbol] += 1
            else:
                letters[symbol] = 1

        elif word_flag == True and (symbol == ' ' or symbol == '\n'):
            word_count += 1
            word_flag = False

min_count_letter = min(letters.values())
print(letters)
for letter, count in letters.items():
    if count == min_count_letter:
        rare_letter = str(letter)
        break

zen.close()

print('Количество букв в файле:', letter_count)
print('Количество слов в файле:', word_count)
print('Количество строк в файле:', string_count)
print('Наиболее редкая буква:', rare_letter)
