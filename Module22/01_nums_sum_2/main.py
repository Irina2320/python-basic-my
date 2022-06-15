general_sum = 0
text_file = open('numbers.txt', 'r')
for symbol in text_file.read():
    if symbol.isdigit():
        general_sum += int(symbol)

text_file.close()
answer = open('answer.txt', 'w')
answer.write(str(general_sum))
answer.close()
