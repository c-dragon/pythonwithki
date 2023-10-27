import enum


class Orientation(enum.Enum):
    N = ('W', 'E')
    E = ('N', 'S')
    S = ('E', 'W')
    W = ('S', 'N')

    def __init__(self, left, right):
        self._left = left
        self._right = right

    def left(self):
        return Orientation.__members__.get(self._left)

    def right(self):
        return Orientation.__members__.get(self._right)
