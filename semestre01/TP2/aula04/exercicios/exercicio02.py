l = int(input("Digite a qtd de linhas da matriz: "))
c = int(input("Digite a qtd de colunas da matriz: "))

matriz = []

for i in range(l):
    l = []
    matriz.append(l)
    for j in range(c):
        elemento = float(input(f"Digite o elemmento na posição {i + 1}x{j + 1}:"))
        l.append(elemento)

for linha in matriz:
    print(' '.join(map(str, l)))