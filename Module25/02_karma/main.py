import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Live:
    def __init__(self):
        self.__karma_points = 0
        self.__day = 0
        self.__trying = 0

    def one_day(self):
        try:
            self.__day += 1
            self.__karma_points += random.randint(1, 7)
            if random.randint(0, 9) == 0:
                raise (random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]))

        except KillError:
            self.write_error(error='Суициднулся')

        except DrunkError:
            self.write_error(error='НедоПереПил')

        except CarCrashError:
            self.write_error(error='Разбился на машинке')

        except GluttonyError:
            self.write_error(error='Пережор')

        except DepressionError:
            self.write_error(error='Глубокий депресняк')

    def write_error(self, error):

        karma_log.write(f'\n\nПопытка: {self.__trying}\nДух буддиста окончил свое существование на {self.__day} день \n'
                        f'\tОчки кармы: {self.__karma_points}\tПричина: {error}')
        self.__karma_points = 0
        self.__day = 0
        self.__trying += 1

    def get_karma_points(self):
        return self.__karma_points

    def print_data(self):
        message = f'Дух монаха постиг Нирвану на {self.__day} день своего существования \n' \
                  f'На это у него ушло {self.__trying} жизней'
        print(message)
        karma_log.write(message)


human = Live()
with open("karma.log", 'a') as karma_log:
    while human.get_karma_points() < 500:
        human.one_day()
    else:
        human.print_data()
