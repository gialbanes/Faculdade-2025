nome = "Giovana"
salFixo = 1500
bonus = 50

qtdSoftware = int(input("Quantos softwares o seu funcionário vendeu? "))

salTotal = salFixo + (bonus * qtdSoftware)

print("------------------------------------------------------------------")

print(f"O salário do(a) funcionário(a) {nome} é R${salTotal},00")