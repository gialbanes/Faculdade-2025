class Operacao:
    def __init__(self, x="", y=""):
        self.__x = x 
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y
    
    def somar(self):
        return print(self.getX() + self.getY())
