violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_time = 0
for i in range(int(input('Сколько песен выбрать? '))):
    print('Название', i + 1, 'песни: ', end='')
    total_time += violator_songs.get(input(), 0)

print('Общее время звучания песен:', round(total_time, 2), 'минут')

