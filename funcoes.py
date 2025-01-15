from visitante_classe import Visitante
from funcionario_classe import Funcionario
from Guia import Guia
from Acervo import Acervo
from Fossil import Fossil
import conhecimentossobrefosseis as consf
import os

verde = '\033[1;92m'
azulclaro = '\033[1;94m'
verdeescuro = '\033[1;49;32m'
ciano = '\033[1;96m'
vermelho = '\033[1;91m'
amarelo = '\033[1;93m'
fim = '\033[m'
negrito = '\033[7;30m'

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
                print(vermelho+'     Valor digitado inválido!'+fim)
        limpar()
        
        def verify(situation, email):
            for p in situation:
                if p.getemail() == email:
                    print(vermelho+'   Esse email já está cadastrado, tente com outro ou entre na sua conta'+fim)
                    return False
            return True
        
        print(azulclaro+'\nVamos começar seu cadastro! Complete os dados abaixo\n'+fim)
        nome = input('Qual seu nome? ')
        cpf = input('Qual seu CPF? ')
        dataNascimento = input('Qual a sua data de nascimento? ')
        email = input('Qual o seu e-mail? ')
        senha = input('Crie uma senha: ')
        limpar()
            
        if situacao.lower() == 'visitante':
            if verify(visitantes, email):
                person = Visitante(nome, cpf, dataNascimento, email, senha)
                visitantes.append(person)
                print(verde+'Conta criada com sucesso!'+fim)
        elif situacao.lower() in ('funcionario', 'funcionário'):
            if verify(funcionarios, email):
                person = Funcionario(nome, cpf, dataNascimento, email, senha)
                funcionarios.append(person)
                print(amarelo+'Seu ID é: {}'.format(person.vizualizar_id())+fim)
                print(verde+'Conta criada com sucesso!'+fim)

        
    def login(funcionarios, visitantes):
        global verificado
        print(azulclaro+'\nVamos fazer seu login?'+fim)
        situation = ''
        while situation.lower() not in ['funcionario', 'funcionário', 'visitante']:
            situation = input('Você é visitante ou funcionário? ')
            if situation.lower() not in ['visitante', 'funcionario', 'funcionário']:
                print(vermelho+'     Valor digitado inválido!'+fim)
        limpar()
        if situation.lower() == 'visitante':
            encontrado = False
            while not encontrado:
                email = input('Insira seu email: ')
                for v in visitantes:
                    if v.getemail() == email:
                        currentv = v
                        encontrado = True
                print(vermelho+'    Esse e-mail não foi encontrado.\n' if not encontrado else '\n' +fim)
            
            senha = input('Insira sua senha (Esqueceu a senha? Digite y para muda-la): ')
            limpar()
            if senha.lower() == 'y':
                currentv.mudarsenha()
                verificado = True 
            else:
                if currentv.verificacao(senha):
                    print(verde+'Bem-vindo(a) de volta!'+fim)
                    verificado = True
                    
                else:
                    print(vermelho+'Senha incorreta!'+fim)
                    verificado = False

            return currentv
                    

        elif situation.lower() in ('funcionario', 'funcionário'):
            encontrado = False
            while not encontrado:
                id = input('Insira seu ID: ')
                for f in funcionarios:
                    if f.vizualizar_id() == id: 
                        currentf = f
                        encontrado = True
                print(vermelho+ '    Esse ID não foi encontrado.\n' if not encontrado else '\n' +fim)  
            senha = input('Insira sua senha (Esqueceu a senha? Digite y para muda-la): ')
            limpar()
            if senha.lower() == 'y':    
                currentf.mudarsenha()
                verificado = True 
            else:
                if currentf.verificacao(senha):
                    print(verde+f'Bem-vindo(a) de volta funcionário {currentf.getnome().title()}!'+fim)
                    verificado = True
                    
                else:
                    print(vermelho+ 'Senha incorreta!' +fim)
                    verificado = False
            return currentf

        else:
            print(vermelho+ 'Digite um valor válido!' +fim)


    start = int(input(ciano+ 'Museu Roberto Marino' +fim+ '\n1- Criar uma conta\n2- Entrar numa conta existente\n> '))
    limpar()
    if start == 1:
        signin()
        pessoa = login(funcionarios, visitantes)
    elif start == 2:
        pessoa = login(funcionarios, visitantes)
    else:
        print(vermelho+ 'Escolha uma opção adequada, por favor!' +fim)
        entrada()
    return verificado, pessoa

