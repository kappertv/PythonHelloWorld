import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(part1("sampleinput"), 35)

    def test_part1i(self):
        self.assertEqual(part1("input"), 226172555)
    
    def test_part2(self):
        self.assertEqual(part2("sampleinput"), 46)

    def test_part2i(self):
        self.assertEqual(part2("input"), 46)
