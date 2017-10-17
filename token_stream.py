from input_stream import InputStream

# '2+3' -> {type:num, value: 2}, {type:op, value:'+'}, {type:num, value: 3}
operators = {
    '+': {'prec': 10, 'assoc': 'left'},
    '*': {'prec': 20, 'assoc': 'left'}
}

class TokenStream:
    def __init__(self, text):
        self.input_stream = InputStream(text)
        self.current = None
        self.has_peeked = False

    def _is_whitespace(self, char):
        return char in ' \t'

    def _is_digit(self, char):
        return char.isdigit()

    def _is_operator(self, char):
        return char in operators

    def _read_while(self, predicate_func):
        _str = ""
        while not self.input_stream.is_eof() and predicate_func(self.input_stream.peek()):
            _str += self.input_stream.next()
        return _str

    def _read_number(self):
        number = self._read_while(self._is_digit)
        return {'type': 'num', 'value': int(number)}

    def _read_operator(self):
        return {'type': 'op', 'value': self.input_stream.next()}

    def _read_next(self):
        _ = self._read_while(self._is_whitespace)
        if self.input_stream.is_eof():
            return None
        char = self.input_stream.peek()
        if self._is_digit(char):
            return self._read_number()
        if self._is_operator(char):
            return self._read_operator()
        self.input_stream.croak("Can't handle character: " + char)
        self.input_stream.next()
        return None

    def next(self):
        if self.has_peeked:
            self.has_peeked = False
            return self.current
        self.current = self._read_next()
        return self.current

    def peek(self):
        if self.has_peeked:
            return self.current
        self.current = self._read_next()
        self.has_peeked = True
        return self.current

    def is_eof(self):
        return self.peek() == None

    def croak(self, msg):
        self.input_stream.croak(msg)
