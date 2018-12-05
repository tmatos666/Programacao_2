import os
ans = 0
while ans != 3:
    os.system('cls')
    print("""
    1. menu 1
    2. menu 2
    3. Exit/Quit""")
    ans = input("Escolha uma opção? ")
    if ans == "1":
        print("\n menu 1")
        #code here
        input("Prima qualquer tecla para sair")
    elif ans == "2":
        print("\n menu 2")
        #code here
        input("Prima qualquer tecla para sair")
    elif ans == "3":
        print("\n Até breve!")
        ans = 3
    else:
        print("\n Escolha uma opção válida!")