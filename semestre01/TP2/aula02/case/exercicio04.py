preco = float(input("Digite o total da compra: "))
op = int(input("Escolha a forma de pagamento: \n 1. À vista (dinheiro) \n 2. Débito \n 3. Crédito\n"))

match op:
    case 1:
        desconto = preco * 15 / 100
        total = preco - desconto
        print(f"O valor da sua compra é R${preco},00 e com o desconto de 15% fica R${total},00")
    case 2:
        desconto = preco * 10 / 100
        total = preco - desconto
        print(f"O valor da sua compra é R${preco},00 e com o desconto de 10% fica R${total},00")
    case 3:
        desconto = preco * 5 / 100
        total = preco - desconto
        print(f"O valor da sua compra é R${preco},00 e com o desconto de 5% fica R${total},00")
    