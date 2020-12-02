import unittest
from Advent02 import partone, parttwo


class TestAdvent01(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_part_one_one(self):
        passwordlines = ['1 3 a abcde',
                         '1 3 b cdefg',
                         '2 9 c ccccccccc']
        res = partone(passwordlines)

        self.assertEqual(res, 2)

    def test_part_two_one(self):
        passwordlines = ['1 3 a abcde',
                         '1 3 b cdefg',
                         '2 9 c ccccccccc']
        res = parttwo(passwordlines)

        self.assertEqual(res, 1)
