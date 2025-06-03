peso1 = float(input("Digite o peso da primeira pessoa: "))
peso2 = float(input("Digite o peso da segunda pessoa: "))

if peso1 > peso2:
    print(f"O peso maior é {peso1}kg da primeira pessoa.")
elif peso1 == peso2:
    print(f"As pessoas tem o mesmo peso de {peso1}kg.")
else:
    print(f"O peso maior é {peso2}kg da segunda pessoa.")