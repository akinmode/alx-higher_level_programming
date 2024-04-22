#!/usr/bin/python3
"""Unittest module for Base"""
import unittest
from models.base import Base

id = 0
#notintegers = [3.5, [], {}, {1, 2}, {1: 2, 3: 4}, "hi", b"hi", ()]

class TestBase(unittest.TestCase):
    """Test cases for Base geometry class"""

    def testinstance(self):
        global id
        a = Base()
        id += 1
        self.assertEqual(a.id, id)
    
    def testincrement(self):
        global id
        a = Base()
        id += 1
        self.assertEqual(a.id, id)
        b = Base()
        id += 1
        self.assertEqual(b.id, id)
        c = Base()
        id += 1
        self.assertEqual(c.id, id)
    
    def testanyid(self):
        global id
        a = Base(98)
        self.assertEqual(a.id, 98)

    def testincrementanyid(self):
        global id
        a = Base()
        id += 1
        self.assertEqual(a.id, id)
        b = Base(19)
        self.assertEqual(b.id, 19)
        c = Base()
        id += 1
        self.assertEqual(c.id, id)
    
    def testnonint(self):
        global id
        astr = "hello"
        a = Base(astr)
        blist = [10, 14, 30]
        b = Base(blist)
        self.assertEqual(a.id, astr)
        self.assertEqual(b.id, blist)

if __name__ == '__main__':
    unittest.main()
