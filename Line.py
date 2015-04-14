from Point import Point


class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @staticmethod
    def bezier_3(p1, p2, p3, p4, step=0.2):
        """
            Linear bezier P0 P1
            B(t) = P0 + t*(P1 - P0) = (1-t)*P0 + t*P1

            Quadric bezier P0 P1 P2
            Bc(t) = (1-t)*B01(t) + t*B12(t) = (1-t)*((1-t)*P0 + t*P1) + t*((1-t)*P1 + t*P2)
                                            = (1-t)^2 * P0 + (1-t)*t*P1 + t*(1-t)*P1 + t^2*P2
                                            = (1-t)^2 * P0 + 2 * (1 - t) * t * P1 + t^2 * P2

            Qubic bezier P0 P1 P2 P3
            Bq(t) = (1-t) * Bc012(t) + t * Bc123(t) = (1-t)^3 * P0 + 3 * (1-t)^2 * t * P1 + 3(1-t) * t^2 * P2 + t^3*P3

            And so on..
        """

        points = []

        t = 0
        while t < 1.:
            t += step

            # a, b, c, d are the coefficients of the 3rd degree bezier from the formula above
            a = (1. - t)**3
            b = 3. * t * (1. - t)**2
            c = 3.0 * t**2 * (1.0 - t)
            d = t**3

            x = a * p1.x + b * p2.x + c * p3.x + d * p4.x
            y = a * p1.y + b * p2.y + c * p3.y + d * p4.y

            points.append(Point(x, y))

        lines = []
        for i in range(len(points) - 1):
            lines.append(Line(points[i], points[i+1]))

        return lines


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

    def __str__(self):
        return 'Line( ' + str(self.p1) + ", " + str(self.p2) + ')'

    def __repr__(self):
        return 'Line( ' + str(self.p1) + ", " + str(self.p2) + ')'