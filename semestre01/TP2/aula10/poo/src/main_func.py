from Funcionario import Funcionario

if __name__ == '__main__':
    func = Funcionario(5, "Giovana", 200, True)
    func2 = Funcionario(6, "Maria", 2200, True)
    func3 = Funcionario(7, "João", 1200, True)

    func.reajuste(10)
    func2.reajuste(20)
    func3.reajuste(30)

    # acessando o salário privado através do get 
    print(f"Salário do funcionário: {func.getSalario()}")
    print(f"Salário do funcionário: {func2.getSalario()}")
    print(f"Salário do funcionário: {func3.getSalario()}")