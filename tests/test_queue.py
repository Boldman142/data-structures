"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_push(self):
        a = Queue()
        a.enqueue("data1")
        self.assertTrue(a)

    def test_dequeue(self):
        a = Queue()
        new_data = "data1"
        a.enqueue(new_data)
        get_ = a.dequeue()
        self.assertEqual(get_, new_data)

    def test_str(self):
        test_class = Queue()
        self.assertEqual(print(test_class), None)
        test_class.enqueue("1")
        self.assertEqual(print(test_class), print("1"))


if __name__ == '__main__':
    unittest.main()
