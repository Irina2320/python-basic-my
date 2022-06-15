class SquareGenerator:
    """
    Класс - генератор

    Args:
        limit: Лимит прогрессии

    Attributes:
        __current_val: Текущее значение генератора
    """
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__current_val = 0

    def __next__(self) -> int:
        if self.__current_val < self.__limit:
            self.__current_val += 1
            return self.__current_val ** 2
        else:
            raise StopIteration

    def __iter__(self):
        return self


def square_generator(limit):
    for value in range(1, limit + 1):
        yield value ** 2


last_number = int(input("Введите крайнее число: "))

for i in SquareGenerator(limit=last_number):
    print(i, end=' ')
else:
    print()

for i in square_generator(limit=last_number):
    print(i, end=' ')
else:
    print()

list_comprehension = [num ** 2 for num in range(1, last_number + 1)]
for number in list_comprehension:
    print(number, end=' ')



