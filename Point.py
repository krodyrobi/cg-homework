class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta(self, point):
        return self.x - point.x, self.y - point.y