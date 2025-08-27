class Fornecedor:
    def __init__(self, nomeFornecedor = "", nomeProduto = "", descricaoProduto = ""):
        self.__nomeFornecedor = nomeFornecedor
        self.__nomeProduto = nomeProduto
        self.__descricaoProduto = descricaoProduto

    def getNomeFornecedor(self):
        return self.__nomeFornecedor
    
    def getNomeProduto(self):
        return self.__nomeProduto
    
    def getDescricaoProduto(self):
        return self.__descricaoProduto
    
    def setNomeFornecedor(self, nome):
        self.__nomeFornecedor = nome

    def setNomeProduto(self, nomeP):
        self.__nomeProduto = nomeP

    def setDescricaoProduto(self, desc):
        self.__descricaoProduto = desc
    
    def cadastrarFornecedor(self, nome, nomeP, desc):
        self.setNomeFornecedor = nome
        self.setNomeProduto = nomeP
        self.setDescricaoProduto = desc 
    
    def listarFornecedor(self):
        print(f"Nome do fornecedor: {self.getNomeFornecedor()}")
        print(f"Nome do produto: {self.getNomeProduto()}")
        print(f"Descrição do produto: {self.getDescricaoProduto()}")