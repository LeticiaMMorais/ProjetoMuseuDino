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

    def acessar_homepage(self, fu_verificado, acervodisp):
        if fu_verificado:
            funcoes.limpar()
            print('Olá, funcionário!')
            funcao = int(input('Você deseja:\n1- Vizualizar acervo\n2- Procurar fóssil\n3- Editar acervo\n4- Sair\n> '))
            funcoes.limpar()
            if funcao == 1:
                acervodisp.listar()
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
            elif funcao == 3:
                acervodisp.edicao(self.editar_acervo())
            elif funcao == 4:
                return True
            else:
                print('Esse valor não está disponível para acesso. Digite um valor válido')
        else:
            print('Crie uma conta ou conecte-se para acessar nosso museu')