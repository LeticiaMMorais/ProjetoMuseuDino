from visitante_classe import Visitante
from funcionario_classe import Funcionario
from Guia import Guia
from Acervo import Acervo
from Fossil import Fossil

funcionarios = []
visitantes = []

def entrada():
    def signin():
        global funcionarios, visitantes
        situacao = input('Sua conta será de funcionário ou de visitante? ')
        print('Vamos começar seu cadastro! Complete os dados abaixo')
        nome = input('Qual seu nome? ')
        cpf = input('Qual seu CPF? ')
        dataNascimento = input('Qual a sua data de nascimento? ')
        email = input('Qual o seu Email? ')
        senha = input('Crie uma senha: ')
        def verify(situation, email):
            for p in situation:
                if p.getemail() == email:
                    print('Esse email já está cadastrado, tente com outro ou entre na sua conta')
                    return False
                else:
                    return True
        if situacao.lower() == 'visitante':
            if verify(visitantes, email):
                person = Visitante(nome, cpf, dataNascimento, email, senha)
                visitantes.append(person)
        elif situacao.lower() in ('funcionario', 'funcionário'):
            if verify(funcionarios, email):
                person = Funcionario(nome, cpf, dataNascimento, email, senha)
                funcionarios.append(person)
        else:
            print('Parece que você digitou incorretamente. Tente novamente!')
        
    def login(funcionarios, visitantes):
        global vi_verificado, fu_verificado
        print('Olá, vamos fazer seu login?')
        situation = input('Você é visitante ou funcionário? ')
        if situation.lower() == 'visitante':
            email = input('Insira seu email: ')
            for v in visitantes:
                if v.getemail() == email:
                    currentv = v
            senha = input('insira sua senha (Esqueceu a senha? Digite y para muda-la): ')
            if senha.lower() == 'y':    
                currentv.mudarsenha() 
            else:
                if currentv.verificacao(senha):
                    print('Bem-vindo(a) de volta!')
                    vi_verificado = True
                else:
                    print('Senha incorreta!')
                    vi_verificado = False
        elif situation.lower() in ('funcionario', 'funcionário'):
            id = input('Insira seu ID: ')
            for f in funcionarios:
                if f.vizualizar_id() == id:
                    currentf = f
            senha = input('insira sua senha (Esqueceu a senha? Digite y para muda-la): ')
            if senha.lower() == 'y':    
                currentf.mudarsenha() 
            else:
                if currentf.verificacao(senha):
                    print(f'Bem-vindo(a) de volta funcionário {currentf.nome.title()}!')
                    fu_verificado = True
                else:
                    print('Senha incorreta!')
                    fu_verificado = False
            

    start = int(input('Museu Dino\n-1- Sign in\n2- Login\n> '))
    if start == 1:
        signin()
    elif start == 2:
        login(funcionarios, visitantes)
    else:
        print('Escolha uma opção adequada, por favor!')
    



print('    ______   _______   __      __         __      __   __   __   __   ____    _______         ____       _______ ')
print('   |   _  \ |   ____| |  \    /  |       \  \    /  / |__| |  \ |  | |    \  |   _   |       /    \     |   _   |')
print('   |  |_> | |  |____  |   \  /   |  ___   \  \  /  /   __  |   \|  | |  |\ \ |  | |  |      /  /\  \    |  | |  |')
print('   |   _ \  |   ____| |  \ \/ /  | |___|   \  \/  /   |  | |  \ |  | |  | | ||  | |  |     /  /__\  \   |  | |  |')
print('   |  |_> | |  |____  |  |\__/|  |          \    /    |  | |  |\   | |  |_/ /|  |_|  |    /  ______  \  |  |_|  |')
print('   |_____/  |_______| |__|    |__|           \__/     |__| |__| \__| |_____/ |_______|   /__/      \__\ |_______|')
print(' ____        ____                                                       _______      ___    ___     __    __________')
print('|    \      /    |                                                     |       \    |___|  |   \   |  |  |    __    |')
print('|     \    /     |   __      __    _______    _______   __      __     |   |\   \    ___   |    \  |  |  |   |  |   |')
print('|      \  /      |  |  |    |  |  /       |  |   ____| |  |    |  |    |   | \   \  |   |  |     \ |  |  |   |  |   |')
print('|   \   \/   /   |  |  |    |  |  \    ___|  |  |____  |  |    |  |    |   |  |   | |   |  |   \  \|  |  |   |  |   |')
print('|   |\      /|   |  |  |____|  |   _\_   \   |   ____| |  |____|  |    |   | /   /  |   |  |   |\  |  |  |   |__|   |')
print('|   | \____/ |   |  |          |  /       |  |  |____  |          |    |   |/   /   |   |  |   | \    |  |          |')
print('|___|        |___|   \________/   |_______/  |_______|  \________/     |_______/    |___|  |___|  \___|  |__________|')



print('BEM VINDO AO MUSEU DINO')

