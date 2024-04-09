#!/usr/bin/python3
"""Unit tests for max_integer in a list"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class contains tests scenerios for max_integer"""

    def test_positive(self):
        """Tests a list with no duplicates"""
        nlist = [1, 2, 5, 0, 3]
        self.assertEqual(max_integer(nlist), 5)

    def test_negative(self):
        """Tests a list with negative number largest magnitude"""
        nlist = [1, 2, 5, -6, 3]
        self.assertEqual(max_integer(nlist), 5)

    def test_negative_result(self):
        """Tests a list with negative number largest number"""
        nlist = [-1, -2, -5, -6, -3]
        self.assertEqual(max_integer(nlist), -1)

    def test_zero_result(self):
        """Tests a list with 0 as max"""
        nlist = [-1, 0, -5, -6, -3]
        self.assertEqual(max_integer(nlist), 0)

    def test_first(self):
        """Tests a list with first element max"""
        nlist = [10, 2, 5, -6, 3]
        self.assertEqual(max_integer(nlist), 10)

    def test_negative(self):
        """Tests a list with last element max"""
        nlist = [-10, -2, -5, -6, -1]
        self.assertEqual(max_integer(nlist), -1)

    def test_duplicate(self):
        """Tests a list with duplicate non-max values"""
        nlist = [1, -5, 3, 1, -5]
        self.assertEqual(max_integer(nlist), 3)

    def test_duplicate_max(self):
        """Tests a list with duplicate max and non-max values"""
        nlist = [1, -5, 3, 3, -5]
        self.assertEqual(max_integer(nlist), 3)

    def test_all_5000(self):
        """Tests a list with all values 5000"""
        nlist = [5000, 5000, 5000, 5000]
        self.assertEqual(max_integer(nlist), 5000)

    def test_all_0(self):
        """Tests a list with all values 0"""
        nlist = [0, 0, 0, 0, 0]
        self.assertEqual(max_integer(nlist), 0)

    def test_all_neg5000(self):
        """Tests a list with all values -5000"""
        nlist = [-5000, -5000, -5000, -5000]
        self.assertEqual(max_integer(nlist), -5000)

    def test_one_element(self):
        """Tests a list with all values 5000"""
        nlist = [-5000]
        self.assertEqual(max_integer(nlist), -5000)

    def test_empty(self):
        """Tests an empty list"""
        nlist = []
        self.assertIs(max_integer(nlist), None)

if __name__ == "__main__":
    unittest.main()
