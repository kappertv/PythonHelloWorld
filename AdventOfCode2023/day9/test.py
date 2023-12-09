import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(part1("sampleinput"), 114)
    
    def test_part1a(self):
        self.assertEqual(part1("input"), 1806615041)
        
    def test_part2(self):
        self.assertEqual(part2("sampleinput"), 2)
    
    def test_part2i(self):
        self.assertEqual(part2("input"), 1211)
        