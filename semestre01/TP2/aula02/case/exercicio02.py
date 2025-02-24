indice = int(input("Digite o índice de poluição: "))

match indice:
    case 0 | 1 | 2:
        print("Considerar aceitável")
    case 3 | 4 | 5:
        print("Suspender atividades")
    case 6 | 7:
        print("Considerar aceitável")
    case _:
        print("Suspender atividades de todos os grupos")