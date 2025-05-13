from Passagem import Passagem

if __name__ == "__main__":
    # instanciando um objeto da classe Passagem
    # eu poderia setar todos os dados dentro de () sem chamar os métodos 
    passagem = Passagem()

    # chamando os métodos de cadastrar com os dados 
    passagem.cadastrarDadosPassageiro("Giovana", "13997833467", "575620948")
    passagem.cadastrarDadosPassagem("Curitiba", "12/05/2025", "23:00", 20)

    passagem.mostrarDadosPassageiro()
    passagem.mostrarDadosPassagem()


