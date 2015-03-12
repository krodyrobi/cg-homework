from Point import Point


class XPM(object):
    def __init__(self, width, height, chars_per_pixel=1):
        self.width = width
        self.height = height

        if chars_per_pixel < 1:
            chars_per_pixel = 1

        self.chars_per_pixel = chars_per_pixel
        self.color_count = 1
        self.colors = [(255, 255, 255, "~" * chars_per_pixel)]

        self.data = [[0 for x in range(height)] for x in range(width)]

    def add_color(self, r, g, b, chars):
        if (r < 0 or r > 255) or (g < 0 or g > 255) or (b < 0 or b > 255):
            return False

        if self.chars_per_pixel < len(chars):
            return False

        for color in self.colors:
            if color[3] == chars:
                return False

        self.colors.append((r, g, b, chars))
        self.color_count += 1

        return True

    def fill_color(self, color_index=0):
        if color_index >= self.color_count:
            return False

        for row in range(self.width):
            for col in range(self.height):
                self.set_pixel(Point(row, col), color_index)

        return True

    def set_pixel(self, point, color_index=0):
        if point.x >= self.width or point.y >= self.height or color_index >= self.color_count:
            return False

        self.data[point.y][point.x] = color_index

        return True

    def write_to_file(self, path='./out.xpm'):
        with open(path, 'w') as f:
            # Header
            f.write("/* XPM */\nstatic char * image[] = {\n")

            # Values
            f.write("/* width,height,nrcolors,charsperpixel */\n")
            f.write("\"%u %u %u %u\",\n" % (self.width, self.height,
                    self.color_count, self.chars_per_pixel))

            # Colors
            f.write("/* colors #RRGGBB */\n")
            for i in range(self.color_count):
                color = self.colors[i]
                chars = color[3]
                f.write("\"%s c #%06x\",\n" % (chars, self.rgb_to_num(*color[0:3])))

            # Pixels
            f.write("/* pixels */\n")
            for row in range(self.height):
                f.write("\"")
                for col in range(self.width):
                    c = self.colors[ self.data[row][col] ]
                    f.write("%s" % c[3])
                f.write("\",\n")

            f.write("};")

    @staticmethod
    def rgb_to_num(r, g, b):
        return ((r & 0xff) << 16) + ((g & 0xff) << 8) + (b & 0xff)