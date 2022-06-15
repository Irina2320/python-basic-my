class QSequence:
    """
    Базовый класс.
    Берет непонятно чего.
    Возвращает непонятно чего.
    Делает это непонятно зачем.
    """
    def __init__(self, sequence) -> None:
        self.sequence = sequence[:]

    def __next__(self) -> int:
        try:
            next_q = self.sequence[-self.sequence[-1]] + self.sequence[-self.sequence[-2]]
            self.sequence.append(next_q)
            return next_q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self


q_sequence = QSequence([1, 1])

for _ in range(30):
    print(next(q_sequence))
