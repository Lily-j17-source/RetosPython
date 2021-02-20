##
numero = 10000
def largo_de_un_numero(n):
   contador = 0
   while( n/10 > 0):
       contador += 1
       n = n/10
       return contador



print(largo_de_un_numero(numero))