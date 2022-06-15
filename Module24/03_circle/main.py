import math

circles = []


class Circle:

    def __init__(self, name, radius=1, point_x=0, point_y=0):
        self.name = name
        self.point_x = point_x
        self.point_y = point_y
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def rise(self, coefficient):
        self.radius *= coefficient
        print('Обновленные данные: ')
        self.print_data()

    def print_data(self):
        perimetr = round(self.perimeter(), 3)
        square = round(self.square(), 3)
        print(f"\nНазвание круга: '{self.name}'"
              f'\nКоординаты (X, Y): ({self.point_x}, {self.point_y})'
              f'\nРадиус: {self.radius}'
              f'\nДлинна окружности: {perimetr}'
              f'\nПлощадь: {square}')


def intersection(circle_1, circle_2):
    total_x = abs(circle_1.point_x - circle_2.point_x)
    total_y = abs(circle_1.point_y - circle_2.point_y)
    distance = math.sqrt(total_x ** 2 + total_y ** 2)
    if distance >= circle_1.radius + circle_2.radius:
        print('Круги пересекаются')
    else:
        print('Круги не пересекаются')


def ask_user():
    message = ('\nЧто хотите сделать? \n1 - нарисовать новый круг '
               '\n2 - посмотреть текущие круги \nВведите свой ответ: ')
    answer = input(message)
    if answer == '1':
        name = input('Введите ИМЯ круга (для более удобной ориентации): ')
        try:
            radius = float(input('\nВведите радиус круга. \n'
                                 '\nДля задания значения параметров по умолчанию нажмите Enter'
                                 '\nОжидание ввода: '))
        except ValueError:
            radius = 1
        try:
            point_x = float(input('Введите координату X: '))
        except ValueError:
            point_x = 0
        try:
            point_y = float(input('Введите координату Y: '))
        except ValueError:
            point_y = 0
        circles.append(Circle(name, radius, point_x, point_y))
        circles[-1].print_data()
    elif answer == '2':
        circle_count = 0
        print("Ваши круги: ")
        for circle in circles:
            circle_count += 1
            print(f'{circle_count} - й круг: {circle.name}')
        else:
            try:
                circle_index = int(input("С каким кругом хотите работать? Введите его порядковый номер: ")) - 1
                circle = circles[circle_index]
                print(f"Вы выбрали круг: {circle.name}")
                print('Что вы хотите сделать? \n1 - увеличить радиус '
                      '\n2 - посмотреть пересечения с другой окружностью')
                answer = input('Ожидание ввода: ')
                if answer == '1':
                    rise_coefficient = int(input('Во сколько раз увеличить окружность? \nОжидание ввода: '))
                    circle.rise(rise_coefficient)
                elif answer == '2':
                    print(
                        f'Выберите номер окружности, с которой хотите посмотреть пересечения окружности {circle.name}')
                    circle_count = 0
                    for circle in circles:
                        circle_count += 1
                        print(f'{circle_count} - й круг: {circle.name}')
                    circle_2_index = int(input('Ожидание ввода: ')) - 1
                    circle_2 = circles[circle_2_index]
                    intersection(circle, circle_2)
                else:
                    raise ValueError
            except (ValueError, IndexError):
                print('Некорректный ввод!')
    else:
        print('Некорректный ввод!\n')


while True:
    ask_user()
