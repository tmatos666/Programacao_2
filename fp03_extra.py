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
     print(i)
f.close()
"""

#Ex3
"""
name = input('Qual o nome do ficheiro?')
p = Path('C:/Users/RAMP/Desktop/MeoCloud/Aulas ESTGF/2019_2020/CTESP/Programação 2/Práticas/Programacao_2')
f = open(name, 'w')
for i in p.glob('*.txt'):
    for x in i.open():
        f.write(x)
f.close()
"""
