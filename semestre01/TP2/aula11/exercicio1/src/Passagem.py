class Passagem:
    # método construtor (especial) chamado quando um objeto é criado 
    def __init__(self, nomePassageiro=None, telefone=None, rg=None, localViagem=None, data=None, horario=None, numPoltrona=None):
        self.nomePassageiro = nomePassageiro
        self.telefone  = telefone
        self.rg = rg
        self.localViagem = localViagem   
        self.data = data
        self.horario  = horario
        self.numPoltrona = numPoltrona
    
    def cadastrarDadosPassageiro(self, nomePassageiro, telefone, rg):
        self.nomePassageiro = nomePassageiro  # atribui o valor do parâmetro ao atributo da instância
        self.telefone = telefone 
        self.rg = rg

    def cadastrarDadosPassagem(self, localViagem, data, horario, numPoltrona):
        self.localViagem = localViagem 
        self.data = data
        self.horario = horario 
        self.numPoltrone = numPoltrona

    def mostrarDadosPassageiro(self):
        print(f"Nome do passageiro: {self.nomePassageiro}")
        print(f"Telefone: {self.telefone}")
        print(f"RG: {self.rg}")
    
    def mostrarDadosPassagem(self):
        print(f"Local da viagem: {self.localViagem}")
        print(f"Data da passagem: {self.data}")
        print(f"Horário da viagem: {self.horario}")
        print(f"Número da poltrona: {self.numPoltrona}")