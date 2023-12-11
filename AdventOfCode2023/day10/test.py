import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1_1(self):
        self.assertEqual(part1("sampleinput1"), 4)

    def test_part1_1a(self):
        self.assertEqual(part1("sampleinput1a"), 4)

    def test_part1_2(self):
        self.assertEqual(part1("sampleinput2"), 8)

    def test_part1_2a(self):
        self.assertEqual(part1("sampleinput2a"), 8)
    
    # def test_part1a(self):
    #     self.assertEqual(part1("input"), 1806615041)
        
    # def test_part2(self):
    #     self.assertEqual(part2("sampleinput"), 2)
    
    # def test_part2i(self):
    #     self.assertEqual(part2("input"), 1211)
        