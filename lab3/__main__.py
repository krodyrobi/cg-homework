#!/usr/bin/env python3
import sys
from CartesianXPM import CartesianXPM
from ClippingWindow import ClippingWindow
from Parser import Parser

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Draw lines from a PostScript file',
                                     add_help=False)

    parser.add_argument("-x", "--help", action="help", help="Prints the program usage")

    parser.add_argument("-f", "--file_in", default='./lab2/test.ps', help='The PostScript filepath')
    parser.add_argument("-o", "--file_out", default='./lab2/out.xpm', help='The image output filepath')
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

    parser = Parser(args.file_in)
    xpm.add_color(0, 0, 0, '#')

    lines = parser.parse()

    for line in lines:
        line = window.clip(line)

        if line is not None:
            line.draw_line(xpm, 1)

    xpm.write_to_file(args.file_out)


if __name__ == "__main__":
    main()