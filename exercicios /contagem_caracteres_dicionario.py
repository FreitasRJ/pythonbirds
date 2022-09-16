def contar_caracteres(s):
    '''Função que conta os caracteres de uma string
    
    Ex.:

    >>> conta_caracteres('renzo')
    {'n': 1, 'e': 1, 'o': 1, 'r': 1, 'z': 1}

    >>> conta_caracteres('banana')
    {'a':3, 'b':1, 'n':2}

        parametros s: string a ser contada
    '''
    
    '''
    caracteres_ordenados = sorted(s)
    caracter_da_vez = caracteres_ordenados[0]
    contador = 1
    resultado = {}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_da_vez:
            contador += 1
        else:
            resultado[caracter_da_vez] = contador
            caracter_da_vez = caracter
            contador = 1
    resultado[caracter_da_vez] = contador

    return resultado

    if __name__== '__main__':
        print(resultado)
    '''

    resultado = {}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado

print(contar_caracteres('renzo'))
print(contar_caracteres('banana'))