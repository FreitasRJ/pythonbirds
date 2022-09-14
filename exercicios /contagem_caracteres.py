def contar_caracteres(s):
    '''Função que conta os caracteres de uma string
    
    Ex.:

    >>> conta_caracteres('renzo')
    e:1
    n:1
    o:1
    r:1
    z:1

    >>> conta_caracteres('banana')
    a:3
    b:1
    n:2

        parametros s: string a ser contada
    '''

    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    contador = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contador +=1
        else:
            print(f'{caracter_anterior}:{contador}')
            caracter_anterior = caracter
            contador = 1
    print(f'{caracter}:{contador}')

if __name__=='__main__':
    contar_caracteres('renzo')
    print()
    contar_caracteres('banana')


#contar_caracteres('caracter')


    