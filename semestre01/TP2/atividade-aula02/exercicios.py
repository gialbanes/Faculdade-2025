ano_atual = int(input("Em qual ano você está? "))
ano_nasc = int(input("Em qual ano você nasceu? "))

idade = ano_atual - ano_nasc

if idade >= 16:
    print("Você já pode votar!")
else:
    print("Você ainda não pode votar!")

"""
# EXERCÍCIO 2
m = int(input("Digite uma medida em metros: "))
conversao = int(input("Escolha uma conversão: \n 1. Decímetros \n 2. Centímetros \n 3. Milímetro \n "))

match conversao:
    case 1:
        d = m * 10.0 
        print(f"{m}m em decímetros é {d}dm.")
    case 2: 
        c = m * 100.0
        print(f"{m}m em centímetros é {c}cm.")
    case 3:
        mm = m * 1000.0
        print(f"{m}m em milímetros é {mm}mm.")
    case _:
        print("Erro")      
"""









"""
# EXERCÍCIO 3
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
op = int(input("Escolha uma operação: \n 1. + \n 2. - \n 3. * \n 4. \n"))

match op:
    case 1:
        soma = num1 + num2
        print(f"A soma entre {num1} e {num2} é {soma}")
    case 2:
        sub = num1 - num2
        print(f"A subtração entre {num1} e {num2} é {sub}")
    case 3: 
        multiplicacao = num1 * num2
        print(f"A multiplicação entre {num1} e {num2} é {multiplicacao}")
    case 4: 
        divisao = num1 / num2 
        print(f"A divisão entre {num1} e {num2} é {divisao}")
    case _:
        print("Erro")
"""






"""
# EXERCÍCIO 4
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1 > num2:
    subtracao = num1 - num2 
    print(f"{num1} - {num2} = {subtracao}")
else:
    subtracao = num2 - num1
    print(f"{num2} - {num1} = {subtracao}")
"""






"""
# EXERCÍCIO 5
nome1 = str(input("Digite o nome da primeira pessoa: "))
h1 = float(input("Digite a altura da primeira pessoa: "))
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = str(input("Digite o nome da segunda pessoa: "))
h2 = float(input("Digite a altura da segunda pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))

if h1 > h2:
    print(F"*** DADOS PESSOAIS *** \n Nome: {nome1} \n Altura: {h1} \n Idade: {idade1} \n")
else:
    print(F"*** DADOS PESSOAIS *** \n Nome: {nome2} \n Altura: {h2} \n Idade: {idade2} \n")
"""






"""
# EXERCÍCIO 6 
compra = float(input("Qual o valor da compra? "))

if compra < 20:
    venda = compra * 1.45
    print(f"O valor de venda do produto será: R$ {venda:.2f}")
else:
    venda = compra * 1.30
    print(f"O valor de venda do produto será: R$ {venda:.2f}")
"""






"""
# EXERCÍICO 7 
nome = str(input("Qual é o nome do cliente? "))
deposito = float(input("Qual é o valor do depósito? "))

saldoAtual = 800 + deposito

print("-------------------------------------")

if saldoAtual == 0:
    print("Saldo limite.")
elif saldoAtual > 0:
    print("Saldo positivo.")
else:
    print("Saldo negativo.")
    
print("-------------------------------------")

print(f"*** DADOS PESSOAIS *** \n Nome: {nome} \n Saldo atual: {saldoAtual}")
"""