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
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            print(stack.top.next_node.next_node.next_node.data)
        self.assertEqual(stack.pop().data, 'data3')
        self.assertEqual(stack.pop().data, 'data2')
