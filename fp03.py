#Ex1
"""from pathlib import Path
p = Path('c:/Users/RAMP/Desktop/A nossa casa')
for x in p.iterdir():
    print(x)
"""

#Ex2
"""from pathlib import Path
p = Path('c:/Users/RAMP/Desktop/A nossa casa')
for x in p.iterdir():
    if x.is_dir():
        print(x)
"""

#Ex3
"""from pathlib import Path
p = Path('c:/Users/RAMP/Desktop/A nossa casa')
for x in p.iterdir():
    if x.is_file(): #ou if not x.is_dir()
        print(x)
"""

#Ex4
"""from pathlib import Path
p = Path('c:/Users/RAMP/Desktop/fp03_exercicios')
p.mkdir()
f = open('c:/Users/RAMP/Desktop/fp03_exercicios/ex4.py', 'x')
for i in range(10):
     f.write("This is line %d\n" % (i+1))
"""

#Ex5
"""from pathlib import Path
p = Path('c:/Users/RAMP/Desktop/fp03_exercicios/ex4.py')
print(p.read_text())
"""

#Ex6
"""import re
from pathlib import Path
p = Path('c:/Users/RAMP/Desktop/fp03_exercicios/ex4.py')
pattern = re.compile(r"\d+")
sum = 0
for x in p.open():
    #print(x)
    s = re.search(pattern, x) 
    sum += int(s[0])
    #print(s)
print(sum)
"""

#Ex7
"""from pathlib import Path
p = Path('c:/Users/RAMP/Desktop/fp03_exercicios/testeDir_1')
p.mkdir()
p = Path('c:/Users/RAMP/Desktop/fp03_exercicios/testeDir_2')
p.mkdir()
p = Path('c:/Users/RAMP/Desktop/NovoDir_1/')
p.mkdir()
p = Path('c:/Users/RAMP/Desktop/NovoDir_1/testeDir_1')
p.mkdir()

p = Path('c:/Users/RAMP/Desktop/fp03_exercicios/')
q = Path('c:/Users/RAMP/Desktop/NovoDir_1/')
for x in p.iterdir():
    if x.is_dir():
        for y in q.iterdir():
            if y.is_dir():
                if x.stem == y.stem:
                    print(x)
"""

#Ex8
"""from pathlib import Path
f = open('c:/Users/RAMP/Desktop/NovoDir_1/OddNumbers.txt', 'w')
valor = input('introduza uma valor inteiro: ')
while int(valor) < 1:
    valor = input('introduza uma valor inteiro: ')
for i in range(int(valor)+1):
    if i%2 == 0: 
        f.write("%s\n" % i)
"""        