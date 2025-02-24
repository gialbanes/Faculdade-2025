pao = 1 
preco = float(input("Digite o preço unitário do pão: "))
precoX = preco

for pao in range(1, 51):
    print(f"{pao} - R${preco:.2f}")
    pao += 1
    preco += precoX