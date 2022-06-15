text = open('text.txt', 'r')
symbols = dict()
symbol_count = dict()
all_symbol = text.read().lower()
text.close()

for symbol in all_symbol:
    if symbol.isalpha():
        if symbol in symbols:
            symbols[symbol] += 1
        else:
            symbols[symbol] = 1

words_count = sum(symbols.values())

for word, frequency in symbols.items():
    frequency = round(frequency / words_count, 3)
    if frequency not in symbol_count:
        symbol_count[frequency] = {word}
    else:
        symbol_count[frequency].update(word)

analysis = open('analysis.txt', 'a')

for frequency, words_set in sorted(symbol_count.items(), reverse=True):
    for word in sorted(words_set):
        analysis.write(word + ' ' + str(frequency) + '\n')

analysis.close()
