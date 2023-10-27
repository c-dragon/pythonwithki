import unittest
from parameterized import parameterized

def sequence(n):
    return (n + 1) * (n - 1)

def more_complex_sequence(n):
    return (n + 1) * (2*n - 1)


class TestSequences(unittest.TestCase):
    @parameterized.expand([
        (0, -1),
        (1, 0),
        (-2, 3),
        (5, 24)
    ])
    def test_sequence(self, n, expected):
        self.assertEqual(expected, sequence(n))

    @parameterized.expand([
        (0, -1),
        (1, 2),
        (-2, 5),
        (5, 54)
    ])
    def test_more_complex_sequence(self, n, expected):
        self.assertEqual(expected, more_complex_sequence(n))


if __name__ == '__main__':
    unittest.main()
