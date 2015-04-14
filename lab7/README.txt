WARNING THE PROGRAM CLIPS THE LINES BY DEFAULT

To run the program from the main dir of the archive (the one with all the class definitions) use:

python3.4 -m lab7 -o "./lab7/out.xpm" -i "./lab7/in.bze" -p 0.2




usage: __main__.py [-x] [-i FILE_IN] [-o FILE_OUT] [-w WIDTH] [-h HEIGHT]
                   [-t WINDOW_TOP] [-l WINDOW_LEFT] [-b WINDOW_BOTTOM]
                   [-r WINDOW_RIGHT] [-p PRECISION]

Draw clipper 3rd degree bezier curves

optional arguments:
  -x, --help            Prints the program usage
  -i FILE_IN, --file_in FILE_IN
                        The POL file containing acounter clockwise vertex list
  -o FILE_OUT, --file_out FILE_OUT
                        The image output filepath
  -w WIDTH, --width WIDTH
                        The image width
                        default: 200
  -h HEIGHT, --height HEIGHT
                        The image height
                        default: 200
  -t WINDOW_TOP, --window_top WINDOW_TOP
                        Clipping window top (ymax)
                        default: 200
  -l WINDOW_LEFT, --window_left WINDOW_LEFT
                        Clipping window left (xmin)
                        default: 0
  -b WINDOW_BOTTOM, --window_bottom WINDOW_BOTTOM
                        Clipping window bottom (ymin)
                        default: 0
  -r WINDOW_RIGHT, --window_right WINDOW_RIGHT
                        Clipping window right (xmax)
                        default: 200
  -p PRECISION, --precision PRECISION
                        The precision at which the bezier is formed
                        default: 0.2