import unittest

class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        for x in ['string', 1.5]:
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self):
        for x in [ -1,  -10,  -100]:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self):
        data = [
            {'in': 0, 'out': (0,)},
            {'in':1, 'out': (1,)}
        ]
        for x in data:
            with self.subTest(x=x):
                self.assertEqual(factorize(x['in']), x['out'])

    def test_simple_numbers(self):
        data = [
            {'in': 3, 'out': (3,) },
            {'in':13, 'out': (13,)},
            {'in':29, 'out': (29,)}
        ]
        for x in data:
            with self.subTest(x=x):
                self.assertEqual(factorize(x['in']), x['out'])    

    def test_two_simple_multipliers(self):
        data = [
            {'in': 6, 'out': (2,3) },
            {'in': 26, 'out': (2, 13)},
            {'in': 121, 'out': (11, 11)}
        ]
        for x in data:
            with self.subTest(x=x):
                self.assertEqual(factorize(x['in']), x['out'])  

    def test_many_multipliers(self):
        data = [
            {'in': 1001, 'out': (7, 11, 13) },
            {'in': 9699690, 'out': (2, 3, 5, 7, 11, 13, 17, 19)}
        ]
        for x in data:
            with self.subTest(x=x):
                self.assertEqual(factorize(x['in']), x['out'])  


def factorize(x):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while x > 1:
        while x % d == 0:
            factors.append(d)
            x /= d
        d = d + 1

    return tuple(factors)

unittest.main()