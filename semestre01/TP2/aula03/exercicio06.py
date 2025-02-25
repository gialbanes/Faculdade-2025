item = 1
preco = 1.99

print("Loja Quase Dois - Tabela de preços")

for item in range(1, 51):
    print(f"{item} - R${preco:.2f}")
    item += 1
    preco += 1.99