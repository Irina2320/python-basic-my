data = dict()

for i in range(int(input('Введите кол-во заказов: '))):
    print(i+1, 'заказ: ', end='')
    order = input().split()
    if order[0] in data:
        if order[1] in data[order[0]]:
            data[order[0]][order[1]] += int(order[2])
        else:
            data[order[0]][order[1]] = int(order[2])
    else:
        data[order[0]] = {order[1]: int(order[2])}

for i in sorted(data.keys()):
     print(str(i) + ':')
     for q in sorted(data[i].keys()):
        print('\t', str(q) + ':', data[i][q])
