from input_stream import InputStream
from token_stream import TokenStream
from parser import Parser


def main():
    parser = Parser(' 12 + 3 * 4 ')
    print(parser.parse())


if __name__ == '__main__':
    main()
