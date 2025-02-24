categoria = str(input("Digite a categoria do empregado: "))
salario = float(input("Digite o salário do empregado: "))

match categoria:
    case "a":
        aumento = salario * 10  
        total = salario + aumento
        print(f"O salário do empregado é R${salario},00 e com o aumento de 10% fica R${total},00")
    case "b":
        aumento = salario * 15
        total = salario + aumento
        print(f"O salário do empregado é R${salario},00 e com o aumento de 15% fica R${total},00")
    case "c":
        aumento = salario * 25
        total = salario + aumento
        print(f"O salário do empregado é R${salario},00 e com o aumento de 20% fica R${total},00")
    case _:
        print("Categoria inválida")