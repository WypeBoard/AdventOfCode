import unittest
from Advent01 import partone, parttwo


class TestAdvent01(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_part_one_one(self):
        expence_report = [1721, 979, 366, 299, 675, 1456]
        res = partone(expence_report)

        self.assertEqual(res, 1721 * 299)

    def test_part_two_one(self):
        expence_report = [1721, 979, 366, 299, 675, 1456]
        res = parttwo(expence_report)

        self.assertEqual(res, 979 * 366 * 675)
