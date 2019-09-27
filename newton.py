#repositorio git: https://github.com/mateus96mt/codigos_metodos_numericos.git
import numpy as np

#método de newton na forma vetorial
def newton(x_0, J_, F, tol):
    i=0
    x_k = x_0
    x_k1 = x_0
    #np.linalg.norm(F(x_k1)) calcula a norma de F(x) aproximado
    while(np.linalg.norm(F(x_k1))>tol and i<10000):#maximo de 100 interacoes
        J1 = np.linalg.inv(J_(x_k))#jacobiana inversa
        x_k1 = x_k -np.dot(J1, F(x_k))
        x_k = x_k1
        i = i + 1
    return [x_k1, i, F(x_k1)]

#matriz jacobiana aproximada
def secante(x_0, F):
    x_k = x_0
    x_k1 = np.zeros(len(x_0))
    for i in range(100):
        J = np.zeros(1)
        x_k1 = x_k -np.dot(J, F(x_k))
        x_k = x_k1
    return x_k1

#funcao exercicio 1
def F1(x):
    return np.array([x[0]**2+x[1]**2+x[2]**2-1,
                     2*x[0]**2+x[1]**2-4*x[2]**2-1,
                     3*x[0]**2-4*x[1]**2+x[2]**2-1])
#jacobiana exercicio 1
def J1(x):
    return np.array([[2*x[0], 2*x[1], 2*x[2]],
                     [4*x[0], 2*x[1], -8*x[2]],
                     [6*x[0], -8*x[1], 2*x[2]]])
#funcao exercicio 2    
def F2(x):
    return np.array([x[0]+x[1]**2-x[1]*x[2]-0.1,
                     x[1]-x[1]**2+3*x[0]*x[2]+0.2,
                     x[2]+x[2]**2+2*x[0]*x[2]-0.3])
#jacobiana exercicio 2    
def J2(x):
    return np.array([[1, 0, -x[1]],
                     [0, -2*x[1], 3*x[0]],
                     [0, 0, 2*x[0]]])
#funcao exercicio 3    
def F3(x):
    return np.array([10*x[0]-2*x[1]**2+x[1]-2*x[2]-5,
                     8*x[1]**2+4*x[2]**2-9,
                     8*x[1]*x[2]+4])
#jacobiana exercicio 3
def J3(x):
    return np.array([[10, -4*x[1]+1, -2],
                     [0, 16*x[1], 8*x[2]],
                     [0, 8*x[2], 8*x[1]]])
def F4(x):
    return np.array([x[0]**2+x[1]-37,
                     x[0]-x[1]**2-5,
                     x[0]+x[1]+x[2]-3])

def J4(x):
    return np.array([[2*x[0],1,0],
                     [1,-2*x[1],0],
                     [1,1,1]])    

def F5(x):
    return np.array([x[0]**2+2*x[1]**2-x[1]-2*x[2],
                     x[0]**2-8*x[1]**2+10*x[2],
                     (x[0]**2)/(7*x[1]*x[2])-1])
def J5(x):
    return np.array([[2*x[0], 4*x[1]-1, -2],
                     [2*x[0], -16*x[1], 10],
                    [(2*x[0])/(7*x[1]*x[2]),
                     -(x[0]**2)/(7*(x[1]**2)*x[2]), 
                     -(x[0]**2)/(7*x[1]*(x[2]**2))]])
def F6(x):
    return np.array([3*x[0]-np.cos(x[1]*x[2])-1/2,
                     x[0]**2-81*(x[1]+0.1)**2+np.sen(x[2]+1.06),
                     np.exp(-x[0]*x[1])+20*x[2]+(10*np.pi-3)/3])

def J6(x):
    return np.array([[3, np.sin(x[1]*x[2])*x[2], np.sin(x[1]*x[2])*x[1]],
                     [2*x[0], -192*(x[1]+0.1), np.cos(x[2])],
                     [-np.exp(-x[0]*x[1]),0, 20]])    
    
def F7(x):
    return np.array([x[0]+np.cos(x[0]*x[1]*x[2])-1,
                     (1-x[0]**(1/4)+0.05*x[2]**2-0.15*x[2]-1),
                     -x[0]**2-0.1*x[1]**2+0.01*x[1]+x[2]-1])

def J7(x):
    return np.array([[1-np.sin(x[0]*x[1]*x[2])*x[0]*x[2],
                      -np.sin(x[0]*x[1]*x[2])*x[1]*x[2],
                      -np.sin(x[0]*x[1]*x[2])*x[0]*x[1]],
                     [(1/4)*(1-x[0])**(-3/4), 1, 0.1*x[2]-0.15],
                     [-2*x[0],-0.2*x[1]+0.01,1]]) 
    
def F8(x):
    return np.array([x[0]+10*x[1],
                     np.sqrt(5)*(x[2]-x[3]),
                     (x[1]-x[2])**2,
                     np.sqrt(10)*(x[0]-x[3])**2])

def J8(x):
    return np.array([[1, 10, 0, 0],
                     [0, 0, np.sqrt(5), np.sqrt(5)],
                     [0, 2*x[1], 2*x[2], 0],
                     [2*np.sqrt(10)*x[0], 0, 0, 2*np.sqrt(10)*x[3]]])
    
def F9(x):
    return np.array([x[0]+x[1] -2,
                     x[0]*x[2]+x[1]*x[3],
                     x[0]*(x[2]**2)+x[1]*(x[3]**2) - 2/3,
                     x[0]*(x[2]**3)+x[1]*(x[3]**3)])

def J9(x):
    return np.array([[1, 1, 0, 0],
                     [x[2], x[3], x[0], x[1]],
                     [2*x[2], 2*x[3], 2*x[0], 2*x[1]],
                     [3*x[2], 3*x[3], 3*x[0], 3*x[1]]])
    
def F10(x):
    return np.array([4*x[0]-x[1]+x[2]-x[0]*x[3],
                     -x[0]+3*x[1]-2*x[2]-x[1]*x[3],
                     x[0]-2*x[1]+3*x[2]-x[2]*x[3],
                     x[0]**2+x[1]**2+x[2]])
    
def J10(x):
    return np.array([[4-x[3], -1, 1, -x[0]],
                     [-1, 3-x[3],-2,-x[1]],
                     [1,-2,3-x[3],-x[2]],
                     [2*x[0],2*x[1],2*x[3],0]])    
    
#funcoes    
F = [lambda x:F1(x), lambda x:F2(x), lambda x:F3(x), lambda x:F4(x), lambda x:F5(x),
     lambda x:F7(x), lambda x:F7(x), lambda x:F8(x), lambda x:F9(x), lambda x:F10(x)]
#jacobianos
J = [lambda x:J1(x), lambda x:J2(x), lambda x:J3(x), lambda x:J4(x), lambda x:J5(x),
     lambda x:J7(x), lambda x:J7(x), lambda x:J8(x), lambda x:J9(x), lambda x:J10(x)]

tol = 1e-10#tolerancia
x0 = [1,2,1]#solucao inicial escolhido para os exercicios de 1 à 4
for i in range(4):
    x = newton(x0, J[i], F[i], tol)
    print("\nEXERCÍCIO ", i+1, "\nx: ", x[0], "\nit: ", x[1], "\nF(x):", x[2], "\nponto de partida: ", x0)