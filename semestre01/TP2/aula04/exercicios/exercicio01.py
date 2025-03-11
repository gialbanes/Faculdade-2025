tam = int(input("Digite o tamaho do vetor: "))
vetor = []

for i in range(tam):
    vetor.append(int(input(f"Digite o elemento {i + 1} do vetor: ")))

print(f"Vetor: {vetor}")