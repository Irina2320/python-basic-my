import random


class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20

    def hit_another(self, enemy):
        print(f'{self.name} наносит удар {enemy.name} \n'
              f'{enemy.name} теряет {self.damage} единиц здоровья')
        enemy.health -= self.damage
        print(f'Остаток здоровья {enemy.name}: {enemy.health}ХР\n')

    def is_alive(self):
        if self.health > 0:
            print(f'Победил: {self.name}, \nОстаток здоровья: {self.health}')


warrior_1 = Warrior("Воин 1")
warrior_2 = Warrior("Воин 2")

while warrior_1.health > 0 and warrior_2.health > 0:
    if random.randint(1, 2) == 1:
        warrior_1.hit_another(warrior_2)
    else:
        warrior_2.hit_another(warrior_1)

for warrior in warrior_1, warrior_2:
    warrior.is_alive()
