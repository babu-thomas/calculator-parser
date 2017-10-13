class InputStream:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.col = 0

    def next(self):
        char = self.text[self.pos]
        self.pos += 1
        self.col += 1
        return char

    def peek(self):
        return self.text[self.pos]

    def is_eof(self):
        return self.peek() == '\n'

    def croak(self, msg):
        print (msg, ' (column: ', self.col, ')', sep="")


def main():
    scanner = InputStream('Heya')
    scanner.next()
    scanner.croak('Something happened')


if __name__ == '__main__':
    main()
