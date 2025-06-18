####################
#CONSTANTS
####################
DIGITS = '0123456789'


####################
#Position
####################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1
        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)


####################
#Errors
####################


class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        result += f'File: {self.pos_start.fn}, Line: {self.pos_start.ln + 1}, Column: {self.pos_start.col + 1}\n'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)


####################
#Token
####################

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}, {self.value}'
        return f'Token({self.type})'


####################
#Lexer
####################


class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_token(self):
        token = []
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            if self.current_char in DIGITS:
                token.append(self.make_number())
            elif self.current_char == '+':
                token.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                token.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                token.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                token.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                token.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                token.append(Token(TT_RPAREN))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")
        return token, None


    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break #error
                dot_count += 1
                num_str += self.current_char
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))


####################
#NODES
####################
#NumberNode used to store numbers (ints and floats) for the parse tree
class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'

#BinaryOpertionNode used to store binary ops like 1+2
class BinaryOperationNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node} {self.op_tok} {self.right_node})'



####################
#PARSER
####################

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = 1
        self.advance()

    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]
        return self.current_token

    def parse(self):
        res = self.expression()
        return res

    def factor(self):
        tok = self.current_token
        if tok.type in (TT_INT, TT_FLOAT):
            self.advance()
            return NumberNode(tok)

    def term(self):
        return self.binary_op(self.factor, (TT_DIV, TT_MUL))

    def expression(self):
        return self.binary_op(self.term, (TT_PLUS, TT_MINUS))

    def binary_op(self, func, ops):
        left = func()
        while self.current_token.type in ops:
            op_token = self.current_token
            self.advance()
            right = func()
            left = BinaryOperationNode(left, op_token, right)
        return left
####################
#Run
####################
def run(fn, text):
    #Generate Tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_token()
    if error: return None, error

    #Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    return ast, None