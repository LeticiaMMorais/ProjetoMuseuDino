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
    
    def ver_perfil(self):
        print(funcoes.negrito+f'SEUS DADOS:{funcoes.fim}\nNome: {self.getnome()}\nCPF: {self.getCPF()}\nData de nascimento: {self.getdatanascimento()}\nE-mail: {self.getemail()}')

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
                        funcoes.limpar()
                        print('\nCerto, então {} lhe acompanhará nesta sessão.\n'.format(guia_esc.getNome()))
                if not encontrado:
                    print(funcoes.vermelho+'     Não foi encontrado nenhum guia com esse nome. Tente novamente:'+funcoes.fim)

            return guia_esc
        

        if vi_verificado: #vi_verificado é para saber se a senha estava correta(True) ou incorreta(False) na hora de entrar.
            funcoes.limpar()
            print('Olá, {}!'.format(self.getnome()))
            funcao = input('Você deseja:\n{0}1-{1} Vizualizar acervo (por conta própria)\n{0}2-{1} Vizualizar acervo com um guia\n{0}3-{1} Conhecer a história do Museu\n{0}4-{1} Procurar fóssil\n{0}5-{1} Sobre a equipe Roberto Marino\n{0}6-{1} Vizualizar perfil\n{0}7-{1} Entrar com outra conta\n{0}8-{1} Sair\n> '.format(funcoes.ciano, funcoes.fim)).strip()
            funcoes.limpar()

            if funcao == '1':
                acervodisp.listar()
                input('\nPress enter para voltar a tela inicial: ')

            elif funcao == '2':
                if self.getGuia() == None:
                    self.setGuia(guia())
                for fossil in acervodisp.getFosseis():
                    print(f'Nome científico do dinossauro: {fossil.getDinossauro()}\nNome popular do dinossauro: {fossil.getDinoPopular()}\nHábito alimentar do dinossauro: {fossil.getCategoria()}\nParte do corpo: {fossil.getParte()}\nIdade: {fossil.getIdade()}')
                    if fossil.getURLimagem() != None:
                        print(f'URL da imagem do fóssil: {fossil.getURLimagem()}')
                    print('\n'+self.getGuia().historiaFossil(fossil))
                    input('\n\nQuando estiver pronto para seguir em frente, press enter.\n')
                    funcoes.limpar()
            
            elif funcao == '3':
                if self.getGuia() == None:
                    self.setGuia(guia())
                print(funcoes.verdeescuro+self.getGuia().getNome()+funcoes.fim,':\n',self.getGuia().historiaMuseu())
                input('\nPress enter para voltar a tela inicial: ')

            elif funcao == '4':
                modo = 0
                while modo not in [1,2,3]:
                    modo = int(input('Você deseja encontrar o fóssil\n{0}1-{1}ID do fóssil\n{0}2-{1}Nome do dinossauro\n{0}3-{1}Hábito alimentar do dinossauro\n> '.format(funcoes.ciano, funcoes.fim)))
                    funcoes.limpar()
                    if modo == 1:
                        pesquisa = input('Digite o ID do fóssil: ')
                    elif modo in (2, 3):
                        pesquisa = input(f'O que você está procurando no modo {modo}?\n> ')
                    else:
                        print(funcoes.vermelho+'Digite um valor correspondente aos citados!'+funcoes.fim)
                acervodisp.encontrar_fossil(pesquisa, modo)
                input('Press enter para voltar a tela inicial: ')

            elif funcao == '5':
                print("Nossa equipe é composta pelas programadoras Angelina Brito e Letícia Morais, que fizeram esse projeto se estender e virar um programa, e pelos nossos queridos funcionários que fazem a administração do museu.")
                input('\nPress enter para voltar a tela inicial: ')
            elif funcao == '6':
                self.ver_perfil()
                input('\nPress enter para voltar a tela inicial: ')
            elif funcao == '7':
                return True
            elif funcao == '8':
                return False
            else:
                print(funcoes.vermelho+'Esse valor não está disponível para acesso. Digite um valor válido'+funcoes.fim, end='\n')
        else:
            print(funcoes.vermelho+'Crie uma conta ou conecte-se para acessar nosso museu'+funcoes.fim)
            return True
