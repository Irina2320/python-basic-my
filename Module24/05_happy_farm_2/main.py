import random


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        return self.state == 3

    def print_state(self):
        print('Садовник полил картошку {} сейчас она {}'.format(self.index, self.states[self.state]))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow(self, index):
        self.potatoes[index].grow()


class Gardener:

    def __init__(self, name):
        self.potato_garden = PotatoGarden(5)
        self.name = name

    def grow_garden(self):
        print('Садовник пьющий, и поливает картошки случайным образом \nПосмотрим, кто доживёт))\n')
        for _ in range(3):
            for index in range(5):
                if random.choice([True, False]):
                    self.potato_garden.grow(index)

    def collect_harvest(self):
        ripe_flag = False
        print('\nПришла пора собирать урожай:')
        for potato in self.potato_garden.potatoes:
            if potato.is_ripe():
                print(f"Картошка {potato.index} готова к сбору урожая")
                ripe_flag = True
        if not ripe_flag:
            print('Картошка не уродилась. Пора менять садовника')


garden_worker = Gardener('Степан')
garden_worker.grow_garden()
garden_worker.collect_harvest()

