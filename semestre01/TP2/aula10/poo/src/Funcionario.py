class Funcionario:
    def __init__(self, codigo, nome, salario, situacao):
        self.codigo = codigo 
        self.nome = nome
        self.__salario = salario # __ -> torna o atributo privado
        self.situacao = situacao
    
    # get é um método que retorna o valor do atributo, nesse caso do salário que deixei privado
    def getSalario(self):
        return self.__salario
    
    # o método set é opcional dependendo do cenário 
    def setSalario(self, salario):
        self.__salario = salario

    def reajuste(self, valor):
        self.__salario = self.__salario + (self.__salario * valor / 100)