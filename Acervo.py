from Fossil import Fossil
class Acervo:
    def __init__(self, fosseis:list=[]):
        self.__fosseis = fosseis


    def getFosseis(self):
        return self.__fosseis
    

    def __adicionar_fossil(self, dinossauro:str,categoria:str, parte:str, idade:int):
        novoID = dinossauro[:2].lower()
        while len(novoID)<=3:
            num = range.randint(100000,999999)
            igual = False
            for fossil in self.__fosseis:
                if fossil.getID() == novoID + str(num):
                    igual = True
            if not igual:
                novoID += str(num)

        novoFossil = Fossil(novoID, dinossauro, categoria, parte, idade)
        self.__fosseis.append(novoFossil)
        print('Fóssil adicionado no acervo!')


    def __excluir_fossil(self,id:str):
        encontrado = False
        for fossil in self.__fosseis:
            if fossil.getID() == id:
                encontrado = True
                self.__fosseis.remove(fossil)
                print(f'O seguinte fóssil foi excluído:\nID:{fossil.getID()}\nDinossauro:{fossil.getDinossauro()}\nCategoria:{fossil.getCategoria()}\nParte:{fossil.getParte()}\nIdade:{fossil.getIdade()}')
        if not encontrado:
            print('Nenhum fóssil com esse ID foi encontrado em nosso acervo.')


    def edicao(self,edit:int):
        if edit == 2:
            id_dinossauro = input('\nCerto, digite o ID do dinossauro que quer excluir: ')
            self.__excluir_fossil(id_dinossauro)

        elif edit == 1:
            nomeDino = input('Digite o nome do dinossauro a que pertence o fóssil: ')
            categoria = input('Digite o tipo da alimentação do dinossauro (Herbivoro, Carnivoro ou Onivoro): ')
            parteDino = input('Digite a parte do corpo do dinossauro a que se refere o fóssil: ')
            idadeFossil = int(input('Informe a idade do fóssil: '))
            
            self.__adicionar_fossil(nomeDino,categoria,parteDino,idadeFossil)

        else:
            print('Só há duas opções: 1 para adicionar e 2 para excluir algum fóssil.')


    def listar(self):
        print('Aqui estão os fósseis do nosso acervo: \n')
        for fossil in self.__fosseis:
            print(f'ID: {fossil.getID()}\nDinossauro: {fossil.getDinossauro()}\nCategoria: {fossil.getCategoria()}\nParte do corpo: {fossil.getParte()}\nIdade:{fossil.getIdade()}\n')
        print("      Você chegou ao fim do acervo.")


    def encontrar_fossil(self,pesquisa:str, modo:int=1):
        '''
        Pode-se encontrar fósseis por três maneiras diferentes, por isso, informa-se um número inteiro de 1 a 3 como argumento para modo (sendo que é padrão o número 1).
        Esses números equivalem a: 1-ID do fóssil, 2-Nome do dinossauro, 3-Categoria do dinossauro.

        No parâmetro pesquisa põe-se o está procurando de acordo com o modo.
        '''
        listaEncontrados = []
        for fossil in self.__fosseis:
            if modo == 1:
                if fossil.getID() == pesquisa:
                    listaEncontrados.append(fossil)
            elif modo == 2:
                if fossil.getDinossauro().upper() == pesquisa.upper():
                    listaEncontrados.append(fossil)
            elif modo == 3:
                if fossil.getCategoria().upper() == pesquisa.upper():
                    listaEncontrados.append(fossil)
        
        if len(listaEncontrados) == 0:
            if modo == 1:
                print(f'Não foi encontrado nenhum fóssil com o ID: {pesquisa}')
            elif modo == 2:
                print(f'Não foi encontrado nenhum fóssil desse dinossauro: {pesquisa}')
            elif modo == 3:
                print(f'Não foi encontrado nenhum fóssil de dinossauro com essa categoria: {pesquisa}')

        else:
            print('Aqui estão os fósseis encontrados: \n')
            for fossil in listaEncontrados:
                print(f'ID: {fossil.getID()}\nDinossauro: {fossil.getDinossauro()}\nCategoria: {fossil.getCategoria()}\nParte do corpo: {fossil.getParte()}\nIdade:{fossil.getIdade()}\n')
                print("      Você chegou ao fim do resultado.")
            
        
