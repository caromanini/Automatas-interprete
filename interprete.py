import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'agregar' : 'ADD'
}

tokens = [
    'INT',
    'ID',
    'STRING',
    'SSTRING'
]+list(reserved.values())

#Por cada token hay que tener una expresion regular que lo identifique 
#El diccionario reserved tambien son tokens

t_ADD = r'agregar'

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING(t):
    r'\"(\s*\w*\s*)*\"' #Esto identifica expresiones del tipo "cualquier cosa"
    t.type = reserved.get(t.value, 'STRING')
    return t

def t_SSTRING(t):
    r'\'(\s*\w*\s*)*\'' #Esto identifica expresiones del tipo 'cualquiercosa'
    t.type = reserved.get(t.value, 'SSTRING')
    return t

t_ignore = ' \t'

def t_error(t):
    print(":(")
    t.lexer.skip(1)

variables = {}

def p_resultado(t):
    '''resultado : s STRING
        | s SSTRING '''
    print("Esto es t[1] en p_resultado: ",t[1])

def p_expr_num(t):
    's : INT'
    t[0] = t[1]
    print("Esto es t[0] en p_expr_num: ", t[0])

def p_expr_id(t):
    's : ID'
    try:
        t[0] = variables[t[1]]
        print("Esto es t[0] en p_expr_id: ", t[0])
    except LookupError:
        print("Variable indefinida '%s'" % t[1])
        t[0] = 0

def p_expr_string(t):
    '''s : STRING 
        | SSTRING'''
    t[0] = t[1][1:-1]
    print("Esto es t[0] en p_expr_string: ",t[0])

def p_oper(t):
    '''s : ADD'''
    print("ESTO ES t[0] en p_oper: ",t[0])

def p_error(t):
    print("ERROR")

lexer = lex.lex()
parser = yacc.yacc()

while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)

#LexToken(INT,'3',1,0)
#LexToken(Tipo de Token, token ingresado, linea en la que se escribio, en que posicion esta)
