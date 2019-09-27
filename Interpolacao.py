#repositorio git: https://github.com/mateus96mt/codigos_metodos_numericos.git
import numpy as np
import matplotlib.pyplot as plt

def L(i, x, pontos):
    n = len(pontos)
    result = 1
    for j in range(n):
        if i!=j:
            x_j = pontos[j, 0]
            x_i = pontos[i, 0]
            result = result * (x - x_j)/(x_i - x_j)
    
    return result

def polinomioLagrange(x, pontos):
    n = len(pontos)
    result = 0
    for i in range(n):
        y_i = pontos[i, 1]
        L_i = L(i, x, pontos)
        result = result + y_i*L_i
        
    return result

pontos = np.array([[1,3.0],[2,3.7],[5,3.9],[6,4.2],[7,5.7],
                   [8,6.6],[10,7.1],[13,6.7],[17,4.5],[20,7.0],
                   [23,6.1],[24,5.6],[25,5.8],[27,5.2],[27.7,4.1],
                   [28,4.3],[29,4.1],[30,3.0]])

#plota os pontos
plt.figure(figsize=[18,4])
plt.xlabel("x", size=15)
plt.ylabel("f(x)", size=15)
plt.grid(which='both')
plt.plot(pontos[:,0], pontos[:,1], 'o', color="black")
plt.ylim(0, 8)

#um polinomio de lagrange a cada n pontos
n = 4
m = list(range(0, len(pontos)-1, n))
pontos = np.split(pontos, m[1:])
p_ = pontos[0][0,0]
for i in range(len(pontos)):
    p = pontos[i]
    x = np.linspace(p_, p[-1,0], 200)
    p_ = x[-1]
    y = [polinomioLagrange(x_i, pontos[i]) for x_i in x]
    plt.plot(x, y, color="black")

plt.tight_layout()
plt.savefig("resultado" + str(n) + ".png", dpi=100)
