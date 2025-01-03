from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, cpf, dataNascimento, email, senha):
        self.nome = nome
        self._cpf = cpf
        self.dataNascimento = dataNascimento
        self._email = email
        self.__senha = senha

    def getnome(self):
        return self.nome
    def getdatanascimento(self):
        return self.dataNascimento
    def getemail(self):
        return self._email
    def __getsenha(self):
        return self.__senha
    def verificacao(self, senha):
        if self.__getsenha == senha:
            return True
        else:
            return False
    def mudarsenha(self):
        esc = input('Digite sua senha antiga (caso não saiba digite 1 para mudar pelo CPF): ')
        if esc != '1':
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
        else:
            cpf_v = input('Digite seu CPF: ')
            if cpf_v == self._cpf:
                nova_senha = input('Digite sua nova senha: ')
                self.__senha = nova_senha
                print('Senha alterada com sucesso!')
            else:
                print('CPF inválido!')
    @abstractmethod
    def falar(self):
        pass
        
        
    
