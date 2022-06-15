import random


class Human:

    def __init__(self, name, home, pet):
        self.name = name
        self.satiety = 30
        self.home = home
        self.alive_flag = True
        self.happy_point = 100
        self.pet = pet

    def pet_the_cat(self):
        print(f'{self.name} погладил кота {self.pet.name}')
        self.happy_point += 5

    def feed_the_cat(self):
        print(f'{self.name} покормил кота {self.pet.name}')
        self.pet.eat()

    def eat(self):
        if self.home.refrigerator_with_food >= 30:
            print(f'Тамагочи {self.name} пошел кушать')
            self.satiety += 30
            self.home.refrigerator_with_food -= 30
            self.home.all_food += 30
        elif self.home.refrigerator_with_food > 0:
            print(f'Еды дома мало. {self.name} съел всё')
            self.satiety += self.home.refrigerator_with_food
            self.home.all_food += self.home.refrigerator_with_food
            self.home.refrigerator_with_food = 0
        else:
            print(f'Еды дома нет. {self.name} остался голодным')

    def is_alive(self):
        if self.home.dirt > 90:
            print(f'Дома срач. {self.name} расстроен!')
            self.happy_point -= 10
        if self.satiety <= 0 or self.happy_point < 10:
            print(f'Тамагочи по имени {self.name} умер')
            self.alive_flag = False
            self.print_status()

    def print_status(self):
        print(f'\tИмя: {self.name} \n\tСытость: {self.satiety}, Счастье: {self.happy_point}'
              f'\n\tДеньги: {self.home.safe_for_money} \n\tЕда: {self.home.refrigerator_with_food} '
              f' Еда для кота: {self.home.refrigerator_with_food}\n')


class Husband(Human):

    def __init__(self, name, home, pet, child):
        super().__init__(name, home, pet)
        self.child = child

    def to_go_to_work(self):
        print(f'Тамагочи {self.name} пошел на работу')
        self.home.safe_for_money += 150
        self.home.all_money += 150


    def play(self):
        print(f'Тамагочи {self.name} пошел играть')
        self.happy_point += 20

    def tamagotchi_action_selection(self):
        if self.alive_flag:
            random_cube = random.randint(1, 6)
            if self.satiety < 20:
                self.eat()
            else:
                self.satiety -= 10
                if self.home.safe_for_money < 50:
                    self.to_go_to_work()
                elif cat.satiety < 20:
                    self.feed_the_cat()
                elif random_cube == 1:
                    self.to_go_to_work()
                elif random_cube == 2:
                    self.pet_the_cat()
                elif random_cube == 3:
                    self.feed_the_cat()
                else:
                    self.play()
        self.is_alive()


class Wife(Human):

    def __init__(self, name, home, pet, child):
        super().__init__(name, home, pet)
        self.child = child

    def go_shopping_for_food(self):
        if self.home.safe_for_money >= 60:
            print(f'Тамагочи {self.name} пошел в магазин за едой')
            self.home.safe_for_money -= 60
            self.home.refrigerator_with_food += 50
            self.home.food_for_cat += 10
        else:
            print(f'Денег дома нет, чтоб купить еды. {self.name} Пошел гладить кота')
            self.pet_the_cat()

    def buy_a_coat(self):
        if self.home.safe_for_money >= 350:
            print('Жена купила шубу!')
            self.home.safe_for_money -= 350
            self.happy_point += 60
            self.home.all_coats += 1
        else:
            print(f"Денег на шубу нет! {self.name} пошел гладить кота")
            self.pet_the_cat()

    def clean_the_house(self):
        if self.home.dirt > 100:
            self.home.dirt -= 100
        else:
            self.home.dirt = 0

    def tamagotchi_action_selection(self):
        if self.alive_flag:
            random_cube = random.randint(1, 6)
            if self.satiety < 30:
                self.eat()
            else:
                self.satiety -= 10
                if self.home.refrigerator_with_food < 30 or self.home.food_for_cat < 10:
                    self.go_shopping_for_food()
                elif self.home.dirt > 50:
                    self.clean_the_house()
                elif cat.satiety < 20:
                    self.feed_the_cat()
                elif random_cube == 1:
                    self.feed_the_cat()
                elif random_cube == 2:
                    self.buy_a_coat()
                else:
                    self.pet_the_cat()
        self.is_alive()


