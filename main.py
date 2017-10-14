from input_stream import InputStream
from token_stream import TokenStream


def main():
    scanner = InputStream('  2 + 3  \n')
    tokenizer = TokenStream(scanner)
    token = tokenizer.read_next()
    while token:
        print(token)
        token = tokenizer.read_next()


if __name__ == '__main__':
    main()
