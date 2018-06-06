
from PIL import Image, ImageDraw
from parser import Parser


class Painter:

    def __init__(self, picture):
        self.picture = picture

    """
    Returns and Image object after drawing figures onto it. (It does not draw it, if figure has color=None)
    """

    def paint(self):
        bg_color = Parser.parse_color(self.picture.screen['bg_color'], self.picture.palette)
        fg_color = Parser.parse_color(self.picture.screen['fg_color'], self.picture.palette)

        height = self.picture.screen['height']
        width = self.picture.screen['width']

        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)

        for fig in self.picture.figures:
            if 'color' in fig:
                parsed_color = Parser.parse_color(fig['color'], self.picture.palette)
            else:
                parsed_color = fg_color

            figure = Parser.parse_figure(fig)
            figure.color = parsed_color
            if figure.color is not None:
                figure.draw(draw)

        del draw
        return image
