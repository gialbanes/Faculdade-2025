num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("----------------------------------------------------")

op = int(input("Escolha uma opção: \n 1. Média ponderada com pesos 2 e 3 \n 2. Quadrado da soma dos 2 números \n 3. Cubo do menor número\n"))

print("----------------------------------------------------")

if op == 1:
    media1 = num1 * 2
    media2 = num2 * 3
    print(f"A média ponderado do número {num1} por 2 é {media1}")
    print(f"A média ponderado do número {num2} por 3 é {media2}")
if op == 2:
    soma = num1 + num2
    quadrado = pow(soma, 2)
    print(f"O quadrado da soma dos números {num1} e {num2} é {quadrado}")
if op == 3:
    if num1 > num2:
        menor = num2
    else:
        menor = num1
    cubo = pow(menor, 3)
    print(f"O menor número é {menor} e o seu cubo é {cubo}")