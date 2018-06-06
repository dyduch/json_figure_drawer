import json
from PIL import Image
from picture import Picture
from painter import Painter
import argparse
from checker import Checker


def parse_json(filename):
    file = open(filename)
    data = json.load(file)
    return data


def main():

    parser = argparse.ArgumentParser(description='Type in filepath, type in "-o" + "filepath" to specify output path')
    parser.add_argument('input',
                        help='Path to the input file.')
    parser.add_argument('-o', '--output',
                        help='Path to the output file.')
    parsed_args = parser.parse_args()
    print(parsed_args.input)
    print(parsed_args.output)

    file = open(parsed_args.input)
    data = json.load(file)

    Checker.parsed_json_contains_keys(data=data)

    pic = Picture(data)
    Checker.check_figures(pic.figures)
    Checker.check_palette(pic.palette)
    Checker.check_screen(pic.screen, pic.palette)
    painter = Painter(pic)

    image = painter.paint()
    if parsed_args.output is None:
        Image._show(image)
    else:
        if not parsed_args.output.endswith('.png'):
            parsed_args.output += '.png'
        Image._show(image)
        image.save(parsed_args.output)


if __name__ == "__main__":
    main()
