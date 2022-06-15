class Node:
    """
    Узел. Хранит данные (element: Любой тип данных) и ссылку на следующий узел (next_node)

    Args:
        element: Любой тип данных

    Attributes:
        next_node: ссылка на следующий узел
    """

    def __init__(self, element=None) -> None:
        self.element = element
        self.next_node = None


class LinkedList:
    """
    Базовый класс списка.

    Attributes:
        head: ссылка на первый узел
    """

    def __init__(self) -> None:
        self.head = None

    def append(self, new_element) -> None:
        """
        Функция добавления элемента в конец списка
        Сначала создает новый узел, затем пробегается по всем узлам
        Если в узле не указана ссылка на следующий узел, то он и является последним
        и его ссылка (next_node) переписывается, указывая на новый элемент

        :param new_element: Данные, которые нужно положить в новый узел. Любой тип данных
        """

        new_node = Node(new_element)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def get(self, element_index: int):
        """
        Функция для получения элемента по индексу.

        :param element_index: Индекс искомого элемента
        """

        last_node = self.head
        node_index = 0
        while node_index <= element_index:
            if node_index == element_index:
                return last_node.element
            node_index += 1
            last_node = last_node.next_node

    def remove(self, remove_element_index: int) -> None:
        """
        Функция для получения элемента по индексу.
        Пробегает по всем элементам в списке с помощью счетчика
        Как найдет элемент - переприсвоит ссылки: предыдущий элемент будет указывать на следующий

        :param remove_element_index: Индекс искомого элемента
        """

        node_index = 0
        head_element = self.head

        if remove_element_index == 0:
            self.head = head_element.next_node
            return

        while node_index <= remove_element_index:
            node_index += 1
            last_element = head_element
            head_element = head_element.next_node

            if node_index == remove_element_index:
                last_element.next_node = head_element.next_node
                return

    def __str__(self) -> str:
        """
        Возвращаем красивый список в виде строки

        :return: str
        """
        current_element = self.head
        all_elements = '['
        while current_element is not None:
            all_elements += (str(current_element.element) + ', ')
            current_element = current_element.next_node
        all_elements = all_elements[:-2] + ']'
        return all_elements


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
