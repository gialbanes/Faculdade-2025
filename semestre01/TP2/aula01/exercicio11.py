nome = str(input("Digite o nome do produto: "))
qtd_comprada = int(input("Digite a quantidade comprada do produto: "))
preco = float(input("Digite o valor unitário do produto: "))

total = qtd_comprada * preco

print("---------------------------------------------------------")
print(f"{qtd_comprada} unidade(s) de {nome} custam R${total:.2f}")