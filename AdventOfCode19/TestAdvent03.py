import unittest
from Advent03 import partone, parttwo


class TestAdvent01(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_part_one_one(self):
        intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        expected_output = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        res = partone(intcode)

        self.assertEqual(res, expected_output)

    def test_part_one_two(self):
        intcode = [1, 0, 0, 0, 99]
        expected_output = [2, 0, 0, 0, 99]
        res = partone(intcode)

        self.assertEqual(res, expected_output)

    def test_part_one_three(self):
        intcode = [2, 3, 0, 3, 99]
        expected_output = [2, 3, 0, 6, 99]
        res = partone(intcode)

        self.assertEqual(res, expected_output)

    def test_part_one_four(self):
        intcode = [2, 4, 4, 5, 99, 0]
        expected_output = [2, 4, 4, 5, 99, 9801]
        res = partone(intcode)

        self.assertEqual(res, expected_output)

    def test_part_one_five(self):
        intcode = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expected_output = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        res = partone(intcode)

        self.assertEqual(res, expected_output)
