# Ex1
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

# Ex2
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

# Ex3
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

# Ex4
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

"""
# Ex 5
class Dog:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def toString(self):
        return "nome:{0}\nidade:{1}\n---------".format(self.nome, self.idade)

class Pets:
    def __init__(self, dogs=None):
        self.dogs = dogs

    def toString(self):
        for i in self.dogs: 
            print(i.toString())

d1=Dog("Becky",10)
d2=Dog("Scooby",1)
d3=Dog("Laika",5)

pets = Pets([d1, d2, d3])
pets.toString()
"""

"""
# Ex 6
class Rectangle:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def area(self):
        return self.comprimento*self.largura


rec = Rectangle(10, 5)
print(rec.area())
"""

"""
import math
# Ex 7
class Circle:
    def __init__(self, raio):
        self.raio = raio

    def perimetro(self):
        return 2*math.pi*self.raio

    def area(self):
        return 2*math.pi*(self.raio*self.raio)


circle = Circle(5)
print(circle.perimetro())
print(circle.area())
"""

"""
#Ex8
surname is a class attribute
all the rest are instance attributes
"""

"""
# Ex9
class Numbers:
    multiplier = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self, a):
        return Numbers.multiplier*a

    @staticmethod
    def subtract(b, c):
        return b - c

    def values(self):
        return [self.x, self.y]

a = Numbers(1,2)
print(a.add())#expected 3
print(a.multiply(10))#expected 20
print(a.subtract(5,3))#expected 2

for i in a.values():#expected [1,2]
    print(i)
"""
