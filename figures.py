
class Figure:
    @staticmethod
    def from_string(string):
        pass


class Point(Figure):
    def __init__(self, x, y, color=None):
        self.xy = [(x, y)]
        self.color = color

    def draw(self, draw):
        draw.point(self.xy, self.color)

    @staticmethod
    def from_string(string):
        return Point(string['x'], string['y'])


class Polygon(Figure):
    def __init__(self, points, color=None):
        self.points = points
        self.color = color

    def draw(self, draw):
        draw.polygon(self.points, self.color)

    @staticmethod
    def from_string(string):
        return Polygon([tuple(point) for point in string['points']])


class Rectangle(Figure):
    def __init__(self, x, y, width, height, color=None):
        self.points = [(x, y), (x+width, y+height)]
        self.color = color

    def draw(self, draw):
        draw.rectangle(self.points, self.color)

    @staticmethod
    def from_string(string):
        return Rectangle(string['x'], string['y'], string['width'], string['height'])


class Square(Figure):
    def __init__(self, x, y, size, color=None):
        self.points = [(x, y), (x+size, y+size)]
        self.color = color

    def draw(self, draw):
        draw.rectangle(self.points, self.color)

    @staticmethod
    def from_string(string):
        return Square(string['x'], string['y'], string['size'])


class Circle(Figure):
    def __init__(self, x, y, radius, color=None):
        self.points = [(x - radius, y - radius), (x + radius, y + radius)]
        self.color = color

    def draw(self, draw):
        draw.ellipse(self.points, self.color)

    @staticmethod
    def from_string(string):
        return Circle(string['x'], string['y'], string['radius'])
