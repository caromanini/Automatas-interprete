import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'agregar' : 'ADD',
    'eliminar' : 'DELETE',
    'actualizar' : 'UPDATE',
    'resumir' : 'RECAP'
}

tokens = [
    'INT',
    'ID',
    'STRING'
]+list(reserved.values())

t_ADD = r'agregar'
t_DELETE = r'eliminar'
t_UPDATE = r'actualizar'
t_RECAP = r'resumir'

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING(t):
    r'\"(\s*\w*\s*)*\"' 
    t.type = reserved.get(t.value, 'STRING')
    return t

t_ignore = ' \t'

def t_error(t):
    print(":(")
    t.lexer.skip(1)

variables = {}

def p_resultado(t):
    '''resultado : s STRING'''
    if(t[1] == 'agregar'):
        add(t[2])

    elif(t[1] == 'eliminar'):
        delete(t[2])

    elif(t[1] == 'actualizar'):
        update(t[2])

    elif (t[1] == 'resumir'):
        recap(t[2])


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
    '''s : STRING '''
    t[0] = t[1][1:-1]

def p_agregar(t):
    '''s : ADD'''
    t[0] = 'agregar'

def p_eliminar(t):
    '''s : DELETE'''
    t[0] = 'eliminar'

def p_update(t):
    '''s : UPDATE'''
    t[0] = 'actualizar'

def p_resumir(t):
    '''s : RECAP'''
    t[0] = 'resumir'

def p_error(t):
    print("\033[91mERROR: Comando invalido\033[0m")

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
    i = 0
    for element in personas:
        i += 1
        print(f"Persona {i} {element}\n")


def recap(nombre):
    internalcheck = False
    for element in personas:
        if (nombre == (f'"{element["Nombre"]}"')):
            archivo = open(element["Nombre"], "w")
            archivo.write(f"Nombre: {element['Nombre']} \n")
            archivo.write(f"Admiracion: {element['Admiracion']} \n")
            archivo.write(f"Amor: {element['Amor']} \n")
            archivo.write(f"Cariño: {element['Cariño']} \n")
            archivo.write(f"Enojo: {element['Enojo']} \n")
            archivo.write(f"Envidia: {element['Envidia']} \n")
            archivo.write(f"Odio: {element['Odio']} \n")
            archivo.close()
            internalcheck = True
            print(element)
        if internalcheck ==False:
            print("No se ha encontrado a una persona de ese nombre :()")
            print ("Existen las siguientes personas para elegir:")
            for element in personas:
                print(element["Nombre"])
    pass

def delete(nombre):
    nombre = nombre.strip('"')

    for i in personas:
        if(i['Nombre'] == nombre):
            personas.remove(i)
    print("PERSONAS: ", personas) #este print esta por mientras para ver la lista personas

def update(nombre):
    nombre = nombre.strip('"')

    found = False
    pos = 0
    for i in personas:
        if(i['Nombre'] == nombre):
                found = True
                break
        pos+=1

    if(found):
        print("Elegiste actualizar tu relacion con", nombre)
        respuesta = input("¿Cuál de los siguientes sentimientos deseas cambiar? (INGRESAR ENTRE COMILLAS) \n -Admiracion\n -Amor\n -Cariño\n -Enojo\n -Envidia\n -Odio\n")

        #Muchos de los prints estan por mientras para ir chequeando como funciona el codigo !!
        if(respuesta == "admiracion"):
            sentimiento = input("Ingresa el nivel de admiracion (0-100): ")
            if (sentimiento <= 100):
                personas[pos]['Admiracion'] = sentimiento
                print("ADMIRACION HACIA", nombre, "AHORA ESTA EN", sentimiento)
                print(personas[pos])   
            else:
                print ("¡Que bobito! Ese número es mayor que 100")        

        elif(respuesta == "amor"):
            sentimiento = input("Ingresa el nivel de amor (0-100): ")
            if (int(sentimiento) <= 100):
                personas[pos]['Amor'] = sentimiento
                print("AMOR HACIA", nombre, "AHORA ESTA EN", sentimiento)
                print(personas[pos])
            else:
                print ("¡Que bobito! Ese número es mayor que 100")

        elif(respuesta == "cariño"):
            sentimiento = input("Ingresa el nivel de cariño (0-100): ")
            if (int(sentimiento) <= 100):
                personas[pos]['Cariño'] = sentimiento
                print("CARIÑO HACIA", nombre, "AHORA ESTA EN", sentimiento)
                print(personas[pos])
            else:
                print ("¡Que bobito! Ese número es mayor que 100")

        elif(respuesta == "enojo"):
            sentimiento = input("Ingresa el nivel de enojo (0-100): ")
            if (int(sentimiento) <= 100):
                personas[pos]['Enojo'] = sentimiento
                print("ENOJO HACIA", nombre, "AHORA ESTA EN", sentimiento)
                print(personas[pos])
            else:
                print ("¡Que bobito! Ese número es mayor que 100")

        elif(respuesta == "envidia"):
            sentimiento = input("Ingresa el nivel de envidia (0-100): ")
            if (int(sentimiento) <= 100):
                personas[pos]['Envidia'] = sentimiento
                print("ENVIDIA HACIA", nombre, "AHORA ESTA EN", sentimiento)
                print(personas[pos])
            else:
                print ("¡Que bobito! Ese número es mayor que 100")

        elif(respuesta == "odio"):
            sentimiento = input("Ingresa el nivel de odio (0-100): ")
            if (int(sentimiento) <= 100):
                personas[pos]['Odio'] = sentimiento
                print("ODIO HACIA", nombre, "AHORA ESTA EN", sentimiento)
                print(personas[pos])
            else:
                print ("¡Que bobito! Ese número es mayor que 100")
    else:
        print("\033[91mERROR: Persona no existe\033[0m")

while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)
