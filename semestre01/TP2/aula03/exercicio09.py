nomes = ["Maria", "João", "Paulo", "Magali"]

localizar = str(input("Digite o nome que você quer localizar: "))

for nome in nomes:
    if localizar == nome:
        print("Nome encontrado")
        break
else:
    print("Nome não encontrado")