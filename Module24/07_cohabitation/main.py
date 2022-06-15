import random


class Human:

    def __init__(self, name, home):
        self.name = name
        self.satiety = 50
        self.home = home
        self.alive_flag = True

    def to_go_to_work(self):
        print(f'Тамагочи {self.name} пошел на работу')
        self.satiety -= 10
        self.home.safe_for_money += 20
        self.is_alive()

    def eat(self):
        if self.home.refrigerator_with_food >= 10:
            print(f'Тамагочи {self.name} пошел кушать')
            self.satiety += 10
            self.home.refrigerator_with_food -= 10
        else:
            print(f'Еды дома нет. {self.name} останется голодным')
            self.satiety -= 10

    def play(self):
        print(f'Тамагочи {self.name} пошел играть')
        self.satiety -= 100
        self.is_alive()

    def go_shopping_for_food(self):
        if self.home.safe_for_money >= 10:
            print(f'Тамагочи {self.name} пошел в магазин за едой')
            self.home.safe_for_money -= 10
            self.home.refrigerator_with_food += 10
        else:
            print(f'Денег дома нет, чтоб купить еды. {self.name} придется идти на работу')
            self.to_go_to_work()

    def is_alive(self):
        if self.satiety <= 0:
            print(f'Тамагочи по имени {self.name} умер')
            self.alive_flag = False
            self.print_status()

    def tamagotchi_action_selection(self):
        if self.alive_flag:
            random_cube = random.randint(1, 6)
            if self.satiety < 20:
                self.eat()
            elif self.home.refrigerator_with_food < 10:
                self.go_shopping_for_food()
            elif self.home.safe_for_money < 50:
                self.to_go_to_work()
            elif random_cube == 1:
                self.to_go_to_work()
            elif random_cube == 2:
                self.eat()
            else:
                self.play()

    def print_status(self):
        print(f'Имя: {self.name} \nСытость: {self.satiety} '
              f'\nДеньги: {self.home.safe_for_money} '
              f'\nЕда: {self.home.refrigerator_with_food}\n')


class Home:

    def __init__(self):
        self.refrigerator_with_food = 50
        self.safe_for_money = 0


studio_apartment = Home()
player_1 = Human('Иван', studio_apartment)
player_2 = Human('Екатерина', studio_apartment)


for day in range(1, 366):
    print('\nДень', day)
    player_1.tamagotchi_action_selection()
    player_2.tamagotchi_action_selection()
    player_1.print_status()
    player_2.print_status()
