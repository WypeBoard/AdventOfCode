import unittest
from Advent01 import partone, parttwo


class TestAdvent01(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_part_one_one(self):
        mass = [12]
        required_fuel = 2
        res = partone(mass)

        self.assertEqual(res, required_fuel)

    def test_part_one_two(self):
        mass = [14]
        required_fuel = 2
        res = partone(mass)

        self.assertEqual(res, required_fuel)

    def test_part_one_three(self):
        mass = [1969]
        required_fuel = 654
        res = partone(mass)

        self.assertEqual(res, required_fuel)

    def test_part_one_four(self):
        mass = [100756]
        required_fuel = 33583
        res = partone(mass)

        self.assertEqual(res, required_fuel)

    def test_part_two_one(self):
        mass = [14]
        required_fuel = 2
        res = parttwo(mass)

        self.assertEqual(res, required_fuel)

    def test_part_two_two(self):
        mass = [1969]
        required_fuel = 966
        res = parttwo(mass)

        self.assertEqual(res, required_fuel)

    def test_part_two_three(self):
        mass = [100756]
        required_fuel = 50346
        res = parttwo(mass)

        self.assertEqual(res, required_fuel)

    def test_part_two_four(self):
        mass = [14, 1969, 100756]
        required_fuel = 51314
        res = parttwo(mass)

        self.assertEqual(res, required_fuel)
