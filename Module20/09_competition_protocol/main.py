def winner():
    max_result = max(local_protocol.values())
    for play, data in local_protocol.items():
        if max_result[1] == data[1]:
            if data[0] in winners:
                continue
            else:
                winners.extend(data)
            break
    local_protocol.pop(play)
    return winners[-2], winners[-1]

winners = []
protocol = {}

for i in range(1, int(input('Сколько записей вносится в протокол? ')) + 1):
    print(i, 'запись: ', end='')
    input_data = input().split()
    protocol[i] = input_data[1], int(input_data[0])
local_protocol = protocol.copy()


print('Итоги соревнований:')
for i in range(3):
    winner()
    print(i + 1, 'место:', winners[-2], winners[-1])
