nomes = ["luiz", "ana cristina", "fernanda", "maria alice", "joaquina"]

x = int(input("Escolha uma opção: \n1 - Fazer busca \n0 - Sair\n"))

while x != 0:
    localizador = str(input("Digite o nome que você quer ver: "))
    for nome in nomes:
        if localizador == nome:
            print("Nome encontrado")
            break
    else:
        print("Nome não encontrado")
    x = int(input("Escolha uma opção: \n1 - Fazer busca \n0 - Sair\n"))