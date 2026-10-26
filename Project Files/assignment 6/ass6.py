import ply.lex as lex
import ply.yacc as yacc

# ---------------- LEXER ----------------

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE'
)

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'

# Ignore spaces and tabs
t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Handle illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(1)


lexer = lex.lex()


# ---------------- PARSER ----------------

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


# Syntax error handler
def p_error(p):
    if p is None:
        print("Syntax error at EOF")
    else:
        print(f"Syntax error at '{p.value}'")


parser = yacc.yacc()


# ---------------- INPUT ----------------

while True:
    try:
        expression = input("input --> ")
    except EOFError:
        break

    if not expression:
        break

    result = parser.parse(expression, lexer=lexer)

    if result is not None:
        print("output -->", result)