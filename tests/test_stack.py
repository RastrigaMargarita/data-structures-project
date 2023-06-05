"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_node(self):
        self.n1 = Node(5, None)
        self.n2 = Node("a", self.n1)
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, "a")
        self.assertEqual(self.n2.next_node.data, 5)


class TestStack(unittest.TestCase):
    def test_stack_push_and_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(str(stack), "data3\\ndata2\\ndata1")

        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            print(stack.top.next_node.next_node.next_node.data)
        self.assertEqual(stack.pop(), 'data3')
        self.assertEqual(stack.pop(), 'data2')

        stack = Stack()
        stack.push('data1')
        data = stack.pop()

        # стэк стал пустой
        self.assertIsNone(stack.top)

        # pop() удаляет элемент и возвращает данные удаленного элемента
        assert data == 'data1'

        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()

        # теперь последний элемента содержит данные data1
        self.assertEqual(stack.top.data, 'data1')

        # данные удаленного элемента
        assert data == 'data2'
