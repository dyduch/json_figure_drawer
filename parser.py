from figures import *


class Parser:

    """
    Return new figure object using from_string method defined for every Figure class
    """
    @staticmethod
    def parse_figure(figure):
            if figure['type'] == 'point':
                return Point.from_string(figure)
            elif figure['type'] == 'polygon':
                return Polygon.from_string(figure)
            elif figure['type'] == 'rectangle':
                return Rectangle.from_string(figure)
            elif figure['type'] == 'square':
                return Square.from_string(figure)
            elif figure['type'] == 'circle':
                return Circle.from_string(figure)

    """
    Return color value (in hex) from hex/rgb/words
    """
    @staticmethod
    def parse_color(color, palette):
        res = None
        if color[0] == '#':
            res = color
        elif color[0] == '(':
            res = "#"
            values = color[1:-1].replace(" ", "").split(',')
            for val in values:
                res += hex(int(val))[-2:]
        elif color in palette:
            res = palette[color]
        return res
