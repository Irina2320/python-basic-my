"""
Немного не догнал вторую часть задания. Просят реализовать стек, но по факту этот стек приходится сортировать
Что лишает смысла всю суть такой структуры
Кароч я реализовал его на словаре
так проще и быстрее
если надо переделать - пишите)
"""


class Stack:
    def __init__(self):
        self.__my_stack = []

    def add_new_element(self, element):
        self.__my_stack.append(element)

    def extract_element(self):
        if self.__my_stack:
            return self.__my_stack.pop()
        else:
            print('Невозможно извлечь! Стек пуст.')
            return None


class TaskManager:
    def __init__(self):
        self.__my_stack = dict()

    def new_task(self, task, priority):
        if priority not in self.__my_stack:
            self.__my_stack[priority] = [task]
        else:
            self.__my_stack[priority].append(task)

    def __str__(self):
        all_task = ''
        for priority, tasks in sorted(self.__my_stack.items()):
            all_task += str(priority) + ' '
            for task in tasks:
                all_task += task + '; '
            else:
                all_task = all_task[:-2] + '\n'
        return all_task


data = Stack()
data.add_new_element(123)
data.add_new_element([1, 2, 3])
data.add_new_element('Alyx')
print(data.extract_element())
print(data.extract_element())
print(data.extract_element())
print(data.extract_element())


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
