violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

timer = 0
song_count = int(input('Сколько песен выбрать? '))
for i in range(song_count):
    print('Название', i + 1, 'песни: ', end = '')
    user_song = input()
    for song in violator_songs:
        if song[0] == user_song:
            timer += song[1]

print('Общее время звучания песен: ', round(timer, 2), 'минут')

# Понимаю, что правильнее было с точки зрения проги все песни кидать в отдельный список, но в задание это не входило))

