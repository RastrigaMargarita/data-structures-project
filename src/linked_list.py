class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.__data = data
        self.next_node = None

    @property
    def data(self):

        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node_to_add = Node(data)

        if self.head is not None:
            node_to_add.next_node = self.head
        self.head = node_to_add

        if self.tail is None:
            self.tail = node_to_add
    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node_to_add = Node(data)

        if self.tail is not None:
            self.tail.next_node = node_to_add
        self.tail = node_to_add

        if self.head is None:
            self.head = node_to_add

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()

    def to_list(self):
        """возвращает список с данными, содержащимися в односвязном списке `LinkedList`"""
        i = self.head
        list_to_return = []
        while (i != None):
            list_to_return.append(i.data)
            i = i.next_node

        return list_to_return

    def get_data_by_id(self, id):
        """возвращает первый найденный в `LinkedList` словарь с ключом 'id', значение которого равно переданному в метод значению"""


        i = self.head
        while (i != None):
            try:
                if i.data["id"] == id:
                     return i.data
            except Exception:
                print("# Данные не являются словарем или в словаре нет id.")
            finally:
                i = i.next_node
