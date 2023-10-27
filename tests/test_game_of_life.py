import unittest
from parameterized import parameterized

from src.game_of_life.game_of_life import GameOfLife


class TestGameOfLife(unittest.TestCase):
    @parameterized.expand([
        ([[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]],
         [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]),

        ([[0, 0, 0],
          [0, 1, 1],
          [0, 0, 0]],
         [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]])
    ])
    def test_underpopulation(self, initial_board, expected_board):
        game = GameOfLife(initial_board)
        game.tick()
        self.assertEqual(game.board, expected_board)


if __name__ == '__main__':
    unittest.main()
