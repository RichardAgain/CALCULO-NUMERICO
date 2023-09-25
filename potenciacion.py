import numpy as np

def metodo_potencias(A, num_simulations: int):
    n, d = A.shape

    if n != d:
        raise ValueError("La matriz debe ser cuadrada.")

    # Inicializamos el vector propio con valores aleatorios
    x = np.random.rand(n)

    for _ in range(num_simulations):
        # Multiplicamos A y x
        x = np.dot(A, x)
        # Normalizamos el vector propio
        x = x / np.linalg.norm(x)

    # El valor propio dominante es el producto punto de Ax y x
    valor_propio = np.dot(np.dot(A, x), x)

    return valor_propio, x

def main(matriz):
    # Definimos una matriz de ejemplo
    A = np.array(matriz)

    # Ejecutamos el método de las potencias
    valor_propio, vector_propio = metodo_potencias(A, num_simulations=100)

    # Redondeamos el valor propio y el vector propio a 2 decimales
    valor_propio = round(valor_propio, 2)
    vector_propio = np.round(vector_propio, 2)


    print(f"El valor propio dominante es: {valor_propio}")
    print(f"El vector propio correspondiente es: {vector_propio}")

    return(valor_propio, vector_propio)
