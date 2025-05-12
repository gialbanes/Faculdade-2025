class Funcionario:
    # Método construtor, é chamado automaticamente quando criamos um novo objeto da classe Funcionario
    def __init__(self, codigo, nome, salario, situacao):
        self.codigo = codigo  # código do funcionário (público)
        self.nome = nome  # nome do funcionário (público)
        self.__salario = salario  # __ -> torna o atributo privado (só pode ser acessado dentro da própria classe)
        self.situacao = situacao  # situação do funcionário (público)

    # get é um método que retorna o valor do atributo privado __salario
    def getSalario(self):
        return self.__salario  # permite acesso controlado ao valor do salário

    # o método set é usado para alterar/modificar o valor de um atributo privado (nesse caso, o salário)
    # o uso de set é opcional e depende de regras de negócio, como validações antes de alterar o atributo
    def setSalario(self, salario):
        self.__salario = salario  # altera o valor do salário para o novo valor passado por parâmetro

    # método para aplicar um reajuste percentual no salário
    # o parâmetro "valor" representa o percentual de reajuste (ex: 10 para 10%)
    def reajuste(self, valor):
        # aumenta o salário de acordo com o percentual informado
        # fórmula: novo salário = salário atual + (salário atual * percentual / 100)
        self.__salario = self.__salario + (self.__salario * valor / 100)
