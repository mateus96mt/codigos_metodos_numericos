#repositorio git: https://github.com/mateus96mt/codigos_metodos_numericos.git
import numpy as np

#codigo para resolver sistemas tridiagonais
def TDMAsolver(a, b, c, d):
    nf = len(d)
    ac, bc, cc, dc = map(np.array, (a, b, c, d))
    for it in range(1, nf):
        mc = ac[it-1]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1] 
        dc[it] = dc[it] - mc*dc[it-1]
        	    
    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for il in range(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    return xc

def spline_integral(a, b, c, d, x, j, n):    
    integral = lambda z: a[j]*z + (b[j]*(z - x[j])**2)/2 + (c[j]*(z - x[j])**3)/3 + (d[j]*(z - x[j])**4)/4
    return integral(x[j+1])-integral(x[j])

pontos = np.array([[1,3.0],[2,3.7],[5,3.9],[6,4.2],[7,5.7],
                   [8,6.6],[10,7.1],[13,6.7],[17,4.5],[20,7.0],
                   [23,6.1],[24,5.6],[25,5.8],[27,5.2],[27.7,4.1],
                   [28,4.3],[29,4.1],[30,3.0]])

n = len(pontos)
x = pontos[:,0]
y = pontos[:,1]
h = [ x[j+1]-x[j] for j in range(n-1) ]

#constantes a_j:
a = [ y[j] for j in range(len(y)) ]

#constante c_j obtida resolvendo o sistema linear tridiagonal:
f = [ ( (3*(a[j+1]-a[j])/(h[j])) + (3*(a[j-1]-a[j])/(h[j-1])) ) for j in range(1, n-1)]
diag_inf = [h[j-1] for j in range(2, n-1)]
diag_princ = [2*(h[j]+h[j-1]) for j in range(1, n-1)]
diag_sup = [h[j] for j in range(1, n-2)]
c = np.zeros(len(x))
c [1:-1] = TDMAsolver(diag_inf, diag_princ, diag_sup, f)

#constante bj e dj
b = np.zeros(len(x))
b[1:-1] = [ (a[j+1]-a[j])/(h[j]) - (h[j]*(2*c[j]+c[j+1]))/3 for j in range(1, n-1) ]
d = np.zeros(len(x))
d[1:-1] = [ (c[j+1]-c[j])/(3*h[j]) for j in range(1, n-1)]

#condicao de contorno derivada segunda de S = 0, nos pontos x0 e xn
d[0] = c[0] = 0
d[-1] = c[-1] = b[-1] = 0
b[0] = 0.7

result = 0
for i in range(n-1):
    result = result + spline_integral(a,b,c,d,x,i,n)

result = result - (x[-1]-x[0])*3
print(result)