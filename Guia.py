from Fossil import Fossil

class Guia:
    def __init__(self, nome:str, genero:str, descricao:str, conhecimentoSobreFosseis:dict={}):
        self.__nome = nome.title()
        self.__genero = genero
        self.__conhecimento = conhecimentoSobreFosseis # O conhecimento sobre fósseis é um dicionário que tem o ID do fóssil como chave e uma história daquele fóssil como valor.
        self.descricao = descricao

    def getNome(self):
        return self.__nome
    
    def getGenero(self):
        return self.__genero
    
    def getConhecimento(self):
        return self.__conhecimento
    
    def setConhecimento(self, conhecimento_atual):
        self.__conhecimento = conhecimento_atual

    def historiaMuseu(self):
        return '\nO Museu Renato Marino foi inaugurado em 2021 quando o senhor Gilberto Marino, fundador do museu, descobriu em uma formação rochosa, próximo a sua casa, um fóssil de Ubirajara Jubatus. Para um amante de dinossauros, que cresceu vendo o trabalho de seu pai — Renato Marino, um grande paleontólogo que tinha um carinho especial pelos dinossauros — aquele momento foi tão inspirador e glorioso que ele decidiu construir um museu para a preservar a memória dos “gigantes” ancestrais e, assim, homenagear seu pai e compartilhar o conhecimento adquirido pelo mesmo. '
    
    def historiaFossil(self, fossil:Fossil):
        if fossil.getID() in self.__conhecimento.keys():
            print(f'   {self.getNome}:')
            return self.__conhecimento[fossil.getID()]
        else:
            return 'Sinto muito, mas ainda não tenho conhecimento o suficiente sobre esse fóssil.'