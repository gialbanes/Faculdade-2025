valor_compra = int(input("Digite o valor da compra: "))

if valor_compra < 20:
    valor_total = valor_compra + (valor_compra * 0.45)
    print(f"O valor do produto com o lucro de 45% é {valor_total}")
else:
    valor_total = valor_compra + (valor_compra * 0.30)
    print(f"O valor do produto com o lucro de 30% é {valor_total}")