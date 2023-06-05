class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.__data = data
        self.next_node = None

    @property
    def data(self):

        try:
            if self is None:
                raise AttributeError("AttributeError: 'NoneType' object has no attribute 'data'")
            else:
                return self.__data
        except AttributeError as e:
            return e

    @data.setter
    def data(self, value):
        self.data = value


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node_to_add = Node(data)

        if self.tail is not None:
            self.tail.next_node = node_to_add
        self.tail = node_to_add

        if self.head is None:
            self.head = node_to_add

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        node_to_return = self.head

        if self.tail is not None:
            self.head = self.head.next_node

        return node_to_return

    def __str__(self):
        """
        :return: представление объекта
        """
        if self.head is None:
            return ""

        string_to_return = self.head.data
        next_node = self.head.next_node
        while next_node is not None:
            string_to_return += ("\\n" + next_node.data)
            next_node = next_node.next_node

        return string_to_return
