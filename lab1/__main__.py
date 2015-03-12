#!/usr/bin/env python3
from CartesianXPM import CartesianXPM
from Point import Point


def get_string(index):
    return "" + chr(index)


def main():
    xpm = CartesianXPM(50, 50, 1)

    for i in range(50):
        red = int(i / 49. * 255)
        xpm.add_color(red, 0, 0, get_string(i + 35))

        for j in range(50):
            xpm.set_pixel(Point(i, j), i + 1)

    xpm.write_to_file('./lab1/out.xpm')

if __name__ == "__main__":
    main()