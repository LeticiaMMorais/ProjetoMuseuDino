from pessoa_classe import Pessoa
import random
import string
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, dataNascimento, email, senha):
        super().__init__(nome, cpf, dataNascimento, email, senha)
        self.__identificador = str(random.randint(1000, 9999)) + 2*str(random.choice(string.ascii_uppercase))
    def vizualizar_id(self):
        return self.__identificador
    def editar_acervo(self):
        item = int(input('Desejo editar o item: '))
        return item
    def falar(self):
        espaco = 5*''
        print(f'Você deseja:\n1. Vizualizar acervo {espaco}2. Pesquisar Fóssil {espaco}3. Sobre nossa equipe')
