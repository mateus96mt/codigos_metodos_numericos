#repositorio git: https://github.com/mateus96mt/codigos_metodos_numericos.git
import math as mp 

#exponencial por somatório sem alteracao
def e1(x, n):
    result = 0;
    for i in range(n):
        result = result + (x**i)/(mp.factorial(i))
    return result

def e2(x, n):
    positivo = 0
    negativo = 0
    
    for i in range(n):
        if i%2==0:
            positivo = positivo + (x**i)/(mp.factorial(i))
        else:
            negativo = negativo + (x**i)/(mp.factorial(i))
    
    return positivo + negativo

x = [-1, -5, -10, -20]

print("x exato aprox1 aprox2 erro1 erro2")
for i in x:
    exato = mp.exp(i)
    aprox1 = e1(i, 100)
    aprox2 = e2(i, 100)
    print(i, exato, aprox1, aprox2, abs(exato - aprox1), abs(exato - aprox2), "\n")