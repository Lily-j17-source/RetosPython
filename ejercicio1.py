##
numero = 10000
def largo_de_un_numero(n):
    i = n
    contador = 1
    while (i/10 > 0):
        contador += 1
        rest = n/10
        i = rest
    return contador
  # contador = 0
   #while( n/10 > 0):
    #   contador += 1
     #  n = n/10
      # return contador



print(largo_de_un_numero(numero))