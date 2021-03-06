from sly import Lexer


class SundanaseLexer(Lexer):
    tokens = {NAME, NUMBER, FLOAT, STRING, IF, THEN, ELSE,
              FOR, TO, ARROW, EQEQ, NTEQ, GTEQ, LTEQ, FUN, PRINT, ERROR}
    ignore = ' \t '
    literals = {'=', '+', '-', '/', '*',
                '(', ')', ',', ';', '^', '%', '<', ">"}

    # Tokens
    IF = r'UPAMI'
    THEN = r'TERAS'
    ELSE = r'HENTEU'
    FOR = r'KAHATUR'
    TO = r'KANGGO'
    FUN = r'FUN'
    ARROW = r'->'
    EQEQ = r'=='
    NTEQ = r'!='
    GTEQ = r'>='
    LTEQ = r'<='
    PRINT = r'PRINT'
    ERROR = r'LEPAT'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    # Define Number Tokens
    @_(r'\d+[.]+\d*')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Define Comment Token
    @_(r'#.*')
    def COMMENT(self, t):
        pass

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')

    # Define Error
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


if __name__ == '__main__':
    lexer = SundanaseLexer()
    env = {}
    while True:
        try:
            text = input('Sundanase > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
