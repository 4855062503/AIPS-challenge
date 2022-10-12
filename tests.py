import unittest

import main

class TestMethods(unittest.TestCase):
    return_dates_input = "2021-12-01 179\n2021-12-05 81\n2021-12-08 134\n2021-12-09 4\n"
    return_dates_input2 = "2021-12-01 10\n2021-12-05 7\n2021-12-08 6\n2021-12-09 1\n"
    top_three_input = "2021-12-01T07:30:00 46\n2021-12-01T08:00:00 42\n2021-12-08T18:00:00 33\n"
    top_three_input2 = "2021-12-01T05:00:00 1\n2021-12-01T05:30:00 1\n2021-12-01T06:00:00 1\n"
    three_lowest_input = "2021-12-01T15:00:00 9\n2021-12-01T15:30:00 11\n2021-12-01T23:30:00 0\n"
    three_lowest_input2 = "2021-12-01T05:00:00 1\n2021-12-01T05:30:00 1\n2021-12-01T06:00:00 1\n"

    def test_total(self):
        self.assertEqual(main.count_all('input.txt'), 398)
        self.assertEqual(main.count_all('input2.txt'), 24)

    def test_return_dates(self):
        self.assertEqual(main.return_dates('input.txt'), self.return_dates_input)
        self.assertEqual(main.return_dates('input2.txt'), self.return_dates_input2)

    def test_top_three(self):
        self.assertEqual(main.top_three('input.txt'), self.top_three_input)
        self.assertEqual(main.top_three('input2.txt'), self.top_three_input2)

    def test_least_cars(self):
        self.assertEqual(main.least_cars('input.txt'), self.three_lowest_input)
        self.assertEqual(main.least_cars('input2.txt'), self.three_lowest_input2)

if __name__ == '__main__':
    unittest.main()
