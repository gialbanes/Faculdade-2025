numero = int(input("Digite o número que você quer fazer a tabuada: "))
x = 0

print(f"Tabuada do {numero}:")

while x <= 10:
    print(f"{numero} X {x} = {numero * x}")
    x += 1