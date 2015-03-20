#!/usr/bin/env python3
from CartesianXPM import CartesianXPM
from Parser import Parser
from Transformer import Transformer

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Draw lines from a PostScript file',
                                     add_help=False)

    parser.add_argument("-x", "--help", action="help", help="Prints the program usage")

    parser.add_argument("-f", "--file_in", default='./lab4/test.ps', help='The PostScript filepath')
    parser.add_argument("-t", "--file_trans", default='./lab4/test.tsf', help='The transformation filepath')
    parser.add_argument("-o", "--file_out", default='./lab4/out.xpm', help='The image output filepath')
    parser.add_argument("-w", "--width", default=200, type=int, help='The image width')
    parser.add_argument("-h", "--height", default=200, type=int, help='The image height')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    xpm = CartesianXPM(args.width, args.height, 1)
    parser = Parser(args.file_in)
    transformer = Transformer(args.file_trans)

    xpm.add_color(0, 0, 0, '#')

    lines = parser.parse()
    for line in lines:
        line.transform(transformer)
        line.draw_line(xpm, 1)

    xpm.write_to_file(args.file_out)

if __name__ == "__main__":
    main()