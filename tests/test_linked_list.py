"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    def test_node(self):
        self.n1 = Node({'id': 1})
        self.n2 = Node({'id': 15623, 'neid': "sldkfjslkd"})
        self.assertEqual(self.n1.data, {'id': 1})
        self.assertEqual(self.n2.data, {'id': 15623, 'neid': "sldkfjslkd"})
        self.n2.data = {'id': 555}
        self.assertEqual(self.n2.data, {'id': 555})
        self.assertEqual(self.n2.data, {'id': 555})


class TestLinkedList(unittest.TestCase):

    def test_insert(self):
        # Создаем пустой односвязный список
        ll = LinkedList()
        assert str(ll) == "None"
        # Добавляем данные
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        # Печатаем данные
        assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
