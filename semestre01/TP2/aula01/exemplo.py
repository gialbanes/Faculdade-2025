valorProduto = float(input("Digite o valor do produto: "))
valorDesconto = float(input("Digite o desconto em %: "))

valorDesconto = valorProduto * valorDesconto / 100
valorVenda = valorProduto - valorDesconto

print(f"O valor final da venda é: R${valorVenda}")