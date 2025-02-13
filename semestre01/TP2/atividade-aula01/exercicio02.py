valor = float(input("Qual o valor da prestação a ser paga? "))
taxa = float(input("Qual a taxa de juros imposta pelo banco? "))
tempo = int(input("Qual a quantidade de meses em atraso? "))

valorAtraso = valor + (valor * (taxa/100) * tempo)

print("----------------------------------------------------")

print(f"A prestação em atraso no valor de R${valor},00 somada à taxa de juros de {taxa}% imposta pelo banco resulta em R${valorAtraso} para ser pago.")