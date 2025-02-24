tabuada = int(input("Digite o número que você quer fazer a tabuada: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

while inicio <= fim:
    print(f"{tabuada} X {inicio} = {tabuada * inicio}")
    inicio += 1