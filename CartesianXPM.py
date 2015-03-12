from Point import Point
from XPM import XPM


class CartesianXPM(XPM):
    def set_pixel(self, point, color_index=9):
        cartesian_point = Point(point.x, self.height - 1 - point.y)

        return super().set_pixel(cartesian_point, color_index)