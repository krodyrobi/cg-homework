class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta(self, point):
        return self.x - point.x, self.y - point.y

    def transform(self, tsf=None):
        if not tsf:
            return None

        for trans in tsf.transfromations:
            trans(point=self)()

    def rasterize(self):
        self.x = int(self.x)
        self.y = int(self.y)