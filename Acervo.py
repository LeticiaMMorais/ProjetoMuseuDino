from Fossil import Fossil
from conhecimentossobrefosseis import conhecimentosobrefosseis as dictconhecimento
import random

class Acervo:
    def __init__(self, fosseis:list=[]):
        self.__fosseis = fosseis


    def getFosseis(self):
        return self.__fosseis
    

    def __adicionar_fossil(self, dinossauro:str,nomePop:str,categoria:str, parte:str, idade:int, historia:str, urlImagem:str=None):
        novoID = dinossauro[:2].upper()
        while len(novoID)<=3:
            num = random.randint(100000,999999)
            igual = False
            for fossil in self.__fosseis:
                if fossil.getID() == novoID + str(num):
                    igual = True
            if not igual:
                novoID += str(num)
        
        novoFossil = Fossil(novoID, dinossauro, nomePop, categoria, parte, idade, urlImagem)
        dictconhecimento[novoFossil.getID()] = historia
        self.__fosseis.append(novoFossil)
        print('Fóssil adicionado no acervo!')


    def __excluir_fossil(self,id:str):
        encontrado = False
        for fossil in self.__fosseis:
            if fossil.getID() == id.upper():
                encontrado = True
                self.__fosseis.remove(fossil)
                dictconhecimento.pop(fossil.getID())
                print(f'O seguinte fóssil foi excluído:\nID:{fossil.getID()}\nDinossauro:{fossil.getDinossauro()}\nCategoria:{fossil.getCategoria()}\nParte:{fossil.getParte()}\nIdade:{fossil.getIdade()}')
        if not encontrado:
            print('Nenhum fóssil com esse ID foi encontrado em nosso acervo.')

        input('Press enter para voltar a tela inicial: ')


    def edicao(self,edit:int):
        if edit == 1:
            nomeDino = input('Digite o nome científico do dinossauro a que pertence o fóssil: ')
            nomePopDino = input('Agora a forma que ele é geralmente chamado pelas pessoas: ')
            categoria = input('Digite o tipo da alimentação do dinossauro (Herbivoro, Carnivoro ou Onivoro): ')
            parteDino = input('Digite a parte do corpo do dinossauro a que se refere o fóssil: ')
            idadeFossil = input('Informe a idade do fóssil: ')
            historia = input('Qual a história do fóssil?\n> ')
            url = input('Informe a URL da imagem (se quiser adicionar só depois, digite D):\n> ').strip()

            if url.upper() =='D':
                self.__adicionar_fossil(nomeDino,nomePopDino,categoria,parteDino,idadeFossil, historia)
            else:
                self.__adicionar_fossil(nomeDino,nomePopDino,categoria,parteDino,idadeFossil, historia, url)

        elif edit == 2:
                id_dinossauro = input('\nCerto, digite o ID do dinossauro que quer excluir: ')
                self.__excluir_fossil(id_dinossauro)

        elif edit == 3:
            pesquisa = input('Informe o ID do fóssil que vai adicionar a URL da imagem: ')
            encontrado = False
            for fossil in self.__fosseis:
                if fossil.getID() == pesquisa:
                    print('Foi encontrado o fóssil:\n')
                    print(f'ID: {fossil.getID()}\nNome científico do dinossauro: {fossil.getDinossauro()}\nHábito alimentar do dinossauro: {fossil.getCategoria()}\nParte do corpo: {fossil.getParte()}\nIdade:{fossil.getIdade()}')
                    if fossil.getURLimagem() != None:
                        print('URL para imagem do fóssil: {}'.format(fossil.getURLimagem()))

                    querIr = input('\nQuer mesmo alterar ou adicionar uma URL no registro desse fóssil? ').strip().upper()
                    if querIr in ['S', 'SIM']:
                        fossil.setURLimagem(input('\nInforme a nova URL: '))
                        encontrado = True
                        break
            if not encontrado:
                print('      Não foi encontrado nenhum fóssil com esse ID.')
                    

        else:
            print('Só há três opções: 1 para adicionar e 2 para excluir algum fóssil, 3 para adicionar uma URL de imagem a um fóssil já existente.')


    def listar(self):
        print('Aqui estão os fósseis do nosso acervo: \n')
        for fossil in self.__fosseis:
            print(f'ID: {fossil.getID()}\nNome científico do dinossauro: {fossil.getDinossauro()}\nHábito alimentar do dinossauro: {fossil.getCategoria()}\nParte do corpo: {fossil.getParte()}\nIdade:{fossil.getIdade()}')
            if fossil.getURLimagem() != None:
                print('URL para imagem do fóssil: {}'.format(fossil.getURLimagem()))
            print()
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
                elif fossil.getDinoPopular().upper() == pesquisa.upper():
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
                print(f'ID: {fossil.getID()}\nNome científico do dinossauro: {fossil.getDinossauro()}\nHábito alimentar do dinossauro: {fossil.getCategoria()}\nParte do corpo: {fossil.getParte()}\nIdade:{fossil.getIdade()}')
                if fossil.getURLimagem() != None:
                    print('URL para imagem do fóssil: {}'.format(fossil.getURLimagem()))
                print()
            print("      Você chegou ao fim do resultado.")
            
        
