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


# '2+3' -> {type:num, value: 2}, {type:op, value:'+'}, {type:num, value: 3}
class TokenStream:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def is_whitespace(self, char):
        return char in ' \t'

    def is_digit(self, char):
        return char.isdigit()

    def is_operator(self, char):
        return char in '+'

    def read_while(self, predicate_func):
        _str = ""
        while not self.input_stream.is_eof() and predicate_func(self.input_stream.peek()):
            _str += self.input_stream.next()
        return _str

    def read_number(self):
        number = self.read_while(self.is_digit)
        return {'type': 'num', 'value': int(number)}

    def read_operator(self):
        operator = self.read_while(self.is_operator)
        return {'type': 'op', 'value': operator}

    def read_next(self):
        _ = self.read_while(self.is_whitespace)
        if self.input_stream.is_eof():
            return None
        char = self.input_stream.peek()
        if self.is_digit(char):
            return self.read_number()
        if self.is_operator(char):
            return self.read_operator()
        self.input_stream.croak("Can't handle character: " + char)
        self.input_stream.next()
        return None


def main():
    scanner = InputStream('  2 + 3  \n')
    tokenizer = TokenStream(scanner)
    token = tokenizer.read_next()
    while token:
        print(token)
        token = tokenizer.read_next()


if __name__ == '__main__':
    main()
