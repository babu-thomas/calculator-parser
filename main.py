from input_stream import InputStream
from token_stream import TokenStream


def main():
    scanner = InputStream('  21 + 3  *  3 \n')
    tokenizer = TokenStream(scanner)
    while not tokenizer.is_eof():
        print(tokenizer.next())


if __name__ == '__main__':
    main()
