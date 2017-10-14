# '2+3' -> {type:num, value: 2}, {type:op, value:'+'}, {type:num, value: 3}
operators = {
    '+': {'prec': 10, 'assoc': 'left'},
    '*': {'prec': 20, 'assoc': 'left'}
}

class TokenStream:
    def __init__(self, input_stream):
        self.input_stream = input_stream
        self.current = None
        self.has_peeked = False

    def is_whitespace(self, char):
        return char in ' \t'

    def is_digit(self, char):
        return char.isdigit()

    def is_operator(self, char):
        return char in operators

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

    def next(self):
        if self.has_peeked:
            self.has_peeked = False
            return self.current
        self.current = self.read_next()
        return self.current

    def peek(self):
        if self.has_peeked:
            return self.current
        self.current = self.read_next()
        self.has_peeked = True
        return self.current

    def is_eof(self):
        return self.peek() == None
