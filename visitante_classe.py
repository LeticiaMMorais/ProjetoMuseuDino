from pessoa_classe import Pessoa
import conhecimentossobrefosseis as consf
from Guia import Guia
import funcoes

class Visitante(Pessoa):
    def __init__(self, nome, cpf, dataNascimento, email, senha):
        super().__init__(nome, cpf, dataNascimento, email, senha)
        self.__guia = None

    def setGuia(self,guianovo):
        self.__guia = guianovo

    def getGuia(self):
        return self.__guia

    def acessar_homepage(self, vi_verificado, acervodisp):
        def guia():
            #Instanciando os objetos de Guia primeiro:
            guias_disp = []
            jenny = Guia('Jenny','Feminino','Oii! Você ama os dinossauros tanto quanto eu? Vamos ver, hehehe.', consf.conhecimentosobrefosseis)
            ruan = Guia('Ruan', 'Masculino','Olá! Precisa de ajuda? Não se preocupe, pode contar comigo.', consf.conhecimentosobrefosseis)
            guias_disp.extend([jenny,ruan])

            #Agora sim é hora de por o visitante para escolher.
            print('\nTemos os seguintes guias disponíveis:')
            for guia_escolher in guias_disp:
                print('\nNome: {}\nGênero: {}\n{}'.format(guia_escolher.getNome(), guia_escolher.getGenero(), guia_escolher.descricao))
            
            encontrado = False
            while not encontrado:
                escolhido = input('\nQual deles você quer que te acompanhe? (Insira o nome dele/a)\n> ').strip()
                for guia_escolher in guias_disp:
                    if guia_escolher.getNome() == escolhido.title():
                        guia_esc = guia_escolher
                        encontrado = True
                        print('Certo, então {} lhe acompanhará nesta sessão.'.format(guia_esc.getNome()))
                if not encontrado:
                    print('     Não foi encontrado nenhum guia com esse nome. Tente novamente:')

            return guia_esc
        

        if vi_verificado: #vi_verificado é para saber se a senha estava correta(True) ou incorreta(False) na hora de entrar.
            funcoes.limpar()
            print('Olá, {}!'.format(self.getnome()))
            funcao = int(input('Você deseja:\n1- Vizualizar acervo (por conta própria)\n2- Vizualizar acervo com um guia\n3- Conhecer a história do Museu\n4- Procurar fóssil\n5- Sobre a equipe Roberto Marino\n6- Sair\n> '))
            funcoes.limpar()

            if funcao == 1:
                acervodisp.listar()

            elif funcao == 2:
                if self.getGuia() == None:
                    self.setGuia(guia())
                for fossil in acervodisp.getFosseis():
                    print(f'Nome científico do dinossauro: {fossil.getDinossauro()}\nNome popular do dinossauro: {fossil.getDinoPopular()}\nHábito alimentar do dinossauro: {fossil.getCategoria()}\nParte do corpo: {fossil.getParte()}\nIdade:{fossil.getIdade()}')
                    if fossil.getURLimagem() != None:
                        print('URL da imagem do fóssil: {fossil.getURLimagem()}')
                    print('\n'+self.getGuia().historiaFossil(fossil))
                    input('\n\nQuando estiver pronto para seguir em frente, press enter.\n')
            
            elif funcao == 3:
                if self.getGuia() == None:
                    self.setGuia(guia())
                print(self.getGuia().getNome(),':\n',self.getGuia().historiaMuseu())

            elif funcao == 4:
                modo = 0
                while modo not in [1,2,3]:
                    modo = int(input('Você deseja encontrar o fóssil\n1-ID do fóssil\n2-Nome do dinossauro\n3-Hábito alimentar do dinossauro\n> '))
                    if modo == 1:
                        pesquisa = input('Digite o ID do fóssil: ')
                    elif modo in (2, 3):
                        pesquisa = input(f'O que você está procurando no modo {modo}?\n> ')
                    else:
                        print('Digite um valor correspondente aos citados!')
                acervodisp.encontrar_fossil(pesquisa, modo)

            elif funcao == 5:
                print("Nossa equipe é composta pelas programadoras Angelina Brito e Letícia Morais, que fizeram esse projeto se estender e virar um programa e pelos nossos queridos funcionários que fazem a administração do museu.")
            elif funcao == 6:
                return True
            else:
                print('Esse valor não está disponível para acesso. Digite um valor válido')
        else:
            print('Crie uma conta ou conecte-se para acessar nosso museu')

