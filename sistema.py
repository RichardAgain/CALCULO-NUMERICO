import random
import copy
import numpy as np
import time
from fractions import Fraction

def random_(a, b):
    # Retorna un numero entero entre a y b incluidos a y b
    return random.randint(a, b)


def vector_por_escalar(vector, escalar):
    # Retorna el vector multiplicado por el escalar dado
    vector_escalado = copy.deepcopy(vector)
    for i in range(len(vector_escalado)):
        vector_escalado[i] *= escalar
    return vector_escalado

def matriz_random(filas, columnas):
    # Retorna una matriz de numeros enteros aleatorios de entre 0 y 99, con la cantidad de filas y columnas dadas
    matriz = [[0]*columnas for i in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = random_(-9,9)
    return matriz


def suma_matricial(matriz1, matriz2):
    # Retorla la matriz resultante de la suma de 2 matrices dadas
    try:
        cantidadDeFilas1 = len(matriz1)
        cantidadDeColumnas1 = len(matriz1[0])
        cantidadDeFilas2 = len(matriz2)
        cantidadDeColumnas2 = len(matriz2[0])
        if validar_matriz(matriz1) and validar_matriz(matriz2) and cantidadDeFilas1 == cantidadDeFilas2 and cantidadDeColumnas1 == cantidadDeColumnas2:
            matriz = [[0] * cantidadDeColumnas1 for i in range(cantidadDeFilas1)]
            for i in range(len(matriz1)):
                for j in range(len(matriz1[0])):
                    matriz[i][j] = matriz1[i][j] + matriz2[i][j]
            return matriz
        else:
            raise IndexError("Las dos matrices deben tener las mismas dimensiones")
    except:
        if len(matriz1) == len(matriz2):
            matriz = [0]*len(matriz1)
            for i in range(len(matriz1)):
                matriz[i] = matriz1[i] + matriz2[i]
        return matriz
    

def print_array(array):
    # Imprime un array en forma ordenada
    try:
        array[0][0]
        for fila in array:
            print(fila)
    except:
        print(array)


def producto_punto(vector1, vector2):
    # Retorna el número resulatante del producto punto/escalar de dos vectores fila
    len1 = len(vector1)
    len2 = len(vector2)
    if len1 == len2:
        vector = 0
        for i in range(len1):
            vector += vector1[i]*vector2[i]
        return vector
    else:
        raise IndexError("Entrada invalida. Se deben introducir dos vectores fila de la misma longitud")


def validar_matriz(matriz):
    # Retorna True si m es una matriz (si el arreglo es rectangular), de lo contrario retorna False
    try:
        cantidadDeColumnas = len(matriz[0])
        cantidadDeFilas = len(matriz)
        for fila in range(1, cantidadDeFilas):
            if cantidadDeColumnas != len(matriz[fila]):
                return False
        return True
    except:
        return False


def columna_de_matriz(matriz, columna):
    #Retorna un vector columna que corresponde a la j-ésima columna de una matriz
    if validar_matriz(matriz):
        vectorColumna = [[0] for i in range(len(matriz))]
        componente = 0
        for fila in matriz:
            vectorColumna[componente][0] = fila[columna]
            componente += 1
        return vectorColumna
    else:
        raise ValueError("Entrada invalida. Se debe introducir una matriz y una columna de esa matriz")
    

def producto_matricial2(matriz1, matriz2):
    # Retorna la matriz resultante del producto de dos matrices
    if validar_matriz(matriz1) and validar_matriz(matriz2) and len(matriz1[0]) == len(matriz2):
        cantidadDeFilas1 = len(matriz1)
        cantidadDeColumnas2 = len(matriz2[0])
        cantidadComun = len(matriz2)
        matriz = [[0]*cantidadDeColumnas2 for fila in range(cantidadDeFilas1)]
        for i in range(cantidadDeFilas1):
            for j in range(cantidadDeColumnas2):
                for k in range(cantidadComun):
                    matriz[i][j] += matriz1[i][k] * matriz2[k][j] 
        return matriz


def norma1(vector, norma = 0):
    # Retorna la norma o modulo de un vector
    for componente in vector:
        norma += componente*componente
    return norma**(0.5)


def norma2(vector, n = 0):
    # Retorna la norma o modulo de un vector, usando el producto punto
    return (producto_punto(vector, vector))**0.5


def matriz_transpuesta(matriz):
    # Retorna la matriz transpuesta de una matriz dada
    if not validar_matriz(matriz):
        raise ValueError("Debe introducir una matriz para retornar su transpuesta")
    cant_filas_matriz = len(matriz)
    cant_columnas_matriz = len(matriz[0])
    cant_filas_transpuesta = cant_columnas_matriz
    cant_columnas_transpuesta = cant_filas_matriz
    matriz_transpuesta = [[0] * cant_columnas_transpuesta for filas in range(cant_filas_transpuesta)]
    for i in range(cant_filas_matriz):
        for j in range(cant_columnas_matriz):
            matriz_transpuesta[j][i] = matriz[i][j]
    return matriz_transpuesta
        

def matriz_menor(matriz, fila, columna):
    # Retorna el menor de una matriz, es decir una matriz igual con la fila y columnas dadas eliminadas
    if validar_matriz(matriz):
        matriz_menor = copy.deepcopy(matriz)
        matriz_menor.pop(fila)
        for i in range(len(matriz_menor)):
            del matriz_menor[i][columna]
        return matriz_menor


def det_cofactores(matriz):
    # Calcula el determinante de una matriz dada por el metodo de los cofactores, no se recomienda para matrices de orden 9 o superior
    if validar_matriz(matriz) and len(matriz) == len(matriz[0]):
        determinante = 0
        for j in range(len(matriz[0])):
            if len(matriz[0]) != 1:
                determinante += (-1)**(j) * matriz[0][j] * det_cofactores(matriz_menor(matriz, 0, j))
            else:
                return matriz[0][0]
        return determinante
    else:
        raise ValueError("Solo se puede calcular el determinante de matrices cuadradas")
    
    
def matriz_intercambiar_filas(matriz, fila_a, fila_b):
    # Retorna la matriz con las filas dadas intercambiadas
    matriz_cambiada = copy.deepcopy(matriz)
    fila_temporal = matriz_cambiada[fila_a]
    matriz_cambiada[fila_a] = matriz_cambiada[fila_b]
    matriz_cambiada[fila_b] = fila_temporal
    return matriz_cambiada

def ceros_diagonal_principal(matriz, fila_columna):
    # Retorna True si en y debajo de fila_columna dada hay puros ceros, de lo contrario retorna False
    for i in range(len(matriz) - fila_columna):
        if matriz[i+fila_columna][fila_columna] == 0:
            continue
        else:
            return False
    return True

def matriz_gaussiana(matriz):
    # Transforma una matriz cuadrada en una matriz triangular superior
    if not (validar_matriz(matriz) and len(matriz) == len(matriz[0])):
        raise ValueError("Solo se puede aplicar la reduccion gaussiana a matrices cuadradas")
    else:
        matriz_gauss = copy.deepcopy(matriz)
        signo = 1
        factor = 1
        for j in range(len(matriz_gauss[0]) - 1):
            if ceros_diagonal_principal(matriz_gauss, j):
                continue
            for fila in range(j, len(matriz_gauss)):
                if matriz_gauss[fila][j] != 0:
                    pivote = matriz_gauss[fila][j]
                    if fila != j:
                        signo *= -1
                    break
                fila += 1
            if fila != j:
                matriz_gauss = matriz_intercambiar_filas(matriz_gauss, j, fila)
            matriz_gauss[j] = vector_por_escalar(matriz_gauss[j], Fraction(1, pivote))
            factor *= pivote
            for i in range(j + 1, len(matriz_gauss)):
                matriz_gauss[i] = suma_matricial(matriz_gauss[i], vector_por_escalar(matriz_gauss[j], -matriz_gauss[i][j]))
        matriz_gauss[0] = vector_por_escalar(matriz_gauss[0], signo * factor)
        return matriz_gauss


def producto_diagonal_principal(matriz):
    # Retorna el producto de los elementos de la diagonal principal de una matriz cuadrada
    producto = 1
    for i in range(len(matriz)):
        producto *= matriz[i][i]
    return producto


def det_gaussiano(matriz):
    # Retorna el determinante de una matriz, transformando primero la matriz en una 
    # matriz triangular superior y luego multiplicando los elementos de la diagonal principal
    matriz_gauss = copy.deepcopy(matriz_gaussiana(matriz))
    return producto_diagonal_principal(matriz_gauss)


def print_matriz_con_fraccciones(matriz):
    # Imprime ordenadamente una matriz, con sus elementos en forma de fraccion
    for i in range(len(matriz)):
        print("[", end="")
        for j in range(len(matriz[0])):
            if j != len(matriz[0]) - 1:
                print(matriz[i][j], end=",  ")
            else:
                print(matriz[i][j], end="]")
        print()


def print_vector_con_fraccciones(vector):
    # Imprime ordenadamente una matriz, con sus elementos en forma de fraccion
    print("[", end="")
    for i in range(len(vector)):
        if i != len(vector) - 1:
            print(vector[i], end=",  ")
        else:
            print(vector[i], end="]")


def ampliar_matriz(matriz, vector):
    # Retorna la matriz ampliada con el vector dado, el vector se coloca como vector columna a la derecha
    if not (validar_matriz(matriz) and len(matriz) == len(matriz[0]) == len(vector)):
        raise ValueError("Solo se puede hacer la ampliacion con matrices cuadradas y vectores de la misma longitud")
    else:
        matriz1 = matriz
        vector1 = vector
        for i in range(len(matriz)):
            matriz1[i] += [vector1[i]]
        return matriz1
    

def gauss_jordan(matriz, vector_de_constantes):
# Retorna el vector solucion del sistema de ecuaciones, usando el metodo de gauss_jordan.
# Si el sistema no tiene solucion (es incompatible) retorna False, y si tiene infinitas solucions (es compatible indeterminado) retorna True
        if not (validar_matriz(matriz) and len(matriz) == len(matriz[0]) == len(vector_de_constantes)):
            raise ValueError("Solo se puede aplicar este metodo de gauss_jordan a matrices cuadradas")
        else:
            matriz_ampliada = ampliar_matriz(matriz, vector_de_constantes)
            vector_solucion = [0]*len(vector_de_constantes)
            compatible_determinado = True
            for j in range(len(matriz_ampliada[0]) - 1):
                if ceros_diagonal_principal(matriz_ampliada, j):
                    continue
                for fila in range(j, len(matriz_ampliada)):
                    if matriz_ampliada[fila][j] != 0:
                        pivote = matriz_ampliada[fila][j]
                        matriz_ampliada = matriz_intercambiar_filas(matriz_ampliada, j, fila)
                        matriz_ampliada[j] = vector_por_escalar(matriz_ampliada[j], Fraction(1, pivote))
                        break
                for i in range(0, len(matriz_ampliada)):
                    if i != j:
                        matriz_ampliada[i] = suma_matricial(matriz_ampliada[i], vector_por_escalar(matriz_ampliada[j], -matriz_ampliada[i][j]))
            for k in range(len(matriz_ampliada)):
                if matriz_ampliada[k][k] == 0:
                    compatible_determinado = False
                    if matriz_ampliada[k][len(matriz_ampliada)] != 0:
                        return False   # El sistema no tiene solucion, es incompatible
                    else:
                        continue
            if not compatible_determinado:
                return True # El sistema tiene infinitas soluciones
            for n in range(len(matriz_ampliada)):
                vector_solucion[n] = matriz_ampliada[n][len(matriz_ampliada)]
            return vector_solucion

print(matriz_random(3,3))

print(gauss_jordan(matriz_random(3,3), [1,2,3]))

