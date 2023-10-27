import unittest

from src.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_3(self):
        self.assertEqual(fizz_buzz(3), "Fizz")

    def test_fizz_buzz_5(self):
        self.assertEqual(fizz_buzz(5), "Buzz")

    def test_fizz_buzz_15(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")

    def test_fizz_buzz_7(self):
        self.assertEqual(fizz_buzz(7), "7")

    def test_fizz_buzz_30(self):
        self.assertEqual(fizz_buzz(30), "FizzBuzz")

    def test_fizz_buzz_negative(self):
        with self.assertRaises(ValueError):
            fizz_buzz(-3)

    def test_fizz_buzz_string(self):
        with self.assertRaises(ValueError):
            fizz_buzz("not a number")


if __name__ == '__main__':
    unittest.main()
