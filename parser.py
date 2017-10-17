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
    def __init__(self, text):
        self.token_stream = TokenStream(text)

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

    def _parse_expression(self, left, current_prec):
        if left and self._is_op():
            op_token = self.token_stream.peek()
            next_prec = operators[op_token['value']]['prec']
            if next_prec >= current_prec:
                self.token_stream.next()
                if operators[op_token['value']]['assoc'] == 'left':
                    new_prec = next_prec+1
                else:
                    new_prec = next_prec
                right = self._parse_expression(self._parse_num(), new_prec)
                ast = {'type': 'binary', 'operator': op_token['value'],
                    'left': left, 'right': right}
                return self._parse_expression(ast, current_prec)

        return left


    def parse(self):
        return self._parse_expression(self._parse_num(), 0)

    def unexpected_token(self, expected_type, actual_token):
        self.token_stream.croak('Expected token of type: ' + expected_type +
            ', found token: ' + str(actual_token))
