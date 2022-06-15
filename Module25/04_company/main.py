import random

names = [
    'Железный Человек', 'Капитан Америка', 'Соколиный Глаз',
    'Человек Муравей', 'Черная Вдова', 'Невероятный Халк',
    'Красная Ведьма', 'Черная Пантера', 'Зимний Солдат'
        ]
workers = []


class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.post = 'Employee'
        self.salary = 0

    def calculation_of_wages(self):
        pass


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 13000
        self.post = 'Manager'

    def calculation_of_wages(self):
        self.salary = 13000

    def print_data(self):
        print(f'\nЛичная карта работника\nДолжность: {self.post}, \n'
              f'Фамилия: {self.get_surname()}, Имя: {self.get_name()}, Возраст: {self.get_age()} \n'
              f'Зарплата: {self.salary}')


class Agent(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 0
        self.volume_of_sales = 0
        self.post = 'Agent'

    def set_volume_of_sales(self, volume_of_sales):
        self.volume_of_sales = volume_of_sales

    def calculation_of_wages(self):
        self.salary = 5000 + self.volume_of_sales / 100 * 5

    def print_data(self):
        print(f'\nЛичная карта работника\nДолжность: {self.post}, \n'
              f'Фамилия: {self.get_surname()}, Имя: {self.get_name()}, Возраст: {self.get_age()} \n'
              f'Объем продаж: {self.volume_of_sales}, Зарплата: {self.salary}')


class Worker(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 0
        self.hours_worked = 0
        self.post = 'Worker'

    def set_hours_worked(self, hours_worked):
        self.hours_worked = hours_worked

    def calculation_of_wages(self):
        self.salary = self.hours_worked * 100

    def print_data(self):
        print(f'\nЛичная карта работника\nДолжность: {self.post}, \n'
              f'Фамилия: {self.get_surname()}, Имя: {self.get_name()}, Возраст: {self.get_age()} \n'
              f'Количество часов: {self.hours_worked}, Зарплата: {self.salary}')


for post in (Manager, Agent, Worker):
    for _ in range(3):
        surname, name = names.pop(0).split()
        workers.append(post(name=name, surname=surname, age=random.randint(18, 65)))

for employer in workers:
    if employer.post == 'Agent':
        employer.set_volume_of_sales(random.randint(10000, 100000))
        employer.calculation_of_wages()

    elif employer.post == 'Worker':
        employer.set_hours_worked(random.randint(20, 100))
        employer.calculation_of_wages()

    employer.print_data()
