import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(sumOfAllPartNumbersPart1(), 4361)
        