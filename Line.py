from Point import Point


class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def delta(self):
        return self.p1.delta(self.p2)

    def intersect(self, line):
        _, dqy = self.p2.delta(self.p1)
        dqx, _ = self.p1.delta(self.p2)

        _, dpy = line.p2.delta(line.p1)
        dpx, _ = line.p1.delta(line.p2)

        C1 = dqy * self.p1.x + dqx * self.p1.y
        C2 = dpy * line.p1.x + dpx * line.p1.y
        det = dqy * dpx - dpy * dqx

        x = (dpx * C1 - dqx * C2) / det
        y = (dqy * C2 - dpy * C1) / det

        return Point(x, y)

    def rasterize(self):
        self.p1.rasterize()
        self.p2.rasterize()

    def transform(self, transformer=None):
        if not transformer:
            return None

        for trans in transformer.transformations:
            trans(point=self.p1)()
            trans(point=self.p2)()

        self.rasterize()

    def draw_line(self, xpm, color_index):
        # Assume X/Y are decrementing with each step
        x_step = -1
        y_step = -1

        # Delta values
        dx, dy = self.delta()
        dx, dy = abs(dx), abs(dy)

        # Delta values * 2 to avoid floating point computations
        dy_2 = (dy << 1)
        dx_2 = (dx << 1)

        # Compute the increment on the x axis
        if self.p1.x < self.p2.x:
            x_step = 1

        # Compute the increment on the y axis
        if self.p1.y < self.p2.y:
            y_step = 1

        # Working point and decision variable
        point = Point(self.p1.x, self.p1.y)
        D = 0

        # Y is the major axis
        if dy > dx:
            while point.y != self.p2.y:
                xpm.set_pixel(point, color_index)
                point.y += y_step
                D += dx_2

                if D > dy:
                    point.x += x_step
                    D -= dy_2
        else:
            while point.x != self.p2.x:
                xpm.set_pixel(point, color_index)

                point.x += x_step
                D += dy_2

                if D > dx:
                    point.y += y_step
                    D -= dx_2

        xpm.set_pixel(point, color_index)