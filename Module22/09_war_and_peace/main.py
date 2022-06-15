import zipfile

archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
archive.extract('voyna-i-mir.txt')
archive.close()
words = dict()
counters = dict()
text = open('voyna-i-mir.txt', 'r', encoding='utf-8')

for string in text:
    for word in string:
        if word.isalpha():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1

text.close()

for word, count in words.items():
    if count not in counters:
        counters[count] = {word}
    else:
        counters[count].update(word)

war_and_peace = open('war_and_peace.txt', 'a')

for count, word in sorted(counters.items()):
    for local_word in sorted(word):
        print(local_word, ' : ', count)
        war_and_peace.write(local_word + ' : ' + str(count) + '\n')
