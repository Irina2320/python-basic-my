import random

cards = [card for card in range(1, 11) for color in range(4)]   # 1 - Туз
cards.extend([10 for _ in range(12)])


class CompPlayer:

    def __init__(self, name):
        self.name = name
        self.total_cards = 0
        self.collect_flag = True

    def collect_card(self):
        if self.total_cards < 20:
            select_card = cards.pop(random.randint(0, len(cards) - 1))
            if select_card == 1:
                select_card = 11
            self.total_cards += select_card
            print(f'\nИгрок {self.name} взял карту {select_card} \nТекущая сумма очков: {self.total_cards}')
        else:
            print(f'\nИгрок {self.name} воздержался от взятия карты')
            self.collect_flag = False


class HumanPlayer:

    def __init__(self):
        self.name = input('Введите имя игрока: ')
        self.total_cards = 0
        self.collect_flag = True

    def collect_card(self):
        print(f'\nХодит игрок: {self.name} Текущая сумма карт: {self.total_cards} \nХотите взять карту? \n1 - Да 2 - Нет')
        answer = input('Ожидание ввода: ')
        if answer == '1':
            select_card = cards.pop(random.randint(0, len(cards) - 1))
            if select_card == 1 and self.total_cards <= 21:
                select_card = 11
            self.total_cards += select_card
            print(f'Игрок {self.name} взял карту {select_card} \nТекущая сумма очков: {self.total_cards}')
        else:
            self.collect_flag = False


def winner(player1, player2):
    if player1.total_cards > 21:
        if player2.total_cards > 21:
            print('Ничья')
        else:
            print("Победил игрок", player2.name)
    elif player2.total_cards > 21:
        print('Победил игрок', player1.name)
    elif player1.total_cards == 21:
        if player2.total_cards == 21:
            print('Ничья')
        else:
            print('Победил игрок', player1.name)
    elif player2.total_cards == 21:
        print("Победил игрок", player2.name)
    elif player1.total_cards > player2.total_cards:
        print('Победил игрок', player1.name)
    elif player2.total_cards > player1.total_cards:
        print('Победил игрок', player2.name)
    else:
        print('Ничья')
    print('Игра окончена')


def dialog():
    print('\nКакой режим игры реализовать? '
          '\n\t1 - Компьютер - Компьютер \n\t2 - Компьютер - Человек \n\t3 - Человек - Человек')
    answer = input('Ожидание ввода: ')
    if answer == '1':
        comp1 = CompPlayer('Compukter 1')
        comp2 = CompPlayer('Compukter 2')
        while comp1.collect_flag or comp2.collect_flag:
            comp1.collect_card()
            comp2.collect_card()
        winner(comp1, comp2)

    elif answer == '2':
        comp = CompPlayer('Compukter')
        user = HumanPlayer()
        while comp.collect_flag or user.collect_flag:
            comp.collect_card()
            user.collect_card()
        winner(comp, user)

    elif answer == '3':
        user1 = HumanPlayer()
        user2 = HumanPlayer()
        while user1.collect_flag or user2.collect_flag:
            user1.collect_card()
            user2.collect_card()
        winner(user1, user2)


while True:
    try:
        dialog()
    except ValueError:
        print('\nЗакончились карты ==)')
