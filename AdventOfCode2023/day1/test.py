import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(sumOfAllCallibrationValuesPart1(), 142)
    
    def test_part2(self):
         self.assertEqual(sumOfAllCalibrationValuesPart2(), 281)