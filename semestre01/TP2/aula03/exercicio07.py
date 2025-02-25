pao = 1 
preco = float(input("Digite o preço unitário do pão: "))
precoX = preco

print("Panificadora Pão de Ontem - Tabela de preços")

for pao in range(1, 51):
    if pao % 2 == 0:
        print(f"{pao} - R${preco:.2f}")
        pao += 1
        preco += precoX