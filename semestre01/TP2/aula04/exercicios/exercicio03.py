l = int(input("Digite a qtd de linhas da matriz: "))
c = int(input("Digite a qtd de colunas da matriz: "))
matriz = []

for i in range(l):
    l = []
    matriz.append(l)
    for j in range(c):
        capital = str(input(f"Digite o nome da capital na posição {i+1}x{j+1}:"))
        l.append(capital)

for l in matriz:
    print(' '.join(map(str, l)))