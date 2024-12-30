from Fossil import Fossil

class Guia:
    def __init__(self, nome:str, conhecimentoSobreFosseis:dict={}):
        self.__nome = nome
        self.__conhecimento = conhecimentoSobreFosseis # O conhecimento sobre fósseis é um dicionário que tem o ID do fóssil como chave e uma história daquele fóssil como valor.

    def getNome(self):
        return self.__nome
    
    def historiaMuseu(self):
        return '' #História do museu vai ser acrescentada aqui
    
    def historiaFossil(self, fossil:Fossil):
        return self.__conhecimento[fossil.getID]