class Cat:
    def __init__(self, name, home):
        self.name = name
        self.satiety = 30
        self.home = home
        self.alive_flag = True

    def eat(self):
        if self.home.food_for_cat >= 10:
            print(f'Кота {self.name} покормили')
            self.satiety += 20
            self.home.food_for_cat -= 10
            self.home.all_food += 10
        elif self.home.food_for_cat > 0:
            print(f'Еды для кота {self.name} мало. Кот съел всю еду')
            self.satiety += self.home.food_for_cat * 2
            self.home.all_food += self.home.food_for_cat
            self.home.food_for_cat = 0
        else:
            print(f'Еды для кота {self.name} недостаточно! Кот начал драть обои')
            self.rip_wallpaper()

    def rip_wallpaper(self):
        print(f'Кот {self.name} дерет обои')
        self.home.dirt += 5
        self.satiety -= 10

    def is_alive(self):
        if self.satiety <= 0:
            print(f'\nТамагочи по имени {self.name} умер\n')
            self.alive_flag = False

    def sleep(self):
        print(f'Кот {self.name} спит')
        self.satiety -= 5

    def print_status(self):
        print(f'\tКошак: {self.name} Сытость:{self.satiety}')

    def tamagotchi_action_selection(self):
        if self.alive_flag:
            random_cube = random.randint(1, 10)
            if random_cube == 1:
                self.rip_wallpaper()
            else:
                self.sleep()
        self.is_alive()


class Child(Human):

    def __init__(self, name, home, pet):
        super().__init__(name, home, pet)

    def go_to_school(self):
        print(f'Ребенок {self.name} пошел в школу')
        self.home.safe_for_money -= 5
        self.happy_point -= 5

    def playing_on_fathers_game_console(self):
        print(f'Ребенок {self.name} играет на папкиной приставке')
        self.happy_point += 50

    def clean_the_house(self):
        print(f'Ребенок {self.name} помогает маме с уборкой')
        self.happy_point -= 5
        if self.home.dirt > 50:
            self.home.dirt -= 50
        else:
            self.home.dirt = 0

    def tamagotchi_action_selection(self):
        if self.alive_flag:
            random_cube = random.randint(1, 6)
            if self.satiety < 10:
                self.eat()
            else:
                self.satiety -= 5
                if self.home.dirt > 80:
                    self.clean_the_house()
                elif cat.satiety < 10:
                    self.feed_the_cat()
                elif random_cube in (1, 3, 6):
                    self.go_to_school()
                elif random_cube == 2:
                    self.pet_the_cat()
                else:
                    self.playing_on_fathers_game_console()
        self.is_alive()


class Home:

    def __init__(self):
        self.refrigerator_with_food = 50
        self.safe_for_money = 100
        self.food_for_cat = 30
        self.dirt = 0
        self.all_coats = 0
        self.all_money = 0
        self.all_food = 0

    def print_data(self):
        print(f'Статистика Дома:\n'
              f'Еды в холодильнике: {self.refrigerator_with_food} Еды для кота: {self.food_for_cat}\n'
              f'Денег в тумбочке: {self.safe_for_money} Грязи дома: {self.dirt} \n'
              f'Шуб в шкафу: {self.all_coats} Денег было заработано за год: {self.all_money} '
              f'Еды съедено за год: {self.all_food}')


trying = 0

while True:
    trying += 1

    studio_apartment = Home()
    cat = Cat('Эдгар', studio_apartment)
    child = Child(name='Люцифер', home=studio_apartment, pet=cat)
    father = Husband(name='Иван', home=studio_apartment, pet=cat, child=child)
    mother = Wife(name='Екатерина', home=studio_apartment, pet=cat, child=child)
    players = (father, mother, child, cat)

    for day in range(1, 366):
        print('\n', '*' * 20, f'\nДень: {day}')
        for player in players:
            player.tamagotchi_action_selection()

        for player in players:
            player.print_status()

        studio_apartment.dirt += 5
        if not all([player.alive_flag for player in players]):
            break
    else:
        studio_apartment.print_data()
        print('- ' * 20, '\nПолучилось с попытки:', trying)
        break
