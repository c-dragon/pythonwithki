class GameOfLife:
    def __init__(self, board):
        self.board = board

    def tick(self):
        self.board = \
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]