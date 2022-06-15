'''Весь геморрой, описанный ниже на случай не только двузначных очков
и победителей с одинаковым кол-вом баллов)'''

first_tour = open('first_tour.txt', 'r')
second_tour = open('second_tour.txt', 'a')
second_tour_data = dict()
min_level = None

for string in first_tour:
    if string[:-1].isdigit():
        min_level = int(string[:-1])
        continue
    string = string.split()
    if int(string[-1]) > min_level:
        if string[-1] not in second_tour_data:
            second_tour_data[string[-1]] = [string[1][0] + '. ' + string[0]]
        else:
            second_tour_data[string[-1]].append(string[1][0] + '. ' + string[0])

second_tour.write(str(len(second_tour_data.values())) + '\n')
for key in sorted(second_tour_data.keys(), reverse=True):
    while len(second_tour_data[key]) > 0:
        second_tour.write(second_tour_data[key].pop() + ' ')
        second_tour.write(str(key) + '\n')

first_tour.close()
second_tour.close()
