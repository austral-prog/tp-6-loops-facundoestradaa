# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """

    resultado = []
    for conjunto in matrix:
        for elemento in conjunto:
            resultado = resultado + [elemento]

    return resultado



def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    resultado = []


    for conjunto in matrix:
        suma = 0
        for elemento in conjunto:
            suma += elemento
        resultado = resultado + [suma]
    return resultado



def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    resultado = []
    columnas = len(matrix[0])

    for i in range(columnas):
        suma = 0
        for conjunto in matrix:
            suma += conjunto[i]
        resultado = resultado + [suma]
    return resultado
