class Cliente:
    def __init__(self, nome, end, rg):
        self.nome = nome
        self.end = end
        self.rg = rg
    
    def cadastrarCliente(self):
        print(f'Cliente {self.nome} cadastrado com sucesso!')
    
    def listarCliente(self):
        print('*** Dados do Cliente: ***')
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.end}')
        print(f'RG: {self.rg}')