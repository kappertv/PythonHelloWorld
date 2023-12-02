import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(sumOfAllValidGamesPart1(), 8)
        
    def test_part2(self):
        self.assertEqual(sumOfAllPowerGamesPart2(), 2286)
    