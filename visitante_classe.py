from pessoa_classe import Pessoa
class Visitante(Pessoa):
    def __init__(self, nome, cpf, dataNascimento, email, senha):
        super().__init__(nome, cpf, dataNascimento, email, senha)
    def falar(self):
        print(f'Olá, me chamo {self.nome.title()} e vim para conhecer mais sobre dinossauros!')
    def acessar(self):
        item = input(f'Desejo acessar o item: ')
        return item

