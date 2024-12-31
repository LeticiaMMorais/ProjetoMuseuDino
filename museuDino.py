from visitante_classe import Visitante
from funcionario_classe import Funcionario
from Guia import Guia
from Acervo import Acervo
from Fossil import Fossil

funcionarios = []
visitantes = []
acervodisp = Acervo()

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
                if currentv.verficacao(senha):
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
                if currentf.verficacao(senha):
                    print(f'Bem-vindo(a) de volta funcionário {currentf.nome.title()}!')
                    fu_verificado = True
                else:
                    print('Senha incorreta!')
                    fu_verificado = False      

    start = int(input('Museu Dino\n-1- Criar conta\n2- Entrar\n> '))
    if start == 1:
        signin()
    elif start == 2:
        login(funcionarios, visitantes)
    else:
        print('Escolha uma opção adequada, por favor!')

def guia():
    pass

def homepage_visi(vi_verificado):
    pass

def homepage_func(fu_verificado, funcionario, acervodisp):
    if fu_verificado:
        print('Olá, funcionário!')
        funcao = int(input('Você deseja:\n1- Vizualizar acervo\n2- Procurar fossíl\n3- Editar acervo\n> '))
        if funcao == 1:
            acervodisp.listar()
        elif funcao == 2: 
            modo = 0
            while modo not in (1, 2, 3):
                modo = int(input('Você deseja encontrar o fossíl\n1-ID do fóssil\n2-Nome do dinossauro\n3-Categoria do dinossauro\n> '))
                if modo == 1:
                    pesquisa = input('Digite o ID do fossíl: ')
                elif modo in (2, 3):
                    pesquisa = input(f'O que você está procurando de {modo}?')
                else:
                    print('Digite um valor correspondente aos citados!')
            acervodisp.encontrar_fossil(pesquisa, modo)
        elif funcao == 3:
            print('1- Adicionar novo fossíl ao acervo\n2- Excluir fóssil do acervo')
            acervodisp.edicao(funcionario.editar_acervo())
        else:
            print('Esse valor não está disponível para acesso. Digite um valor válido')
    else:
        print('Crie uma conta ou conecte-se para acessar nosso museu')

print('BEM VINDO')#aqui vai ficar o bem-vindo e o nome do museu

#logo após será executado as funções