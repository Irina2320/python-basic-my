zen = open('zen.txt', 'r')
zen_reverse = []
for line in zen:
    if line[-1] == '\n':
        line = line[:-1]
    zen_reverse.append(line)
zen.close()


for _ in range(len(zen_reverse)):
    print(zen_reverse.pop())

