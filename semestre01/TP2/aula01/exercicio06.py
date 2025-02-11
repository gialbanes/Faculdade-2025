salAtual = float(input("Digite o salário atual do funcionário: "))
reajuste = float(input("Digite o reajuste em %: "))
reajuste = salAtual *  reajuste / 100
salNovo = salAtual + reajuste


print(f"O novo salário do funcionário é R${salNovo}")
