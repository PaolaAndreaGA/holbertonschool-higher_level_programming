#!/usr/bin/python3

"""Unittest for max_integer(list=[])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test 6-max_integer
    """
    def test_if_empty(self):
        """Checks to make sure a list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_unordered(self):
        """Checks an unordered list"""
        un_list = [8, 6, 2, 7, 3]
        self.assertEqual(max_integer(un_list), 8)

    def test_ordered(self):
        """Checks an ordered list"""
        o_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(o_list), 5)

    def test_neg_unordered(self):
        """Checks an unordered list of negatives"""
        nun_list = [-9, -6, -4, -8, -3]
        self.assertEqual(max_integer(nun_list), -9)

    def test_neg_ordered(self):
        """Checks an ordered list of negatives"""
        no_list = [-7, -6, -5, -4, -2]
        self.assertEqual(max_integer(no_list), -2)

    def test_single(self):
        """Checks a list with a single element"""
        single = [6]
        self.assertEqual(max_integer(single), 6)

    def test_float_list(self):
        """Checks a list of floats"""
        f_list = [2.2, 5.5, 6.3, 8.9, 2.7]
        self.assertEqual(max_integer(f_list), 2.7)

    def test_float_int(self):
        """Checks a list of floats and ints"""
        f_and_i = [2.2, 1, 7.4, 9, 3.4]
        self.assertEqual(max_integer(f_and_i), 7)

    def test_string_list(self):
        """Checks a list of strings"""
        s_list = ["oh", "hello", "beato", "burrito"]
        self.assertRaises(TypeError, max_integer, "beato", s_list)

    def test_single_string(self):
        """Checks a single string"""
        single_string = ["house"]
        self.assertRaises(TypeError, max_integer, "s", single_string)

    def test_same(self):
        """Checks through a list of the same ints"""
        same_int = [30, 30, 30, 30]
        self.assertEqual(max_integer(same_int), 30)

    def test_mixed_types(self):
        """Checks to see if numbers are mixed with strings"""
        mixed = [1, 2, 3, "beat", 5]
        self.assertRaises(TypeError, max_integer, mixed)

if __name__ == '__main__':
    unittest.main()
