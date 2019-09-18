import unittest
from unittest import mock
from input_loops import average_input_scores

class testWhileAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(7, average_input_scores.average( [5, 7, 9] ))


if __name__ == '__main__':
    unittest.main()
