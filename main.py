import funcoes
from visitante_classe import Visitante
from funcionario_classe import Funcionario
from acervoMuseu import acervoDino
import os



print('           ______   _______   __      __         __      __   __   __   __   ____    _______         ____       _______ ')
print('          |   _  \ |   ____| |  \    /  |       \  \    /  / |__| |  \ |  | |    \  |   _   |       /    \     |   _   |')
print('          |  |_> | |  |____  |   \  /   |  ___   \  \  /  /   __  |   \|  | |  |\ \ |  | |  |      /  /\  \    |  | |  |')
print('          |   _ \  |   ____| |  \ \/ /  | |___|   \  \/  /   |  | |  \ |  | |  | | ||  | |  |     /  /__\  \   |  | |  |')
print('          |  |_> | |  |____  |  |\__/|  |          \    /    |  | |  |\   | |  |_/ /|  |_|  |    /  ______  \  |  |_|  |')
print('          |_____/  |_______| |__|    |__|           \__/     |__| |__| \__| |_____/ |_______|   /__/      \__\ |_______|')
print('                               ____        ____                                                  ')
print('                              |    \      /    |                                                 ')
print('                              |     \    /     |   __      __    _______    _______   __      __ ')
print('                              |      \  /      |  |  |    |  |  /       |  |   ____| |  |    |  |')
print('                              |   \   \/   /   |  |  |    |  |  \    ___|  |  |____  |  |    |  |')
print('                              |   |\      /|   |  |  |____|  |   _\_   \   |   ____| |  |____|  |')
print('                              |   | \____/ |   |  |          |  /       |  |  |____  |          |')
print('                              |___|        |___|   \________/   |_______/  |_______|  \________/ ')
print(' ______                                                                   ____        ____')
print('|    _  \                                                                |    \      /    |')
print('|   | \  |   _______   ______   _______   _____    ________   _______    |     \    /     |      ____       _____    __   __   __   _______ ')
print('|   |_/  /  |   _   | |   _  \ |   ____| |   _ \  |__    __| |   _   |   |      \  /      |     /    \     |   _ \  |__| |  \ |  | |   _   |')
print('|       /   |  | |  | |  |_> | |  |____  |  |_> |    |  |    |  | |  |   |   \   \/   /   |    /  /\  \    |  |_> |  __  |   \|  | |  | |  |')
print('|   |\  \   |  | |  | |   _ \  |   ____| |     /     |  |    |  | |  |   |   |\      /|   |   /  /__\  \   |     /  |  | |  \ |  | |  | |  |')
print('|   | \  \  |  |_|  | |  |_> | |  |____  |  |\ \     |  |    |  |_|  |   |   | \____/ |   |  /  ______  \  |  |\ \  |  | |  |\   | |  |_|  |')
print('|___|  \__\ |_______| |_____/  |_______| |__| \_\    |__|    |_______|   |___|        |___| /__/      \__\ |__| \_\ |__| |__| \__| |_______|')
input('\n\nPress enter para seguir: ')
funcoes.limpar()
verificado, person = funcoes.entrada()
continuar = 'S'
while continuar.upper() in ['S', 'SIM']:
    if person.acessar_homepage(verificado, acervoDino):
        verificado, person = funcoes.entrada()


    continuar = input('\n\nVocê quer continuar?\n> ').strip().upper()
    funcoes.limpar()
