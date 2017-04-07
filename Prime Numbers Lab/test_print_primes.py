import unittest
from print_primes import prime_numbers_in_range


class PrintTest(unittest.TestCase):
    """docstring for MissingNumberTest"""

    def test_empty_list(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59],
                         prime_numbers_in_range(60),
                         msg='should return 0 for empty list')

    def test_it_works(self):
        list1 = prime_numbers_in_range(60)
        self.assertListEqual(list1,
                             [2, 3, 5, 7, 11, 13, 17, 19, 23,
                                 29, 31, 37, 41, 43, 47, 53, 59],
                             msg='should return the correct primes')

    def test_it_does_not_take_string(self):
        result = "invalid"
        self.assertEqual(result, prime_numbers_in_range("60"),
                         msg='should only accept integers')

    def test_it_returns_empty_list(self):
        result = []
        self.assertEqual(result, prime_numbers_in_range(-5),
                         msg='should return empty list for negative int')

    def test_it_does_not_take_list(self):
        result = "invalid"
        self.assertEqual(result, prime_numbers_in_range([]),
                         msg='should only accept integers')

if __name__ == '__main__':
    unittest.main()
