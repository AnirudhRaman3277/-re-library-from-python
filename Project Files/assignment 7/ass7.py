import ply.lex as lex
import ply.yacc as yacc

tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE')

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_expression_val(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_op(p):
    '''expression : expression expression PLUS
                  | expression expression MINUS
                  | expression expression TIMES
                  | expression expression DIVIDE'''
    if p[3] == '+':
        p[0] = p[1] + p[2]
    elif p[3] == '-':
        p[0] = p[1] - p[2]
    elif p[3] == '*':
        p[0] = p[1] * p[2]
    elif p[3] == '/':
        if p[2] == 0:
            print("Error: Division by zero!")
            p[0] = None
        else:
            p[0] = p[1] / p[2]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")

parser = yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            s = input('postfix > ')
        except EOFError:
            break
        if s.strip().lower() == 'exit':
            break
        if not s.strip():
            continue
            
        result = parser.parse(s)
        if result is not None:
            print(f"Result: {result}")
