import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(part1("sampleinput"), 2)
        
    def test_part1b(self):
        self.assertEqual(part1("sampleinput2"), 6)
    
    def test_part1i(self):
        self.assertEqual(part1("input"), 20569)
    
    def test_part2(self):
        self.assertEqual(part2("sampleinput3"), 6)

    def test_part2i(self):
        self.assertEqual(part2("input"), 111)
    
    # 10_000_000 too low 14 minuten.
    # 100_000_000 ..
    # 1000_000_000 too low .. gaat hem zo niet worden. 1400 minuten..
    # 10_000_000_000 not right anser guessed 4 times wait 5 minutes.
    # ...
    # 100_000 9 sec
    # 1_000_000 86 sec
    # needs some performance gain
