from pessoa_classe import Pessoa
class Visitante(Pessoa):
    def __init__(self, nome, cpf, dataNascimento, email, senha):
        super().__init__(nome, cpf, dataNascimento, email, senha)
        self.__guia = None

    def setGuia(self,guianovo):
        self.__guia = guianovo

    def getGuia(self):
        return self.__guia

    def falar(self):
        print(f'Olá, me chamo {self.nome.title()} e vim para conhecer mais sobre dinossauros!')
    def acessar(self):
        item = input(f'Desejo acessar o item: ')
        return item

