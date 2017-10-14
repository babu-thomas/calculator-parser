# {'type': 'num', 'value': 21} {'type': 'op', 'value': '+'} {'type': 'num', 'value': 3}
# {'type': 'op', 'value': '*'} {'type': 'num', 'value': 3} -> 
# {'type': 'binary', 'operator': '+',
#  'left': {'type': 'num', 'value': 21}
#  'right': {'type': 'binary', 'operator': '*',
#            'left': {'type': 'num', 'value': 3},
#            'right': {'type': 'num', 'value': 3}
#           }
# }

from token_stream import operators, TokenStream


class Parser():
    def __init__(self, token_stream):
        self.token_stream = token_stream

    def _is_op(self, which_op=None):
        token = self.token_stream.peek()
        test = token and token['type'] == 'op'
        if which_op:
            test = test and token['value'] == which_op
        return test

    def _is_num(self):
        token = self.token_stream.peek()
        return token and token['type'] == 'num'

    def _parse_num(self):
        if self._is_num():
            token = self.token_stream.next()
            return token

        actual = self.token_stream.peek()
        self.unexpected_token('num', actual)
        return None

    def parse(self):
        return self._parse_num()

    def unexpected_token(self, expected_type, actual_token):
        self.token_stream.croak('Expected token of type: ' + expected_type +
            ', found token: ' + str(actual_token))
