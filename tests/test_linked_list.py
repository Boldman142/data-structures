"""Здесь надо написать тесты с использованием unittest
 для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class TestQueue(unittest.TestCase):

    def test_str(self):
        test_class = LinkedList()
        self.assertIsNone(print(test_class))
        test_class.insert_beginning({'id': 1})
        self.assertEqual(print(test_class), print("{'id': 1} -> None"))

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 1})
        ll.insert_beginning({'id': 13})
        self.assertEqual(ll.head.data, {'id': 13})
        self.assertEqual(ll.tail.data, {'id': 1})

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 1})
        ll.insert_at_end({'id': 15})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 15})


if __name__ == '__main__':
    unittest.main()
