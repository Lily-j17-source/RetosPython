#ejercicio 3
def factorial(n):
    resultado = 1
    i = 2
    while i <= n:
        resultado *= i
        i +=1
    return resultado


print(factorial(4))