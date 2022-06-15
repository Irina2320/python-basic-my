# Вода + Воздух = Шторм
# Вода + Огонь = Пар
# Вода + Земля = Грязь
# Воздух + Огонь = Молния
# Воздух + Земля = Пыль
# Огонь + Земля = Лава

class Water:

    def __init__(self):
        self.name = 'Water'

    def __add__(self, other):
        if other.name == 'Air':
            return Storm()
        elif other.name == 'Fire':
            return Steam()
        elif other.name == 'Ground':
            return Dirt()
        else:
            return None


class Air:

    def __init__(self):
        self.name = 'Air'

    def __add__(self, other):
        if other.name == 'Water':
            return Storm()
        elif other.name == 'Fire':
            return Lightning()
        elif other.name == 'Ground':
            return Dust()
        else:
            return None


class Fire:

    def __init__(self):
        self.name = 'Fire'

    def __add__(self, other):
        if other.name == 'Water':
            return Steam()
        elif other.name == 'Air':
            return Lightning()
        elif other.name == 'Ground':
            return Lava()
        else:
            return None


class Ground:

    def __init__(self):
        self.name = 'Ground'

    def __add__(self, other):
        if other.name == 'Water':
            return Dirt()
        elif other.name == 'Air':
            return Dust()
        else:
            return None


class Storm:
    def __init__(self):
        self.name = 'Storm'
        print('Азъ есмъ Шторм! Дитя Воды и Воздуха')


class Steam:
    def __init__(self):
        self.name = 'Steam'
        print('Азъ есмъ Пар! Дитя Воды и Огня')


class Dirt:
    def __init__(self):
        self.name = 'Dirt'
        print('Азъ есмъ Грязь! Дитя Воды и Земли')


class Dust:
    def __init__(self):
        self.name = 'Dust'
        print('Азъ есмъ Пыль! Дитя Воздуха и Земли')


class Lightning:
    def __init__(self):
        self.name = 'Lightning'
        print('Азъ есмъ Молния! Дитя Воздуха и Огня')


class Lava:
    def __init__(self):
        self.name = 'Lava'
        print('Азъ есмъ Лава! Дитя Земли и Огня')


water, air, ground, fire = Water(), Air(), Ground(), Fire()
elements = (water, air, ground, fire)

for first_element in elements:
    for second_element in elements:
        if not first_element + second_element:
            print(f'Союз {first_element.name} и {second_element.name} потерпел неудачу')

