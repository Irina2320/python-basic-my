import os

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
text = open(os.path.abspath('text.txt'), 'r')
cipher_text = open(os.path.abspath('cipher_text.txt'), 'a')
shift = 0
upper_flag = False
for string in text:
    shift += 1
    for symbol in string:
        if symbol.isalpha():
            upper_flag = symbol.isupper()
            if upper_flag:
                cipher_text.write(alphabet[(alphabet.index(symbol.lower()) + shift) % 25].upper())
            else:
                cipher_text.write(alphabet[(alphabet.index(symbol) + shift) % 25])
        else:
            cipher_text.write(symbol)

text.close()
cipher_text.close()
