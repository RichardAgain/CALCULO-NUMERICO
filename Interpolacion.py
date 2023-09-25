import numpy as np
from sympy import *
import matplotlib.pyplot as plt

x=Symbol("x")

#Funciones: 

def polinomioL(xi,fi):
    pol=0
    for i in range(len(xi)):
        num=1
        deno=1
        for j in range(len(xi)):
            if j != i:
                num*=(x-xi[j])
                deno*=(xi[i]-xi[j])
        terminoL=num/deno
        pol+=terminoL*fi[i] 
    return pol               

def valores(xi,fi):
    pol=polinomioL(xi,fi)
    pol_Simple=pol.expand()
    px=lambdify(x,pol_Simple)
    muestras=100
    a,b=min(xi),max(xi)
    pxi=np.linspace(a,b,muestras)
    pfi=px(pxi)
    return pxi, pfi, pol, pol_Simple

def grafica(xi,fi,pxi,pfi):
    plt.subplots(figsize=(15,8))
    plt.plot(xi,fi,"o",label="Puntos")
    plt.plot(pxi,pfi,label="Polinomio")
    plt.legend()
    plt.grid(1)
    plt.xlabel("xi")
    plt.ylabel("yi")
    plt.title("Interpolacion de Lagrange")
    plt.show()

#Asignaciones:

xi = np.array([0,3,5,7,8,10,14])
fi = np.array([3.67,8.33,21.97,19.33,15.10,14.31,13.74])

pxi,pfi,pol,pol_Simple=valores(xi,fi)

#Impresiones:

print("")
print("POLINOMIO EN X")
print(pxi)
print("")
print("POLINOMIO EN Y")
print(pfi)
print("")
print("POLINOMIO BASE")
print(pol)
print("")
print("POLINOMIO SIMPLIFICADO")
print(pol_Simple)
print("")
grafica(xi,fi,pxi,pfi)