class Fossil:
    def __init__(self, id:str, nomeCientificoDino:str,nomePopularDino:str, categoria:str, parte:str,idade:str,urlImagem:str = None):
        self.__id = id
        self.__dinossauro = nomeCientificoDino.title()
        self.__nomePopular = nomePopularDino.title()
        self.__categoria = categoria.lower()
        self.__parte = parte.lower()
        self.__idade = idade
        self.__imagem = urlImagem

    def getID(self):
        return self.__id
    
    def getDinossauro(self):
        return self.__dinossauro.title()
    
    def getDinoPopular(self):
        return self.__nomePopular.title()
    
    def getCategoria(self):
        return self.__categoria
    
    def getParte(self):
        return self.__parte
    
    def getIdade(self):
        return self.__idade
    
    def getURLimagem(self):
        return self.__imagem
    
    def setURLimagem(self, novaURL):
        self.__imagem = novaURL
        