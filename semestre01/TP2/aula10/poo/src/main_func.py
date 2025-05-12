from Funcionario import Funcionario  # importa a classe Funcionario do arquivo Funcionario.py

# esse bloco garante que o código só será executado se o arquivo for executado diretamente
if __name__ == '__main__':
    
    # cria um objeto da classe Funcionario com código 5, nome "Giovana", salário 200 e situação ativa (True)
    func = Funcionario(5, "Giovana", 200, True)
    
    # cria outro objeto da classe Funcionario com dados diferentes
    func2 = Funcionario(6, "Maria", 2200, True)
    
    # cria um terceiro objeto da classe Funcionario
    func3 = Funcionario(7, "João", 1200, True)

    # aplica um reajuste de 10% no salário da funcionária "Giovana"
    func.reajuste(10)
    
    # aplica um reajuste de 20% no salário da funcionária "Maria"
    func2.reajuste(20)
    
    # aplica um reajuste de 30% no salário do funcionário "João"
    func3.reajuste(30)

    # acessando o salário privado de cada funcionário através do método getSalario()
    # não é possível acessar __salario diretamente, pois é um atributo privado
    print(f"Salário do funcionário: {func.getSalario()}")   # imprime o salário reajustado da Giovana
    print(f"Salário do funcionário: {func2.getSalario()}")  # imprime o salário reajustado da Maria
    print(f"Salário do funcionário: {func3.getSalario()}")  # imprime o salário reajustado do João
