class Fornecedor:
    def __init__(self, nomeFornecedor, nomeProduto, descricaoProduto):
        self.nomeFornecedor = nomeFornecedor 
        self.nomeProduto = nomeProduto
        self.descricaoProduto = descricaoProduto
    
    def cadastrarFornecedor(self, nomeFornecedor, nomeProduto, descricaoProduto):
        self.nomeFornecedor = nomeFornecedor    
        self.nomeProduto = nomeProduto
        self.descricaoProduto = descricaoProduto
    
    def listarFornecedor(self):
        print(f"Nome do fornecdor {self.nomeFornecedor}")
        print(f"Nome do produto: {self.nomeProduto}")
        print(f"Descrição do produto: {self.descricaoProduto}")