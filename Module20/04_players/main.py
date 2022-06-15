players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# Не пидумал как развернуть кортеж в кортеже((
players_list = [(name + scores) for name, scores in players.items()]
print(players_list)



players_list = []

for name, score in players.items():
    lokal_list = []
    for name_lokal in name:
        lokal_list.append(name_lokal)
    for score_lokal in score:
        lokal_list.append(score_lokal)
    players_list.append(tuple(lokal_list))

print(players_list)
