##
numero = 89635

def largo_de_un_numero(n):
    if(isinstance(n,int)):
        contador = 0
        numero_cadena = str(n)
        while numero_cadena[contador:]:
          contador += 1
        return contador
    else:
        return"no el el tipo de dato correcto"


print(largo_de_un_numero(numero))