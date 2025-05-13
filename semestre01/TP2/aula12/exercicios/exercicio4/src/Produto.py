class Produto():
    def __init(self, nome = "", qtd = 0, valor = 0.0, total = 0.0):
        self.__nome = nome
        self.__qtd = qtd
        self.__valor = valor
        self.__total = total
    
    def getNome(self):
        return self.__nome
    
    def getQtd(self):
        return self.__qtd
    
    def getValor(self):
        return self.__valor
    
    def getTotal(self):
        return self.__total
    
    def setNome(self, nome):
        self.__nome = nome

    def setQtd(self, qtd):
        self.__qtd = qtd
    
    def setValor(self, valor):
        self.__valor = valor
    
    def setTotal(self, total):
        self.__total = total

    def calcularTotal(self):
        self.__total = self.getQtd() * self.getValor()
        print(f"Total: {self.getTotal()}")