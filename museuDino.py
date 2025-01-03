from visitante_classe import Visitante
from funcionario_classe import Funcionario
from Guia import Guia
from Acervo import Acervo
from Fossil import Fossil
import conhecimentossobrefosseis as consf

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

def guia():
    #Instanciando os objetos de Guia primeiro:
    guias_disp = []
    jenny = Guia('Jenny','Feminino','Oii! Você ama os dinossauros tanto quanto eu? Vamos ver, hehehe.', consf.conhecimentosobrefosseis)
    ruan = Guia('Ruan', 'Masculino','Olá! Precisa de ajuda? Não se preocupe, pode contar comigo.', consf.conhecimentosobrefosseis)
    guias_disp.extend([jenny,ruan])

    #Agora sim é hora de por o visitante para escolher.
    print('\nTemos os seguintes guias disponíveis:')
    for guia_escolher in guias_disp:
        print('\nNome: {}\nGênero: {}\n{}'.format(guia_escolher.getNome(), guia_escolher.getGenero(), guia_escolher.descricao))
    
    encontrado = False
    while not encontrado:
        escolhido = input('\nQual deles você quer que te acompanhe? (Insira o nome dele/a)\n> ').strip()
        for guia_escolher in guias_disp:
            if guia_escolher.getNome() == escolhido.title():
                guia_esc = guia_escolher
                encontrado = True
                print('Certo, então {} lhe acompanhará nesta sessão.'.format(guia_esc.getNome()))
        if not encontrado:
            print('     Não foi encontrado nenhum guia com esse nome. Tente novamente:')

    return guia_esc

def homepage_visi(vi_verificado, visitante, acervodisp):
    if vi_verificado:
        visitante.falar()
        print('Olá, {}!'.format(visitante.getnome().title()))
        funcao = int(input('Você deseja:\n1- Vizualizar acervo (por conta própria)\n2- Vizualizar acervo com um guia\n3- Conhecer a história do Museu\n4- Procurar fóssil\n5- Sobre a equipe Roberto Marino\n> '))
        guiaEscolhido = False

        if funcao == 1:
            acervodisp.listar()

        elif funcao == 2:
            if not guiaEscolhido:
                guia_esc = guia()
            guiaEscolhido = True #aqui o visitante já escolheu o guia dele
            for fossil in acervodisp.getFosseis():
                print(f'Nome do dinossauro: {fossil.getDinossauro()}\nHábito alimentar do dinossauro: {fossil.getCategoria()}\nParte do corpo: {fossil.getParte()}\nIdade:{fossil.getIdade()}\n')
                print(guia_esc.historiaFossil(fossil))
                input('\n\nQuando estiver pronto para seguir em frente, press enter.\n')
        
        elif funcao == 3:
            if not guiaEscolhido:
                guia_esc = guia()
            print(guia.getNome(),':\n',guia_esc.historiaMuseu())

        elif funcao == 4:
            modo = 0
            while modo not in [1,2,3]:
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
    else:
        print('Crie uma conta ou conecte-se para acessar nosso museu')

            


def homepage_func(fu_verificado, funcionario, acervodisp):
    if fu_verificado:
        print('Olá, funcionário!')
        funcao = int(input('Você deseja:\n1- Vizualizar acervo\n2- Procurar fóssil\n3- Editar acervo\n> '))
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
        elif funcao == 3:
            print('1- Adicionar novo fóssil ao acervo\n2- Excluir fóssil do acervo')
            acervodisp.edicao(funcionario.editar_acervo())
        else:
            print('Esse valor não está disponível para acesso. Digite um valor válido')
    else:
        print('Crie uma conta ou conecte-se para acessar nosso museu')
