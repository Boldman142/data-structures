"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        a = Stack()
        a.push("data1")
        self.assertTrue(a)

    def test_pop(self):
        a = Stack()
        new_data = "data1"
        a.push(new_data)
        get_ = a.pop()
        # print(get_)
        # print(new_data)
        self.assertEqual(get_, new_data)

    def test_str(self):
        test_class = Stack()
        self.assertEqual(print(test_class), print("Стэк пустой"))
        test_class.push(1)
        self.assertEqual(print(test_class), print("1 next(None)"))


if __name__ == '__main__':
    unittest.main()
