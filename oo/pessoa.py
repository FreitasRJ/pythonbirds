

class Pessoa:
    olhos = 2 # atributo de classe (fora da __init__). Utilizado para valores que seram sempre os mesmos.

    def __int__(self, *filhos, nome, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    
    def cumprimentar(self):
        return f'Olá  {id(self)}'

    @staticmethod # Decorate.
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls): # usa-se cls no lugar da palavra class e refere-se ao nome da classe
        return f'{cls} - olhos {cls.olhos}'

renzo = Pessoa()
luciano = Pessoa()
renzo.nome = "Renzo"
luciano.nome = "Luciano"
print(renzo.nome)
a =  renzo
print(renzo.__dict__) # mostra as estancias da classe contantes em def __init__
print(renzo.olhos)
Pessoa.olhos = 3
print(renzo.olhos)
print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
print(Pessoa.nome_e_atributos_de_classes(), luciano.nome_e_atributos_de_classes())







