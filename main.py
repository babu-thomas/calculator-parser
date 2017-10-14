from input_stream import InputStream
from token_stream import TokenStream
from parser import Parser


def main():
    scanner = InputStream('  *21 + 3  *  3 \n')
    tokenizer = TokenStream(scanner)
    # while not tokenizer.is_eof():
    #     print(tokenizer.next())

    parser = Parser(tokenizer)
    print(parser.parse())


if __name__ == '__main__':
    main()
