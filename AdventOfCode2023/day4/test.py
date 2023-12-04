import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(sumOfAllCardValuesPart1(), 13)
    
    def test_part2(self):
        self.assertEqual(countTotalScratchCardsPart2(), 30)