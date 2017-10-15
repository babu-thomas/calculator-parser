from input_stream import InputStream
from token_stream import TokenStream
from parser import Parser


def main():
    scanner = InputStream(' *** \n')
    tokenizer = TokenStream(scanner)
    parser = Parser(tokenizer)
    print(parser.parse())


if __name__ == '__main__':
    main()
