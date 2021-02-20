#ejercicio 4
def formato_numeros(numero):
    numero_cadena = str(numero)
    numero_caracteres = 3
    separador = ","
    contador = 0
    nuevo_formato = ""
    for letra in numero_cadena[::-1]:
        if contador == numero_caracteres:
            nuevo_formato += separador
            contador = 0
        contador += 1
        nuevo_formato += letra
    return(nuevo_formato[::-1])




print(formato_numeros(43214124))
    