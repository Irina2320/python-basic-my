message = list(input('Сообщение: '))
lokal_word = []
result_message = []

for i in message:
    if i.isalpha():
        lokal_word.insert(0, i)
    else:

        result_message.extend(lokal_word)
        result_message.append(i)
        lokal_word.clear()

print('Новое сообщение:', ''.join(result_message))

