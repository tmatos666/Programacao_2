#Ex1
"""class Person:
    def __init__(self, nome, idade, altura, peso=60):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    def printdados(self):
        print("O meu nome é ", self.nome, " tenho ", self.idade, \
        " e tenho ", self.altura, " e peso ", self.peso)

p1 = Person("Telmo", 40, 178)
p1.printdados()
p2 = Person("Teresa", 20, 158, 45)
p2.printdados()
"""

#Ex2
"""class Carro:
    def __init__(self, marca, cilindrada, numeroPortas, potencia):
        self.marca = marca
        self.cilindrada = cilindrada
        self.numeroPortas = numeroPortas
        self.potencia = potencia
    def printdados(self):
        print("O meu carro é um ", self.marca, " tem ", self.cilindrada, \
        "de cilindrada, tem ", self.numeroPortas, " e como potência tem ", self.potencia)

p1 = Carro("Mazda", 2000, 4, 120)
p1.printdados()
p2 = Carro("BMW", 2000, 2, 150)
p2.printdados()
"""

#Ex3
"""class Person:
    def __init__(self, nome, idade, altura, peso=60):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    def printdados(self):
        print("O meu nome é ", self.nome, " tenho ", self.idade, \
        " e tenho ", self.altura, " e peso ", self.peso)
    def falar(self):
        print("bla.. bla.. bla..")

p1 = Person("Telmo", 40, 178)
p1.printdados()
p1.falar()
p2 = Person("Teresa", 20, 158, 45)
p2.printdados()
p2.falar()
"""

#Ex4
"""class Contador:
    def __init__(self, contador=0):
         self.contador=contador

    def incrementa(self):
        self.contador+=1

    def decrementa(self):
        self.contador-=1
    
    def mostrarContador(self):
        print(self.contador)

contador = Contador()
contador.incrementa()
contador.incrementa()
contador.mostrarContador()
contador.decrementa()
contador.mostrarContador()

novoContador = Contador()
while novoContador.contador < 3:
    n = input("Carregue na tecla «ENTER» para retirar uma senha {}".format(novoContador.contador+1))
    if n == "":
        novoContador.contador += 1

print("Carregue mais papel!")
 """
    
