"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):


    def test_push(self):
        a = Stack()
        a.push("data1")
        self.assertTrue(a)




if __name__ == '__main__':
    unittest.main()
