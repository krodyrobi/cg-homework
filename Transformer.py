from curr import gen_cur
from Point import Point
from math import radians, sin, cos


class Transformer(object):
    def __init__(self, path):
        self.input = path
        self.transformations = []
        self.read()

    def read(self):
        self.transformations = []

        with open(self.input, 'r') as file:
            for line in file:
                line = line.rstrip()
                tokens = line.split()
                func = None

                size = len(tokens)
                if tokens[0] == 't':
                    if size != 3:
                        continue

                    func = gen_cur(self._translate)
                    func = func(tx=int(tokens[1]), ty=int(tokens[2]))
                elif tokens[0] == 'r':
                    if size != 4:
                        continue

                    pivot = Point(int(tokens[1]), int(tokens[2]))
                    func = gen_cur(self._rotate)
                    func = func(pivot=pivot, angle=float(tokens[3]))
                elif tokens[0] == 's':
                    if size != 5:
                        continue

                    pivot = Point(int(tokens[1]), int(tokens[2]))
                    func = gen_cur(self._scale)
                    func = func(pivot=pivot, sx=float(tokens[3]), sy=float(tokens[4]))

                self.transformations.append(func)

    @staticmethod
    def _rotate(point, pivot, angle):
        rads = radians(angle)

        Transformer._translate(point, -pivot.x, -pivot.y)

        point.x = point.x * cos(rads) - point.y * sin(rads)
        point.y = point.x * sin(rads) + point.y * cos(rads)

        Transformer._translate(point, pivot.x, pivot.y)

    @staticmethod
    def _translate(point, tx, ty):
        point.x = point.x + tx
        point.y = point.y + ty

    @staticmethod
    def _scale(point, pivot, sx, sy):
        point.x += -pivot.x
        point.y += -pivot.y

        point.x *= sx
        point.y *= sy

        point.x += pivot.x
        point.y += pivot.y