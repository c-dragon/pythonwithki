import unittest

from parameterized import parameterized

from rover.mars_rover import MarsRover
from rover.orientation import Orientation


class TestMarsRover(unittest.TestCase):
    @parameterized.expand([
        (Orientation.N, 1, 2),
        (Orientation.E, 2, 1),
        (Orientation.S, 1, 0),
        (Orientation.W, 0, 1)
    ])
    def test_move_forward(self, orientation, expected_x, expected_y):
        rover = MarsRover(1, 1, orientation)
        rover.move('M')
        self.assertEqual(rover.x, expected_x)
        self.assertEqual(rover.y, expected_y)
        self.assertEqual(rover.orientation, orientation)

    @parameterized.expand([
        (Orientation.N, Orientation.W),
        (Orientation.E, Orientation.N),
        (Orientation.S, Orientation.E),
        (Orientation.W, Orientation.S)
    ])
    def test_turn_left(self, initial_orientation, expected_orientation):
        rover = MarsRover(0, 0, initial_orientation)
        rover.move('L')
        self.assertEqual(rover.x, 0)
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.orientation, expected_orientation)

    @parameterized.expand([
        (Orientation.W, Orientation.N),
        (Orientation.N, Orientation.E),
        (Orientation.E, Orientation.S),
        (Orientation.S, Orientation.W)
    ])
    def test_turn_right(self, initial_orientation, expected_orientation):
        rover = MarsRover(0, 0, initial_orientation)
        rover.move('R')
        self.assertEqual(rover.x, 0)
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.orientation, expected_orientation)

    @parameterized.expand([
        (0, Orientation.W, 9),
        (9, Orientation.E, 0)
    ])
    def test_move_across_equator(self, initial_x, orientation, expected_x):
        rover = MarsRover(initial_x, 0, orientation)
        rover.move('M')
        self.assertEqual(rover.x, expected_x)
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.orientation, orientation)

    @parameterized.expand([
        (0, 9),
        (4, 5),
        (9, 0)
    ])
    def test_cross_north_pole(self, initial_x, expected_x):
        rover = MarsRover(initial_x, 9, Orientation.N)
        rover.move('M')
        self.assertEqual(rover.x, expected_x)
        self.assertEqual(rover.y, 9)
        self.assertEqual(rover.orientation, Orientation.S)

    @parameterized.expand([
        (0, 9),
        (4, 5),
        (9, 0)
    ])
    def test_cross_south_pole(self, initial_x, expected_x):
        rover = MarsRover(initial_x, 0, Orientation.S)
        rover.move('M')
        self.assertEqual(rover.x, expected_x)
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.orientation, Orientation.N)

    def test_multiple_moves(self):
        rover = MarsRover(1, 2, Orientation.N)
        rover.move('LMLMLMLMM')
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 3)
        self.assertEqual(rover.orientation, Orientation.N)


if __name__ == '__main__':
    unittest.main()
