#Ejercicio2
def devuelve_lista(numero1, longitud):
    if(isinstance(numero1,int)):
        if(isinstance(longitud,int)):
            listaMultiplos =[]
            multiplo=numero1
            for i in range(longitud):
                multiplo += numero1 * i
                listaMultiplos.append(multiplo)
            return listaMultiplos
        


print(devuelve_lista(8,5))
