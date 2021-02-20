##
numero = 100
def largo_de_un_numero(n):
   # numero= int(input("Dame un numero"))
   contador = 1
   while(n /10 > 0):
        n = n/10
        contador = contador + 1
        return(contador)

print(largo_de_un_numero(numero))