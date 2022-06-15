friends = int(input('Кол-во друзей: '))
vouchers = int(input('Долговых расписок: '))
duty = []

for i in range(friends):
    duty.append(0)

for i in range(vouchers):
    print('\n', i + 1, 'расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    duty[to_whom - 1] -= how_much
    duty[from_whom - 1] += how_much

print('\nБаланс друзей:')
for i in range(friends):
    print(i+1, ':', duty[i])
