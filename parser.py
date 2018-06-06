from figures import *


class Parser:

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
