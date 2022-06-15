string_count = 0
symbols_sum = 0

with open('people.txt', 'r') as people:
    for name in people:
        string_count += 1
        if name.endswith('\n'):
            name = name[:-1]
        try:
            if len(name) > 2:
                symbols_sum += len(name)
            else:
                raise ValueError()
        except ValueError:
            print(f'Ошибка! В имени меньше 3 символов в строке {string_count}')
            with open('errors.log', 'a') as errors:
                errors.write(f'Менее трёх символов в строке {string_count}\n')

print('Общее количество символов:', symbols_sum)
