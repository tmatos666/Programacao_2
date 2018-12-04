"""
# Parte 1
class Carro:
    velocidadeMaxima = 200
    ligado = False

    def __init__(self, matricula, velocidadeAtual=0):
        self.matricula = matricula
        self.velocidadeAtual = velocidadeAtual

    def associaCondutor(self, condutor):
        self.condutor=condutor

    def isCarroLigado(self):
        if self.ligado:
            print("Carro esá ligado")
        else:
            print("Carro esá desligado")

    def ligarCarro(self):
        self.ligado = True

    def desligarCarro(self):
        self.ligado = False

    def acelerar(self):
        if self.ligado:
            self.velocidadeAtual += (10 + self.condutor.destreza*0.1)
            if self.velocidadeAtual > self.velocidadeMaxima:
                print("Velocidade é muito alta!!")
                self.velocidadeAtual = self.velocidadeMaxima

    def travar(self, intensidade):
        self.velocidadeAtual -= intensidade
        if self.velocidadeAtual < 0:
            print("Velocidade não pode ser menor que zero!!")
            self.velocidadeAtual = 0

    def imprimeDados(self):
        print("Condutor --> ",end="")
        self.condutor.imprimeDados()
        print("Carro --> Matricula:{0} \t velocidadeAtual:{1}".
        format(self.matricula, self.velocidadeAtual))

class Condutor:
    def __init__(self, nome, idade, destreza):
        self.nome=nome
        self.idade=idade
        self.destreza=destreza

    def imprimeDados(self):
        print("Nome:{0} \t idade:{1} \t destreza:{2}".format(self.nome, self.idade, self.destreza))


carro1 = Carro("11-AA-56")
carro1.associaCondutor(Condutor("Telmo", 30, 50))
#carro1.imprimeDados()
carro2 = Carro("10-BB-56")
carro2.associaCondutor(Condutor("Joaquim", 50, 10))
#carro2.imprimeDados()
carro1.ligarCarro()
carro2.ligarCarro()
carro1.acelerar()
carro1.acelerar()
carro2.acelerar()
carro2.acelerar()
carro1.travar(20)
carro2.travar(10)
carro1.imprimeDados()
carro2.imprimeDados()
carro1.desligarCarro()
carro2.desligarCarro()
"""

"""
#Parte 2
class CC:
    numeroCartaoGeneric = 1

    def __init__(self, nome, pontos=0, numeroCartao=0):
        self.nome = nome
        self.pontos = pontos
        self.numeroCartao = CC.numeroCartaoGeneric
        CC.numeroCartaoGeneric += 1

    def transfere(self, CC):
        self.pontos += CC.pontos
        CC.pontos = 0

    def mostra(self):
        print("Nome: {0}\n Cartao: {1}\n Pontos: {2}".format(
            self.nome, self.numeroCartao,  self.pontos))

p1 = CC("telmo", 5)
p2 = CC("Teresa", 10)
p1.transfere(p2)
p1.mostra()
p2.mostra()
"""

"""
#Parte 3
class Expenses:
    def __init__(self, number, value, date,type="other"):
        self.number=number
        self.type=type
        self.value=value
        self.date=date

    def printData(self):
        print("number: {0}, type: {1}, value: {2}, date: {3}".
        format(self.number,self.type, self.value,self.date))

class User:
    def __init__(self, name, email, birth, expenses):
        self.name=name
        self.email=email
        self.birth=birth
        self.expenses=expenses

    def printData(self):
        print("name:{0}, email:{1}, birth:{2}, expenses:".
        format(self.name,self.email, self.birth))
        for i in self.expenses:
            print("  -- ", end="")
            i.printData()

    def mostValueExpense(self, month):
        v = self.getMonthExpenses(month)
        if len(v) == 0:
            return "nenhuma despesa nesse mês"

        max = self.expenses[0].value
        for i in v:
            if max < i.value:
                max = i.value
        return max

    def expenseByMonths(self):
        month = []
        for j in range(12):
            month.append(self.mostValueExpense(j+1))
        return month

    def getMonthExpenses(self, month):
        ex = []
        for i in self.expenses:
            m = list(i.date)[3]+list(i.date)[4]
            if(int(m) == month):
                ex.append(i)
        return ex


e1 = Expenses(1, 10.5, "04-12-2018")
e2 = Expenses(1, 100.5, "05-08-2018", "Carro")
e3 = Expenses(1, 70.5, "10-12-2018", "Alimentação")
e4 = Expenses(1, 140.5, "11-08-2018", "Casa")
u1 = User("Telmo", "tsm@estg.ipp.pt", "10-01-1990", [e1,e2])
u2 = User("Joaquim", "jsa@estg.ipp.pt", "10-01-1960", [e3,e4])
u1.printData()
u2.printData()
print("Despesa mais elevada: ", u1.mostValueExpense(12))
j = 1
for i in u1.expenseByMonths():
    print("mes:{0} --> {1}".format(j,i))
    j+=1
"""

"""
#Parte 4
class Track:
    def __init__(self, number, name, duration, author):
        self.number=number
        self.name=name
        self.duration=duration
        self.author=author

class Cd:
    def __init__(self, name, year, editor, tracks):
        self.year=year
        self.name=name
        self.editor=editor
        self.tracks = tracks

    def printdata(self):
        print("CD: {0}, {1}, {2}".format(self.year, self.name, self.editor))
        for i in self.tracks:
            print("   {0},{1},{2},{3}".format(i.number,i.name, i.duration, i.author))

track1 = Track(1,"hello 1", 120, "Harvey")
track2 = Track(2,"hello 2", 110, "Robin Hood")
track3 = Track(3,"hello 3", 90, "Good Luck")
track4 = Track(4,"hello 4", 140, "Hello World")
track5 = Track(5,"hello 1", 130, "Good to be back")

cd1 = Cd("Hello and good luck",2018,"Editor 1",[track1,track2,track3,track4,track5])
cd1.printdata()
"""


