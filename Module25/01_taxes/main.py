class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculator(self):
        try:
            budget = float(input("Введите свой бюджет: "))
            apartment_worth = Apartment(float(input('Введите стоимость квартиры: ')))
            car_worth = Car(float(input('Введите стоимость машины: ')))
            country_house_worth = CountryHouse(float(input('Введите стоимость дачи: ')))
            general_tax = apartment_worth.calculator() + car_worth.calculator() + country_house_worth.calculator()
            print("Общий налог:", general_tax)
            balance = budget - general_tax
            if balance > 0:
                print(f'\nДенег на уплату налогов хватает! \nОстаток: {balance}$')
            else:
                print(f'\nДенег на уплату налогов недостаточно! \nНе хватает: {abs(balance)}$')

        except ValueError:
            print('Некорректный ввод!')


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculator(self):
        print(f'\nНалог на квартиру: {self.worth / 1000}$')
        return round(self.worth / 1000, 2)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculator(self):
        print(f'Налог на машину: {self.worth / 200}$')
        return round(self.worth / 200, 2)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculator(self):
        print(f'Налог на дачу: {self.worth / 500}$')
        return round(self.worth / 500, 2)


property = Property(0)
property.calculator()
