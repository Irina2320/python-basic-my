"""
Реализуйте класс автомобиля, а также класс, который будет описывать автобус. У автобуса, кроме того, что имеется у автомобиля,
должны быть поля, содержащие число пассажиров и количество полученных денег, изначально равное нулю. Также должны быть методы «войти» и «выйти»,
изменяющие число пассажиров. Наконец, метод move должен быть переопределён, чтобы увеличивать количество денег в соответствии
с количеством пассажиров и пройденным расстоянием.
"""
import math


class Car:
    def __init__(self):
        self.angle = 0
        self.point_x = None
        self.point_y = None
        self.set_coordinates()
        self.total_distance = 0

    def move(self):
        try:
            message = (f'\nВведите угол машины в градусах (0 - 360) относительно текущего направления градация углов '
                       f'идет против часовой стрелки\nТекущий угол относительно оси "Х": {self.angle} \n'
                       f'(0 или 360 - прямо, 90 - повернуть налево 180 - назад, 270 - направо) \nОжидание ввода: ')
            new_angle = float(input(message))
            if new_angle < 0 or new_angle > 360:
                raise ValueError
            distance = float(input('Введите расстояние, на которое проехала машина: '))
            if distance < 0:
                print('Движение назад невозможно! Для этого действия развернитесь на 180 градусов '
                      'и введите положительное расстояние')
                raise ValueError
            self.find_coordinates(new_angle, distance)
            print(f'\nОбновленные данные: \nКоордината "Х": {self.point_x} Координата "Y": {self.point_y} '
                  f'\nОбщее расстояние: {self.total_distance}, угол относительно "Х": {self.angle}')

        except ValueError:
            print('Некорректный ввод! Попробуйте ввести данные снова. \nДанные - числа!\n')
            self.move()

    def set_coordinates(self):
        try:
            point_x = float(input('Введите координату "Х": '))
            point_y = float(input('Введите координату "Y": '))
            self.point_x = point_x
            self.point_y = point_y

        except ValueError:
            print('Некорректный ввод! Попробуйте ввести координаты снова. Координаты - числа')
            self.set_coordinates()

    def find_coordinates(self, new_angle, distance):
        self.total_distance += distance
        new_angle = (self.angle + new_angle) % 360
        self.angle = new_angle
        angle_options = 0
        while new_angle > 90:
            new_angle -= 90
            angle_options += 1
        new_angle = math.radians(new_angle)
        cos_diff = round(math.cos(new_angle) * distance, 2)
        sin_diff = round(math.sin(new_angle) * distance, 2)

        if angle_options == 0:
            self.point_x += cos_diff
            self.point_y += sin_diff
        elif angle_options == 1:
            self.point_x -= sin_diff
            self.point_y += cos_diff
        elif angle_options == 2:
            self.point_x -= cos_diff
            self.point_y -= sin_diff
        elif angle_options == 3:
            self.point_x += sin_diff
            self.point_y -= cos_diff


class Bus(Car):
    def __init__(self):
        print('\nАвтобус - такси. Одна единица расстояния стоит один рубль. Деньги списываются с каждого человека. '
              'Больше пассажиров - больше денег')
        super(Bus, self).__init__()
        self.money = 0
        self.passengers = 0

    def enter(self):
        try:
            new_passengers = int(input('Введите, сколько человек вошло: '))
            self.passengers += new_passengers
        except ValueError:
            print('Некорректный ввод!')

    def exit(self):
        try:
            new_passengers = int(input('Введите, сколько человек вышло: '))
            if new_passengers < self.passengers:
                self.passengers -= new_passengers
            else:
                print('Ошибка: пассажиров выходит больше, чем едет на данный момент!')
        except ValueError:
            print('Некорректный ввод!')

    def move(self):
        try:
            message = (f'\nВведите угол автобуса в градусах (0 - 360) относительно текущего направления. '
                       f'Градация углов идет против часовой стрелки\nТекущий угол относительно оси "Х": {self.angle}\n'
                       f'(0 или 360 - прямо, 90 - повернуть налево 180 - назад, 270 - направо) \nОжидание ввода: ')
            new_angle = float(input(message))
            if new_angle < 0 or new_angle > 360:
                raise ValueError
            distance = float(input('Введите расстояние, на которое проехала машина: '))
            if distance < 0:
                print('Движение назад невозможно! Для этого действия развернитесь на 180 градусов '
                      'и введите положительное расстояние')
                raise ValueError

            self.find_coordinates(new_angle, distance)
            self.money += self.passengers * distance

            print(f'\nОбновленные данные: \nКоордината "Х": {self.point_x} Координата "Y": {self.point_y} '
                  f'\nОбщее расстояние: {self.total_distance}, угол относительно "Х": {self.angle}\n'
                  f'Текущее число пассажиров: {self.passengers} Количество заработанных денег: {self.money}')

        except ValueError:
            print('Некорректный ввод! Попробуйте ввести данные снова. \nДанные - числа!\n')
            self.move()


car = Car()
car.move()
car.move()
car.move()

bus = Bus()
bus.enter()
bus.move()
bus.enter()
bus.move()
bus.exit()
bus.move()





