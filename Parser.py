from Line import Line
from Point import Point


class Parser(object):
    def __init__(self, path):
        self.path = path

    def parse(self):
        objects = []

        with open(self.path, 'r') as file:
            begin_found = False

            for line in file:
                line = line.rstrip()

                if not begin_found:
                    if line == '%%%BEGIN':
                        begin_found = True
                        continue

                if line == '%%%END':
                    break

                tokens = line.split()

                if len(tokens) == 5:
                    if tokens[-1] == 'Line':
                        coords = [int(i) for i in tokens[0:4]]
                        p1 = Point(coords[0], coords[1])
                        p2 = Point(coords[2], coords[3])
                        objects.append(Line(p1, p2))

        return objects
