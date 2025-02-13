custoFabrica = float(input("Qual o custo de fabricação do carro?"))
distribuidor = 0.28
impostos = 0.45

percDisribuidor = 0.28 * custoFabrica
percImposto = 0.45 * custoFabrica

total = custoFabrica + percDisribuidor + percImposto

print("----------------------------------------")

print(f"O valor à ser pago pelo carro é R${total}.")