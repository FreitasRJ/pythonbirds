'''
    Você deve criar uma classe carro  que vai possuir dois atributos
compostos por outras duas classes:

1 -  Motor  
2 -  Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1 - Atributo de dado velocidade
2 - Método acelerar,. que deverá incrementar a velocidade de uma unidade
3 - Método frear que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de contraolar a direção. Ela oferece os 
seguintes atributos:

1 - Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2 - Método girar a direita,
3 - Método girar a esquerda.

  N
O   L
  S


Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

'''
class Carro:

    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade
    
    def calcular_direcao(self):
        return self.direcao.valor


    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()


class Motor:
    def __init__(self):
        self.velocidade = 0    

    def acelerar(self):
        self.velocidade += 1 
       

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0
       

class Direcao:
    
    def __init__(self):
        self.valor = 'Norte'
        self.chave = 1
        
    def girar_a_direita(self):
        rumo = {1:'Norte', 2:'Leste', 3:'Sul', 4:'Oeste'}
        self.chave +=1
        if self.chave > 4:
            self.chave = 1
        self.valor = rumo[self.chave]

    def girar_a_esquerda(self):
        rumo = {1:'Norte', 2:'Leste', 3:'Sul', 4:'Oeste'}
        self.chave -=1
        if self.chave < 1:
            self.chave = 4
        self.valor = rumo[self.chave]
        

# Teste
car = Carro(Direcao(),Motor())

while True:

    print(f'Direção: {car.calcular_direcao():<5}  -  Velocidade: {car.calcular_velocidade():>3}    ', end="")
    acao = input()

    if acao == '4':
        car.direcao.girar_a_esquerda()            
    elif acao == '6':
        car.direcao.girar_a_direita()
    elif acao == ' ':
        car.motor.acelerar()            
    elif acao == '0':
        car.motor.frear()


