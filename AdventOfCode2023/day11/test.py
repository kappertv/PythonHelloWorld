import unittest
from solution import *

class MyFirstTests(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(part1("sampleinput"), 374)

    def test_part1i(self):
        self.assertEqual(part1("input"), 374)
