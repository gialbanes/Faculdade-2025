tam = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(tam):
    vetor.append(str(input(f"Digite a cor da posição {i}: ")))

print(f"Vetor: {vetor}")
