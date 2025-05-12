from Pessoa import Pessoa  # importa a classe Pessoa do arquivo Pessoa.py

# esse bloco garante que o código só será executado se o arquivo for executado diretamente,
# e não se for importado por outro módulo
if __name__ == '__main__':
    
    # cria um objeto da classe Pessoa com nome "Giovana", idade 19 e status ativo (True)
    pessoa = Pessoa("Giovana", 19, True)
    
    # imprime o nome da pessoa acessando diretamente o atributo público
    print(pessoa.nome)
    
    # imprime a idade da pessoa acessando diretamente o atributo público
    print(pessoa.idade)
    
    # imprime se a pessoa está ativa (True ou False)
    print(pessoa.ativo)
