num = int(input("Digite um número inteiro positivo: "))

if num % 2 == 0:
    quadrado = pow(num, 2)
    print("----------------------------------------")
    print(f"O número é par e o seu quadrado é {quadrado}")
else:
    cubo = pow(num, 3)
    print("----------------------------------------")
    print(f"O número é ímpar e o seu cubo é {cubo}")
