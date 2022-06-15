countries = dict()

for i in range(int(input('Кол-во стран: '))):
    print(i+1, '- я страна: ',  end='')
    lokal_country = input().split()
    countries[lokal_country[0]] = lokal_country[1:]

for i in range(3):
    print(i+1, 'город: ', end='')
    lokal_city = input()
    for country in countries:
        if lokal_city in countries[country]:
            print('Город', lokal_city, 'расположен в стране', country)
            break
    else:
        print('По городу', lokal_city, 'данных нет.')
