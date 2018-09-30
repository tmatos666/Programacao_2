#Ex 1
"""x =[]
for i in range(21):
    x.append(i+5)
"""

#Ex 2
"""x=[]
soma = 0
n = input('Input number: ')
while n != '-1' and len(x) < 10:
    x.append(n)
    soma = soma + int(n)
    n = input('Input number: ')
print('Average = ' , soma/len(x))
"""

#Ex 3
"""x=[]
while len(x) < 10:
    n = input('Input number: ')
    x.append(n)
c = input('Odd(P) or Even(I)?: ')
odd = 0
if c == 'I':
    odd = 1
for i in range(len(x)):
    if int(x[i]) % 2 == odd:
            print(x[i])
"""

#Ex 4
"""def imp(n):
    for i in range(0,n):
        print('*',end='')

n = input('Input number: ')
imp(int(n))
"""

#Ex 5
"""def operation(a,b,t):
    if t == '+':
        return a+b
    elif t == '-':
        return a-b
    elif t == '*':
        return a*b
    else:
        return a/b
a = input('Input first number: ')
b = input('Input second number: ')
op = input('Input operation (+,-,*,/): ')
final = operation(int(a), int(b), op)
print(final)
"""

#Ex 6
"""def lerInteiro(n, caracter):
    for i in range(0,n):
        print(caracter,end='')

n = input('Input number: ')
lerInteiro(int(n), '#')
"""

#Ex 7
"""def validGrade(n):
    if int(n) < 21 and int(n) >= 0:
        return n
    else:
        return -1

def lerNotas():
    sum = 0
    i = 0
    while  i < 10:
        n = input('Input grade: ')
        if validGrade(n) != -1:
            sum += int(n)
            i = i+1
        else:
            print('Grade error!!')       
    return sum/10

print('Average: ', lerNotas())
"""
#Ex 8
"""def do(numero):
    if numero == 0:
        return 0
    else:
        print('*' * numero)
        do(numero-1)
do(4)
"""