class Pessoa: 
    def __init__(self, nome, idade, ativo):
        self.nome = nome
        self.idade = idade
        self.ativo = ativo 
    
    def ativar(self):
        self.ativo = True
        print("A pessoa foi ativada com sucesso!")
           
    def desativar(self):
        self.desativar = True
        print("A pessoa foi desativada com sucesso!")