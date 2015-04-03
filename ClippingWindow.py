from Line import Line
from Point import Point


class ClippingWindow(object):
    TOP = 1
    BOTTOM = 2
    RIGHT = 4
    LEFT = 8

    def __init__(self, wt, wr, wb, wl):
        self.window_top = wt
        self.window_bottom = wb
        self.window_left = wl
        self.window_right = wr

    def clip_line(self, line):
        p1 = line.p1
        p2 = line.p2

        code1 = self.__score_point(p1)
        code2 = self.__score_point(p2)

        while True:
            # totally inside the clipping window
            if (code1 | code2) == 0:
                return line

            # totally outside the window
            if not code1 & code2 == 0:
                return None

            # pick one of the points that is not 0
            code = code1 if code1 else code2

            # compute the intersection point with the clipping window
            if code & self.TOP:
                x = p1.x + (p2.x - p1.x) * (self.window_top - p1.y) / (p2.y - p1.y)
                y = self.window_top
            elif code & self.BOTTOM:
                x = p1.x + (p2.x - p1.x) * (self.window_bottom - p1.y) / (p2.y - p1.y)
                y = self.window_bottom
            elif code & self.RIGHT:
                y = p1.y + (p2.y - p1.y) * (self.window_right - p1.x) / (p2.x - p1.x)
                x = self.window_right
            else:
                y = p1.y + (p2.y - p1.y) * (self.window_left - p1.x) / (p2.x - p1.x)
                x = self.window_left

            # compute the new code for the point we just processed
            if code == code1:
                p1 = Point(x, y)
                code1 = self.__score_point(p1)
            else:
                p2 = Point(x, y)
                code2 = self.__score_point(p2)

        return Line(p1, p2)

    def clip_poly(self, point_list):
        def inside(line, point):
            dpx, dpy = line.p1.delta(point)
            dqx, dqy = line.p2.delta(point)

            return dpx * dqy > dpy * dqx

        clip_points = self.__get_clip_window()
        result = list(point_list)

        clip_size = len(clip_points)
        for c in range(clip_size):
            poly_size = len(result)
            input_points = list(result)
            result = []

            c1 = clip_points[c]
            c2 = clip_points[(c + 1) % clip_size]
            c_line = Line(c1, c2)

            for p in range(poly_size):
                p1 = input_points[p]
                p2 = input_points[(p + 1) % poly_size]
                p_line = Line(p1, p2)

                if inside(c_line, p1):
                    if inside(c_line, p2):  # case in -> in
                        result.append(p2)
                    else:                   # case in -> out
                        result.append(c_line.intersect(p_line))
                elif inside(c_line, p2):    # case out -> in
                    result.append(c_line.intersect(p_line))
                    result.append(p2)

        return result

    def __get_clip_window(self):
        return [Point(self.window_left, self.window_top),
                Point(self.window_left, self.window_bottom),
                Point(self.window_right, self.window_bottom),
                Point(self.window_right, self.window_top)]

    def __score_point(self, point):
        code = 0

        if point.y > self.window_top:
            code |= self.TOP
        elif point.y < self.window_bottom:
            code |= self.BOTTOM

        if point.x > self.window_right:
            code |= self.RIGHT
        elif point.x < self.window_left:
            code |= self.LEFT

        return code
