alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
    'э', 'ю', 'я'
            ]

message = list(input('Введите сообщение: '))
shift = int(input('Введите сдвиг: '))

for word in range(len(message)):
    for i in range(len(alphabet)):
        if message[word] == alphabet[i]:
            i = (i + shift) % len(alphabet)
            message[word] = alphabet[i]
            break



print('Зашифрованное сообщение: ', ''.join(message))
