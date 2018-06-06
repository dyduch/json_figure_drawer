import sys
import re

class Checker:

    @staticmethod
    def parsed_json_contains_keys(data):
        figures = 'Figures' in data
        screen = 'Screen' in data
        palette = 'Palette' in data

        if figures is False or palette is False or screen is False:
            print('The file doesn\'t contain necessary elements!')
            sys.exit(1)

    @staticmethod
    def check_point(point):
        if 'x' not in point or 'y' not in point:
            raise TypeError('Point type has to have x and y values' + point)
        try:
            int(point['x'])
            int(point['y'])
        except ValueError:
            print('x and y of Point have to be Integers')
            sys.exit(1)

    @staticmethod
    def check_polygon(polygon):
        if 'points' not in polygon:
            raise TypeError('Polygon type has to have its points values')
        points = polygon['points']
        for point in points:
            if len(point) != 2:
                print('Point of a polygon ccan have only two values! ')
                sys.exit(1)
            try:
                int(point[0])
                int(point[1])
            except ValueError:
                print('x and y of every point of Polygon have to be Integers')
                sys.exit(1)

    @staticmethod
    def check_rectangle(rect):
        if 'x' not in rect or 'y' not in rect or 'height' not in rect or 'width' not in rect:
            raise TypeError('Rectangle type has to have x, y, height and width values')
        try:
            int(rect['x'])
            int(rect['y'])
            int(rect['height'])
            int(rect['width'])
        except ValueError:
            print('x and y and height and width of Rectangle have to be Integers')
            sys.exit(1)

    @staticmethod
    def check_square(square):
        if 'x' not in square or 'y' not in square or 'size' not in square:
            raise TypeError('Square type has to have x, y and size values')
        try:
            int(square['x'])
            int(square['y'])
            int(square['size'])
        except ValueError:
            print('x and y and size of Square have to be Integers')
            sys.exit(1)

    @staticmethod
    def check_circle(circle):
        if 'x' not in circle or 'y' not in circle or 'radius' not in circle:
            raise TypeError('Circle type has to have x, y and radius values')
        try:
            int(circle['x'])
            int(circle['y'])
            int(circle['radius'])
        except ValueError:
            print('x and y and radius of Circle have to be Integers')
            sys.exit(1)

    @staticmethod
    def check_figures(figures):
        for figure in figures:
            if figure['type'] == 'point':
                Checker.check_point(figure)
            elif figure['type'] == 'polygon':
                Checker.check_polygon(figure)
            elif figure['type'] == 'rectangle':
                Checker.check_rectangle(figure)
            elif figure['type'] == 'square':
                Checker.check_square(figure)
            elif figure['type'] == 'circle':
                Checker.check_circle(figure)
            else:
                raise TypeError('This figure type is not allowed: ' + figure['type'])

    @staticmethod
    def check_palette(palette):
        for key in palette:
            match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', palette[key])
            if not match:
                print('Color value in palette has to be hex value!')
                print(palette[key])
                sys.exit(1)
            match = re.search(r'\d', key)
            if match:
                print('Color key has to be a "normal" color name!')
                print(key)
                sys.exit(1)

    @staticmethod
    def check_screen(screen, palette):
        if 'height' not in screen or 'width' not in screen or 'bg_color' not in screen or 'fg_color' not in screen:
            raise TypeError('Screen has to have height, width, bg_color and fg_color values')
        try:
            int(screen['height'])
            int(screen['width'])
        except ValueError:
            print('height and with of screen have to be Integers')
            sys.exit(1)
        if screen['bg_color'] not in palette or screen['fg_color'] not in palette:
            print('bg_color and fg_color color names have to be in palette!')
            sys.exit(1)