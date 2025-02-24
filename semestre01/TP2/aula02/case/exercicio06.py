pessoa = float(input("Digite o peso da pessoa na Terra: "))
planeta = input("Digite o número do planeta: ")

match planeta:
    case 1:
        peso = pessoa * 0.37
        print(f"O peso da pessoa em Mercúrio é {peso}")
    case 2: 
        peso = pessoa * 0.88
        print(f"O peso da pessoa em Vênus é {peso}")
    case 3: 
        peso = pessoa * 0.38
        print(f"O peso da pessoa em Marte é {peso}")
    case 4: 
        peso = pessoa * 2.64
        print(f"O peso da pessoa em Júpiter é {peso}")
    case 5: 
        peso = pessoa * 1.15
        print(f"O peso da pessoa em Saturno é {peso}")