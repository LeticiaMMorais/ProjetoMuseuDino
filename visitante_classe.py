from pessoa_classe import Pessoa
class Visitante(Pessoa):
    def __init__(self, nome, cpf, dataNascimento, email, senha):
        super().__init__(nome, cpf, dataNascimento, email, senha)
    def falar(self):
        print(f'Olá, me chamo {self.nome.title()} vim para conhecer mais sobre dinossauros!')
    def acessar(self):
        item = input(f'Desejo acessar o item: ')
        return item

p1 = Visitante('anna', '111.222.333.43', '12/11/1997', 'annaangeh45@gamil.com', 'lovelove1')
print(p1._email)