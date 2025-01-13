from pessoa_classe import Pessoa
import random
import string
import funcoes

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, dataNascimento, email, senha):
        super().__init__(nome, cpf, dataNascimento, email, senha)
        self.__identificador = str(random.randint(1000, 9999)) + 2*str(random.choice(string.ascii_uppercase))
    
    def vizualizar_id(self):
        return self.__identificador
    
    def editar_acervo(self):
        item = int(input('\n1- Adicionar novo fóssil ao acervo\n2- Excluir fóssil do acervo\n3- Colocar uma URL para imagem de algum fóssil\nDesejo editar o item: '))
        return item

    def ver_Perfil(self):
        print('SEUS DADOS:')
        print(f'ID: {self.__identificador}\nNome: {self.getnome()}\nCPF: {self.getCPF()}\nData de Nascimento: {self.getdatanascimento()}\nE-mail: {self.getemail()}')

    def acessar_homepage(self, fu_verificado, acervodisp):
        funcoes.limpar()
        if fu_verificado:
            print('Olá, funcionário(a) {}!'.format(self.getnome()))
            funcao = int(input('Você deseja:\n1- Vizualizar acervo\n2- Procurar fóssil\n3- Editar acervo\n4- Visualizar perfil\n5- Entrar com outra conta\n6- Sair\n>  '))
            funcoes.limpar()
            if funcao == 1:
                acervodisp.listar()
                input('\nPress enter para voltar a tela inicial: ')
            elif funcao == 2: 
                modo = 0
                while modo not in (1, 2, 3):
                    modo = int(input('Você deseja encontrar o fóssil\n1-ID do fóssil\n2-Nome do dinossauro\n3-Hábito alimentar do dinossauro\n> '))
                    funcoes.limpar()
                    if modo == 1:
                        pesquisa = input('Digite o ID do fóssil: ')
                    elif modo in (2, 3):
                        pesquisa = input(f'O que você está procurando no modo {modo}?')
                    else:
                        print('Digite um valor correspondente aos citados!')
                acervodisp.encontrar_fossil(pesquisa, modo)
                input('Press enter para voltar a tela inicial: ')

            elif funcao == 3:
                acervodisp.edicao(self.editar_acervo())
            elif funcao == 4:
                self.ver_Perfil() 
                input('\n\nPress enter para voltar a tela inicial: ')   
            elif funcao == 5:
                return True
            elif funcao == 6:
                return False
            else:
                print('Esse valor não está disponível para acesso. Digite um valor válido')
        else:
            print('Crie uma conta ou conecte-se para acessar nosso museu:')
            return True