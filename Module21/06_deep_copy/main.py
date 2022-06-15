def site_generator(some_struct, product_name, tab):
    tik = len(some_struct)
    for i_key, i_value in some_struct.items():
        tik -= 1
        if i_key == 'title' or i_key == 'h2':
            print('\t' * tab, "'" + i_key + "'", ':', "'" + i_value.format(product_name) + "'", end='')
        elif isinstance(i_value, dict):
            print('\t' * tab, "'" + i_key + "' : {")
            site_generator(i_value, product_name, tab + 1)
        else:
            print('\t' * tab, "'" + i_key + "'", ':', "'" + i_value + "'", end='')
        if tik == 0:
            print()
        else:
            print(',')

    print('\t' * (tab - 1), '}', end='')


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {0} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {0}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}



for _ in range(int(input('Сколько сайтов: '))):
    product_name = input('Введите название продукта для нового сайта: ')
    print('Сайт для', product_name + ':\n')
    tab = 1
    print('site = {')
    site_generator(site, product_name, tab=1)
    print('\n')

