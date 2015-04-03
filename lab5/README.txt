I've looked up to see how to parse args of the kind `-wl` but the standard is that `wl` would be considered to be 2 arguments `w` AND `l` so I've chaged them to use some other keys and a long notation see below.

To run the program from the main dir of the archive (the one with all the class definitions) use:

python3.4 -m lab3 -o "./lab5/out.xpm" --window_top=150 --window_left=50 --window_right=100 --window_bottom=100





usage: __main__.py [-x] [-f FILE_IN] [-o FILE_OUT] [-w WIDTH] [-h HEIGHT]
                   [-i WINDOW_TOP] [-j WINDOW_LEFT] [-k WINDOW_BOTTOM]
                   [-l WINDOW_RIGHT]

Draw clipped polygons

optional arguments:
  -x, --help            Prints the program usage
  -f FILE_IN, --file_in FILE_IN
                        The POL file containing acounter clockwise vertex list
  -o FILE_OUT, --file_out FILE_OUT
                        The image output filepath
  -w WIDTH, --width WIDTH
                        The image width
  -h HEIGHT, --height HEIGHT
                        The image height
  -i WINDOW_TOP, --window_top WINDOW_TOP
                        Clipping window top (ymax)
  -j WINDOW_LEFT, --window_left WINDOW_LEFT
                        Clipping window left (xmin)
  -k WINDOW_BOTTOM, --window_bottom WINDOW_BOTTOM
                        Clipping window bottom (ymin)
  -l WINDOW_RIGHT, --window_right WINDOW_RIGHT
                        Clipping window right (xmax)