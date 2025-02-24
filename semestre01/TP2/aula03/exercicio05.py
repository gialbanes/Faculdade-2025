res1 = str(input("Digite a sua resposta: "))
res2 = str(input("Digite a sua resposta: "))
res3 = str(input("Digite a sua resposta: "))

x = 1
pontos = 0

while x <= 3:
    if x == 1:
        if res1 == "a":
            pontos += 1
    elif x == 2:
        if res2 == "c":
            pontos += 1
    elif x == 3:
        if res3 == "d":
            pontos += 1
    x += 1

print(f"Você obteve {pontos}.")