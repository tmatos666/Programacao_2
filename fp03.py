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