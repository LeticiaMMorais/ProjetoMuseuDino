from visitante_classe import Visitante
from funcionario_classe import Funcionario
from Guia import Guia
from Acervo import Acervo
from Fossil import Fossil
import conhecimentossobrefosseis as consf
import os

funcionarios = []
visitantes = []

def limpar():
    os.system('cls' if os.name=='nt' else 'clear')

def entrada():
    global funcionarios, visitantes

    def signin():
        global funcionarios, visitantes
        situacao = ''
        while situacao.lower() not in ['visitante', 'funcionario', 'funcionário']:
            situacao = input('Sua conta será de funcionário ou de visitante? ').strip()
            if situacao.lower() not in ['visitante', 'funcionario', 'funcionário']:
                print('     Valor digitado inválido!')
        limpar()
        
        def verify(situation, email):
            for p in situation:
                if p.getemail() == email:
                    print('   Esse email já está cadastrado, tente com outro ou entre na sua conta')
                    return False
            return True
        
        print('\nVamos começar seu cadastro! Complete os dados abaixo\n')
        nome = input('Qual seu nome? ')
        cpf = input('Qual seu CPF? ')
        dataNascimento = input('Qual a sua data de nascimento? ')
        email = input('Qual o seu Email? ')
        senha = input('Crie uma senha: ')
        limpar()
            
        if situacao.lower() == 'visitante':
            if verify(visitantes, email):
                person = Visitante(nome, cpf, dataNascimento, email, senha)
                visitantes.append(person)
                print('Conta criada com sucesso!')
        elif situacao.lower() in ('funcionario', 'funcionário'):
            if verify(funcionarios, email):
                person = Funcionario(nome, cpf, dataNascimento, email, senha)
                funcionarios.append(person)
                print('Seu ID é: {}'.format(person.vizualizar_id()))
                print('Conta criada com sucesso!')

        
    def login(funcionarios, visitantes):
        global verificado
        print('\nVamos fazer seu login?')
        situation = ''
        while situation.lower() not in ['funcionario', 'funcionário', 'visitante']:
            situation = input('Você é visitante ou funcionário? ')
            if situation.lower() not in ['visitante', 'funcionario', 'funcionário']:
                print('     Valor digitado inválido!')
        limpar()
        if situation.lower() == 'visitante':
            email = input('Insira seu email: ')
            for v in visitantes:
                if v.getemail() == email:
                    currentv = v
            
            senha = input('insira sua senha (Esqueceu a senha? Digite y para muda-la): ')
            limpar()
            if senha.lower() == 'y':
                currentv.mudarsenha()
                verificado = True 
            else:
                if currentv.verificacao(senha):
                    print('Bem-vindo(a) de volta!')
                    verificado = True
                    
                else:
                    print('Senha incorreta!')
                    verificado = False

            return currentv
                    

        elif situation.lower() in ('funcionario', 'funcionário'):
            id = input('Insira seu ID: ')
            for f in funcionarios:
                if f.vizualizar_id() == id:
                    currentf = f
            senha = input('insira sua senha (Esqueceu a senha? Digite y para muda-la): ')
            limpar()
            if senha.lower() == 'y':    
                currentf.mudarsenha()
                verificado = True 
            else:
                if currentf.verificacao(senha):
                    print(f'Bem-vindo(a) de volta funcionário {currentf.getnome().title()}!')
                    verificado = True
                    
                else:
                    print('Senha incorreta!')
                    verificado = False
            return currentf

        else:
            print('Digite um valor válido!')


    start = int(input('Museu Roberto Marino\n1- Criar uma conta\n2- Entrar numa conta existente\n> '))
    limpar()
    if start == 1:
        signin()
        pessoa = login(funcionarios, visitantes)
    elif start == 2:
        pessoa = login(funcionarios, visitantes)
    else:
        print('Escolha uma opção adequada, por favor!')
        entrada()
    return verificado, pessoa

