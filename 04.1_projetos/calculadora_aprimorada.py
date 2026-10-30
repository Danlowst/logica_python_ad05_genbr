def somarmultiplosnumeros(numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    return resultado

def multiplicarmultiplosnumeros(numeros):
    resultado = 1
    for i in numeros:
        resultado *= i
    return resultado

def ehpar(numero):
    return numero % 2 == 0


def ehinteiro(numero):
    return type(numero) is int
