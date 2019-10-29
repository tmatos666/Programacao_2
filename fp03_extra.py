from pathlib import Path

#Ex1
"""
def list(p):
    if p.stem != '':
        print(p.stem)
        list(p.parent)

p = Path('c:/Users/aluno/Desktop/teste/teste1/teste2')
list(p)
"""

#Ex2
"""
name = input('Qual o nome do ficheiro?')
p = Path('.')
f = open(name, 'w')
for i in p.iterdir():
     f.write(str(i)+'\n')
f.close()
"""

#Ex3
"""
name = input('Qual o nome do ficheiro?')
p = Path('.')
f = open(name, 'w')
for i in p.glob('*.txt'):
    for x in i.open():
        f.write(x)
f.close()
"""

#Ex4
"""
f = open('numeros.txt', 'w')
soma = 0
text = 'Soma = '
for i in range(1000): 
    soma +=i
    if i%10==0 and i!= 0:
        f.write(text+str(soma)+'\n')
        soma = 0
    f.write(str(i+1)+'\n')
"""   

#Ex5
"""
def imprimirNum():
    f = open('numeros.txt', 'w')
    for i in range(1000): 
        f.write(str(i+1)+'\n')

def appendFile(name,n):
    f = open(name, 'a')
    f.write(str(n)+'\n')
    f.close()

def isPrime(n):  
    if n == 1:
        return True
    for i in range(2, n//2): #é suficiente procurar até metade do número 
        if (n % i) == 0: 
            return False
    return True

with open('numeros.txt') as line:
    for fp in line:
        i = fp.rstrip()
        if int(i)%2==0:
            appendFile('pares.txt',i)
        else:
            if isPrime(int(i))==True:
                appendFile('primos.txt',i)
            else:
                appendFile('impares.txt',i)
"""

#Ex6
"""
def lookString(file,s):
    count = 0
    with open(file) as line:
        for fp in line:
            i = fp.rstrip()
            string = i.split(' ')
            for str in string:
                if str == s:
                    count += 1
    return count


count = lookString('string.txt', 'ola')
print (count)
"""
