import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(errorMarginPart1(), 288)
    
    def test_part2(self):
        self.assertEqual(part2(), 71503)