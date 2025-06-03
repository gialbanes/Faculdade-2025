import math

num = int(input("Digite um número inteiro positivo: "))

if num%2 == 0:
    quadrado = math.pow(num, 2)
    print(f"O número digitado foi {num}, ele é par e o seu quadrado é {quadrado}")

else:
    cubo = math.pow(num, 3)
    print(f"O número digitado foi {num}, ele é ímpar e o seu cubo é {cubo}.")

