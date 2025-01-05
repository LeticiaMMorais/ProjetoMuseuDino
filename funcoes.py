from visitante_classe import Visitante
from funcionario_classe import Funcionario
from Guia import Guia
from Acervo import Acervo
from Fossil import Fossil
import conhecimentossobrefosseis as consf

funcionarios = []
visitantes = []

def entrada():
    global funcionarios, visitantes

    def signin():
        global funcionarios, visitantes
        situacao = input('Sua conta será de funcionário ou de visitante? ').strip()
        print('\nVamos começar seu cadastro! Complete os dados abaixo\n')
        nome = input('Qual seu nome? ')
        cpf = input('Qual seu CPF? ')
        dataNascimento = input('Qual a sua data de nascimento? ')
        email = input('Qual o seu Email? ')
        senha = input('Crie uma senha: ')

        def verify(situation, email):
            for p in situation:
                if p.getemail() == email:
                    print('   Esse email já está cadastrado, tente com outro ou entre na sua conta')
                    return False
            return True
                
        if situacao.lower() == 'visitante':
            if verify(visitantes, email):
                person = Visitante(nome, cpf, dataNascimento, email, senha)
                visitantes.append(person)
        elif situacao.lower() in ('funcionario', 'funcionário'):
            if verify(funcionarios, email):
                person = Funcionario(nome, cpf, dataNascimento, email, senha)
                funcionarios.append(person)
                print('Seu ID é: {}'.format(person.vizualizar_id()))
        else:
            print('   Parece que você digitou incorretamente. Tente novamente!')
        
    def login(funcionarios, visitantes):
        global verificado
        print('\nVamos fazer seu login?')
        situation = input('Você é visitante ou funcionário? ')
        if situation.lower() == 'visitante':
            email = input('Insira seu email: ')
            print(visitantes)
            for v in visitantes:
                if v.getemail() == email:
                    currentv = v
            
            senha = input('insira sua senha (Esqueceu a senha? Digite y para muda-la): ')
            if senha.lower() == 'y':    
                currentv.mudarsenha() 
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
            if senha.lower() == 'y':    
                currentf.mudarsenha() 
            else:
                if currentf.verificacao(senha):
                    print(f'Bem-vindo(a) de volta funcionário {currentf.getnome().title()}!')
                    verificado = True
                    
                else:
                    print('Senha incorreta!')
                    verificado = False
            return currentf


    start = int(input('Museu Roberto Marino\n1- Criar uma conta\n2- Entrar numa conta existente\n> '))
    if start == 1:
        signin()
        pessoa = login(funcionarios, visitantes)
    elif start == 2:
        pessoa = login(funcionarios, visitantes)
    else:
        print('Escolha uma opção adequada, por favor!')
        entrada()
    return verificado, pessoa
