class Pessoa: 
    # método construtor da classe Pessoa, chamado automaticamente quando um novo objeto é criado
    def __init__(self, nome, idade, ativo):
        self.nome = nome      # nome da pessoa (público)
        self.idade = idade    # idade da pessoa (público)
        self.ativo = ativo    # indica se a pessoa está ativa (público - True ou False)
    
    # método para ativar a pessoa (define o atributo ativo como True)
    def ativar(self):
        self.ativo = True  # ativa a pessoa
        print("A pessoa foi ativada com sucesso!")  # mensagem de confirmação
    
    # método para desativar a pessoa (deveria definir o atributo ativo como False)
    def desativar(self):
        self.ativo = False  # desativa a pessoa (corrigido, estava com erro no código original)
        print("A pessoa foi desativada com sucesso!")  # mensagem de confirmação
