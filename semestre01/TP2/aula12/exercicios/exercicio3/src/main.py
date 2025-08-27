from Fornecedor import Fornecedor 

if __name__ == "__main__":
    f = Fornecedor()

    f.setNomeFornecedor("Giovana")
    f.setNomeProduto("Celular")
    f.setDescricaoProduto("Iphone 16")

    f.listarFornecedor()