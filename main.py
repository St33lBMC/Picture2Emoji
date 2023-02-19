import sys
from converter import Converter
from image_parser import Parser


def __main__():
    argc = len(sys.argv)
    converter = Converter()
    if argc != 2:
        print("your'e a failure")
    p = Parser()
    output = p.parse_to_pixel_matrix(sys.argv[1])
    test = converter.convert(output)
    print(test)


if __name__ == '__main__':
    __main__()