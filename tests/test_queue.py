"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Node, Queue


class TestNode(unittest.TestCase):

    def test_node(self):
        self.n1 = Node(5)
        self.n2 = Node("a")
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, "a")


class TestStack(unittest.TestCase):
    def test_queue_queue(self):
        queue = Queue()
        self.assertEqual(str(Queue()), "")
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.next_node, None)

        self.assertEqual(str(queue), "data1\\ndata2\\ndata3")
