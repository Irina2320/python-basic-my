guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    status = input('Гость пришёл или ушёл? ')
    if status == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) >= 6:
            print('Прости,', name, ', но мест нет.')
        else:
            guests.append(name)
            print("Привет,", name)
    elif status == 'ушёл':
        name = input('Имя гостя: ')
        print('Пока,', name)
        guests.remove(name)
    elif status == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:
        print('Некорректный ввод!')