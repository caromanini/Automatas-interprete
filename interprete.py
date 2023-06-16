import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'agregar' : 'ADD',
    'eliminar' : 'DELETE'
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
t_DELETE = r'eliminar'

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

    if(t[1] == 'agregar'):
        add(t[2])
    if(t[1] == 'eliminar'):
        delete(t[2])

def p_expr_num(t):
    's : INT'
    t[0] = t[1]

def p_expr_id(t):
    's : ID'
    try:
        t[0] = variables[t[1]]
    except LookupError:
        print("Variable indefinida '%s'" % t[1])
        t[0] = 0

def p_expr_string(t):
    '''s : STRING 
        | SSTRING'''
    t[0] = t[1][1:-1]

def p_agregar(t):
    '''s : ADD'''
    t[0] = 'agregar'


def p_eliminar(t):
    '''s : DELETE'''
    t[0] = 'eliminar'

def p_error(t):
    print("ERROR")

lexer = lex.lex()
parser = yacc.yacc()

personas = []
def add(nombre): 
    nombre = nombre.strip('"')

    aux = {
        "Nombre" : "",
        "Admiracion" : 0,
        "Amor" : 0,
        "Cariño" : 0,
        "Enojo" : 0,
        "Envidia" : 0,
        "Odio" : 0
    }

    aux["Nombre"] = nombre
    personas.append(aux)

def delete(nombre):
    nombre = nombre.strip('"')

    for i in personas:
        if(i['Nombre'] == nombre):
            personas.remove(i)

while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)
