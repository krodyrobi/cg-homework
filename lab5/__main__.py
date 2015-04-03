#!/usr/bin/env python3
import sys
from CartesianXPM import CartesianXPM
from ClippingWindow import ClippingWindow

import argparse
from Line import Line
from Point import Point


def parse_args():
    parser = argparse.ArgumentParser(description='Draw clipped polygons',
                                     add_help=False)

    parser.add_argument("-x", "--help", action="help", help="Prints the program usage")

    parser.add_argument("-f", "--file_in", default='./lab5/test.pol', help='The POL file containing a'
                                                                           'counter clockwise vertex list')
    parser.add_argument("-o", "--file_out", default='./lab5/out.xpm', help='The image output filepath')
    parser.add_argument("-w", "--width", default=200, type=int, help='The image width')
    parser.add_argument("-h", "--height", default=200, type=int, help='The image height')

    parser.add_argument("-i", "--window_top", default=200, type=int, help='Clipping window top (ymax)')
    parser.add_argument("-j", "--window_left", default=0, type=int, help='Clipping window left (xmin)')
    parser.add_argument("-k", "--window_bottom", default=0, type=int, help='Clipping window bottom (ymin)')
    parser.add_argument("-l", "--window_right", default=200, type=int, help='Clipping window right (xmax)')

    args = parser.parse_args()

    if (args.window_top > args.height or args.window_bottom < 0
        or args.window_right > args.width or args.window_left < 0
        or args.window_top < args.window_bottom
        or args.window_left > args.window_right):

            print("Clipping window is either invalid or is greater than the image to be produced")
            sys.exit(0)

    return args


def main():
    args = parse_args()

    xpm = CartesianXPM(args.width, args.height, 1)
    window = ClippingWindow(args.window_top, args.window_right,
                            args.window_bottom, args.window_left)

    xpm.add_color(0, 0, 0, '#')
    coords = []

    with open(args.file_in, 'r') as f:
        l = f.readline()
        if not l:
            print("POL file empty")
            sys.exit(1)

        floats = [float(x) for x in l.split()]
        if len(floats) % 2 == 1:
            print("POL file does not contain x y pairs")
            sys.exit(1)
        for num in range(0, len(floats), 2):
            coords.append(Point(floats[num], floats[num + 1]))

    new_list = window.clip_poly(coords)
    new_size = len(new_list)
    if new_size >= 3:
        for i in range(new_size):
            p1 = new_list[i]
            p2 = new_list[(i + 1) % new_size]
            line = Line(p1, p2)
            line.rasterize()
            line.draw_line(xpm, 1)

    xpm.write_to_file(args.file_out)


if __name__ == "__main__":
    main()