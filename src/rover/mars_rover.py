from rover.orientation import Orientation


class MarsRover:

    def __init__(self, x, y, orientation, planet_width=10, planet_height=10):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.planet_width = planet_width
        self.planet_height = planet_height

    def move(self, commands):
        for command in commands:
            if command == 'M':
                self._move_forward()
            else:
                self._turn(command)

            self._handle_north_pole_crossing()
            self._handle_south_pole_crossing()

    def _handle_north_pole_crossing(self):
        if self.y >= self.planet_height:
            self.x = self.planet_width - (self.x + 1)
            self.y = self.planet_height - 1
            self.orientation = Orientation.S

    def _handle_south_pole_crossing(self):
        if self.y < 0:
            self.x = self.planet_width - (self.x + 1)
            self.y = 0
            self.orientation = Orientation.N

    def _move_forward(self):
        if self.orientation == Orientation.N:
            self.y = self.y + 1
        elif self.orientation == Orientation.E:
            self.x = (self.x + 1) % self.planet_width
        elif self.orientation == Orientation.S:
            self.y = self.y - 1
        elif self.orientation == Orientation.W:
            self.x = (self.x - 1) % self.planet_width

    def _turn(self, direction):
        if direction == 'L':
            self.orientation = self.orientation.left()
        elif direction == 'R':
            self.orientation = self.orientation.right()
