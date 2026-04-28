# Replace the "ANSWER HERE" for your answer
from sys import base_exec_prefix


def power(base, exp):
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """

    if exp == 0:
        return 1

    else:
        resultado =1
        for i in range(exp):
            resultado = resultado*base
            print(resultado)
    return resultado


def sum_of_powers(base, max_exp):
    """
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """

    total = 0
    for expo in range(0, max_exp+1):
        valor = power(base, expo)
        total = total + valor
        print(total)
    return total
