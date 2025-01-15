import funcoes
from visitante_classe import Visitante
from funcionario_classe import Funcionario
from acervoMuseu import acervoDino


apresentacao = ['           ______   _______   __      __         __      __   __   __   __   ____    _______         ____       _______ ',
'          |   _  \ |   ____| |  \    /  |       \  \    /  / |__| |  \ |  | |    \  |   _   |       /    \     |   _   |',
'          |  |_> | |  |____  |   \  /   |  ___   \  \  /  /   __  |   \|  | |  |\ \ |  | |  |      /  /\  \    |  | |  |',
'          |   _ \  |   ____| |  \ \/ /  | |___|   \  \/  /   |  | |  \ |  | |  | | ||  | |  |     /  /__\  \   |  | |  |',
'          |  |_> | |  |____  |  |\__/|  |          \    /    |  | |  |\   | |  |_/ /|  |_|  |    /  ______  \  |  |_|  |',
'          |_____/  |_______| |__|    |__|           \__/     |__| |__| \__| |_____/ |_______|   /__/      \__\ |_______|',
'                               ____        ____                                                  ',
'                              |    \      /    |                                                 ',
'                              |     \    /     |   __      __    _______    _______   __      __ ',
'                              |      \  /      |  |  |    |  |  /       |  |   ____| |  |    |  |',
'                              |   \   \/   /   |  |  |    |  |  \    ___|  |  |____  |  |    |  |',
'                              |   |\      /|   |  |  |____|  |   _\_   \   |   ____| |  |____|  |',
'                              |   | \____/ |   |  |          |  /       |  |  |____  |          |',
'                              |___|        |___|   \________/   |_______/  |_______|  \________/ ',
' ______                                                                   ____        ____',
'|    _  \                                                                |    \      /    |',
'|   | \  |   _______   ______   _______   _____    ________   _______    |     \    /     |      ____       _____    __   __   __   _______ ',
'|   |_/  /  |   _   | |   _  \ |   ____| |   _ \  |__    __| |   _   |   |      \  /      |     /    \     |   _ \  |__| |  \ |  | |   _   |',
'|       /   |  | |  | |  |_> | |  |____  |  |_> |    |  |    |  | |  |   |   \   \/   /   |    /  /\  \    |  |_> |  __  |   \|  | |  | |  |',
'|   |\  \   |  | |  | |   _ \  |   ____| |     /     |  |    |  | |  |   |   |\      /|   |   /  /__\  \   |     /  |  | |  \ |  | |  | |  |',
'|   | \  \  |  |_|  | |  |_> | |  |____  |  |\ \     |  |    |  |_|  |   |   | \____/ |   |  /  ______  \  |  |\ \  |  | |  |\   | |  |_|  |',
'|___|  \__\ |_______| |_____/  |_______| |__| \_\    |__|    |_______|   |___|        |___| /__/      \__\ |__| \_\ |__| |__| \__| |_______|']
cores = [funcoes.verdeescuro, funcoes.verde, funcoes.amarelo, funcoes.azulclaro, funcoes.ciano]
seq = 0
for p in apresentacao:
    print(cores[seq]+p+funcoes.fim)
    seq+=1
    if seq == len(cores):
        seq = 0
input('\n\nPress enter para seguir: ')
funcoes.limpar()
verificado, person = funcoes.entrada()
continuar = 'S'
while continuar.upper() in ['S', 'SIM']:
    confirmar = person.acessar_homepage(verificado, acervoDino)
    if confirmar == None:
        pass
    elif confirmar:
        verificado, person = funcoes.entrada()
        funcoes.limpar()
    elif not confirmar:
        continuar = 'N'
    
    
