import unittest

from src.hello_world import HelloWorld


class TestHelloWorld(unittest.TestCase):

    def test_greeting(self):
        hello_world = HelloWorld("Hello Friedrichsdorf")
        self.assertEqual(hello_world.greeting, "Hello Friedrichsdorf")


if __name__ == '__main__':
    unittest.main()
