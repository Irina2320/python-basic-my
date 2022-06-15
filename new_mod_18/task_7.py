def ip_check():
    if len(ip_address) != 4:
        print('Адрес - это четыре числа, разделенные точками')
        return False

    for i in ip_address:
        if not i.isdigit():
            print(i, '- не целое число')
            return False
        elif 0 > int(i) or int(i) > 255:
            print(i, 'превышает 255')
            return False
    return True


while True:
    ip_address = input('Введите IP: ').split('.')
    if ip_check():
        print('IP-адрес корректен')
        break

