import random

children = []
names = ('Паша', 'Катя', 'Коля', 'Света')


class Parent:

    def __init__(self, name, adult):
        self.name = name
        self.adult = adult
        self.children = children

    def calm_down_the_child(self, some_child):
        some_child.trouble = False

    def feed_the_child(self, some_child):
        some_child.hunger = False

    def tell_about_yourself(self):
        print(f'\nИмя: {self.name} \nВозраст: {self.adult} \nДети: ', end='')
        if children:
            for child in children:
                print(child.name, end=' ')
            else:
                print()
        else:
            print('Детей пока нет')


class Child:

    def __init__(self, name, adult):
        self.name = name
        self.adult = adult
        self.trouble = random.choice([True, False])
        self.hunger = random.choice([True, False])

    def tell_about_yourself(self):
        print(f'\nИмя: {self.name} \nВозраст: {self.adult} ')
        if self.trouble:
            print('Диагноз: Тревожное расстройство')
        else:
            print("Диагноз: Ребенок вызывает тревожное расстройство у других)")
        if self.hunger:
            print("Ребенок голодает")
        else:
            print("Ребенок сыт по горло")


mother = Parent('Елена', random.randint(20, 100))
mother.tell_about_yourself()
father = Parent('Джон', random.randint(20, 100))
father.tell_about_yourself()
print('\nВзяли ипотеку... \nПожили для себя... \nПора заводить детей))\n')
for name in names:
    children.append(Child(name, random.randint(0, min(mother.adult, father.adult) - 16)))
    children[-1].tell_about_yourself()
else:
    mother.tell_about_yourself()
    father.tell_about_yourself()

print("\nЕсть некоторые проблемы с детьми... Мама кормит, папа успокаивает")
for child in children:
    mother.feed_the_child(child)
    father.calm_down_the_child(child)

print('Проверяем работу родителей: \n')
for child in children:
    child.tell_about_yourself()
