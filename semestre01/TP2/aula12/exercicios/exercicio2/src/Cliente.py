class Cliente:
    def __init__(self, nome="", end="", rg=""):
        self.__nome = nome
        self.__end = end
        self.__rg = rg

    def getNome(self):
        return self.__nome

    def getEnd(self):
        return self.__end
    
    def getRg(self):
        return self.__rg
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setEnd(self, end):
        self.__end = end
    
    def setRg(self, rg):
        self.__rg = rg
    
    def cadastrarCliente( self, nome, end, rg):
        self.setNome = nome 
        self.setEnd = end
        self.setRg = rg

    def listarCliente(self):
        print(f"Nome: {self.getNome()}")
        print(f"Endereço: {self.getEnd()}")
        print(f"RG: {self.getRg()}")