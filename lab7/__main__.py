#!/usr/bin/env python3
import sys
import os.path

from CartesianXPM import CartesianXPM
from ClippingWindow import ClippingWindow

import argparse
from Line import Line
from Point import Point


def parse_args():
    parser = argparse.ArgumentParser(description='Draw clipped 3rd degree bezier curves',
                                     add_help=False)

    parser.add_argument("-x", "--help", action="help", help="Prints the program usage")

    parser.add_argument("-i", "--file_in", default='./lab7/test.bze', help='The POL file containing a'
                                                                           'counter clockwise vertex list')
    parser.add_argument("-o", "--file_out", default='./lab7/out.xpm', help='The image output filepath')
    parser.add_argument("-w", "--width", default=200, type=int, help='The image width')
    parser.add_argument("-h", "--height", default=200, type=int, help='The image height')

    parser.add_argument("-t", "--window_top", default=200, type=int, help='Clipping window top (ymax)')
    parser.add_argument("-l", "--window_left", default=0, type=int, help='Clipping window left (xmin)')
    parser.add_argument("-b", "--window_bottom", default=0, type=int, help='Clipping window bottom (ymin)')
    parser.add_argument("-r", "--window_right", default=200, type=int, help='Clipping window right (xmax)')

    parser.add_argument("-p", "--precision", default=0.2, type=float,
                        help='The precision at which the bezier is formed')

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

    if not os.path.isfile(args.file_in):
        print("Input file %s does not exist" % args.file_in)
        sys.exit(1)

    xpm = CartesianXPM(args.width, args.height, 1)
    xpm.add_color(0, 0, 0, '#')
    window = ClippingWindow(args.window_top, args.window_right,
                            args.window_bottom, args.window_left)

    points = []
    with open(args.file_in, 'r') as file:
        for line in file:
            line = line.rstrip()
            tokens = line.split()

            if len(tokens) == 3:
                if tokens[-1] == 'Point':
                    coords = [int(i) for i in tokens[0:2]]
                    p1 = Point(coords[0], coords[1])
                    points.append(p1)

    len_points = len(points)
    if len_points < 4:
        print('Not enough points received a minimum of 4 required')
        sys.exit(1)

    r = (len_points - 1) // 3
    for j in range(r):
        i = 3*j
        lines = Line.bezier_3(
            points[i],
            points[i + 1],
            points[i + 2],
            points[i + 3],
            args.precision)

        for line in lines:
            line = window.clip_line(line)
            line.rasterize()
            if line is not None:
                line.draw_line(xpm, 1)

    xpm.write_to_file(args.file_out)


if __name__ == "__main__":
    main()
