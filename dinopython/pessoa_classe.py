class Pessoa():
    def __init__(self, nome, cpf, dataNascimento, email, senha):
        self.__nome = nome.title()
        self._cpf = cpf
        self.__dataNascimento = dataNascimento
        self._email = email
        self.__senha = senha

    def getnome(self):
        return self.__nome
    def getCPF(self):
        return self._cpf
    def getdatanascimento(self):
        return self.__dataNascimento
    def getemail(self):
        return self._email
    def __getsenha(self):
        return self.__senha
    def verificacao(self, senha):
        if self.__getsenha() == senha:
            return True
        else:
            return False
    def mudarsenha(self):
        esc = ''
        while esc not in [self.__getsenha(), '1']:
            esc = input('Digite sua senha antiga (caso não saiba digite 1 para mudar pelo CPF): ')
            if esc not in [self.__getsenha(), '1']:
                print('Digite um valor válido!')
        if esc == self.__getsenha():
            senha_antiga = esc
            if senha_antiga == self.__getsenha():
                while True:
                    nova_senha = input('Digite sua nova senha: ')
                    if nova_senha != senha_antiga:
                        self.__senha = nova_senha
                        print('Senha alterada com sucesso!')
                        break
                    else:
                        print('Digite novamente uma senha que não seja a mesma que sua antiga!')
            else:
                print('Senha incorreta')
        elif esc == '1':
            cpf_v = ''
            while cpf_v != self._cpf:
                cpf_v = input('Digite seu CPF: ')
                if cpf_v == self._cpf:
                    nova_senha = input('Digite sua nova senha: ')
                    self.__senha = nova_senha
                    print('   Senha alterada com sucesso!')
                else:
                    print('   CPF inválido!')

    def acessar_homepage(self, acervodisp):
        print('Olá, {}!'.format(self.__nome))
        funcao = int(input('Você deseja:\n1- Vizualizar acervo\n2- Procurar fóssil\n> '))
        if funcao == 1:
            acervodisp.listar()
        elif funcao == 2: 
            modo = 0
            while modo not in (1, 2, 3):
                modo = int(input('Você deseja encontrar o fóssil\n1-ID do fóssil\n2-Nome do dinossauro\n3-Hábito alimentar do dinossauro\n> '))
                if modo == 1:
                    pesquisa = input('Digite o ID do fóssil: ')
                elif modo in (2, 3):
                    pesquisa = input(f'O que você está procurando no modo {modo}?')
                else:
                    print('Digite um valor correspondente aos citados!')
            acervodisp.encontrar_fossil(pesquisa, modo)
        else:
            print('Esse valor não está disponível para acesso. Digite um valor válido')
        
        
