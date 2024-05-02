
XY = 'xy'
XYZ = 'xyz'

class Point:
    def __init__(self, weight, x, y, z=None):
        self.w = weight
        self.x = x
        self.y = y
        if z is None:
            self.type = XY
            self.z = 0
        else:
            self.type = XYZ
            self.z = z

    def __str__(self):
        if self.type == XY:
            return f'({self.x}, {self.y}, w={self.w})'
        else:
            return f'({self.z}, {self.x}, {self.y}, w={self.w})'

    def __copy__(self):
        return Point(self.w, self.x, self.y, self.z if self.type == XYZ else None)