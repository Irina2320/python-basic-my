def find_key(key, deep, diction):
    if key in diction:
        return diction[key]
    elif deep == 1:
        return None
    else:
        for i_value in diction.values():
            if isinstance(i_value, dict):
                local_key = find_key(key, deep - 1, i_value)
                if local_key:
                    return local_key

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите искомый ключ: ')
if input('Хотите ввести максимальную глубину? Y/N: ').lower() == 'y':
    deep = int(input('Введите максимальную глубину: '))
else:
    deep = -1

print('Значение ключа:', find_key(key, deep, site))
