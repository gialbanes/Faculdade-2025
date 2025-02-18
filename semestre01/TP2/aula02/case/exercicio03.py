
op = int(input("Escolha uma opção \n 1. Tensão (em volt) \n 2.Resistência (em Ohm) \n 3. Corrente (em Ampére) \n"))

match op:
    case 1:
        r = int(input("Digite a resistência: "))
        i = int(input("Digite a corrente: "))
        u = r * i 
        print(f"A tensão é {u}V.")
    case 2:
        u = int(input("Digite a tensão: "))
        i = int(input("Digite a corrente: "))
        r = u / i 
        print(f"A resistência é {r}Ohm.")
    case 3:
        u = int(input("Digite a tensão: "))
        r = int(input("Digite a resistência: "))
        i = u / r
        print(f"A corrente é {i} Ampére.")