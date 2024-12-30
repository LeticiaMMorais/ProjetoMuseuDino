class Fossil:
    def __init__(self, id:str, dinossauro:str, categoria:str, parte:str,idade:int):
        self.__id = id
        self.__dinossauro =dinossauro
        self.__categoria = categoria
        self.__parte = parte
        self.__idade = idade

    def getID(self):
        return self.__id
    
    def getDinossauro(self):
        return self.__dinossauro
    
    def getCategoria(self):
        return self.__categoria
    
    def getParte(self):
        return self.__parte
    
    def getIdade(self):
        return self.__idade
    
        