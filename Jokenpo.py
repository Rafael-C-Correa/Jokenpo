import funex
from random import choice

# VARIÁVEIS

player_pts = 0
computer_pts = 0
both_pts = 0
pc_choice = 0
jog_choice = 0
ped = 'PEDRA'
pap = 'PAPEL'
tes = 'TESOURA'

# ESCOLHA DO PC

def pc():
    global pc_choice
    pc_choice = choice([ped, pap, tes])

# ESCOLHA DO JOGADOR

def player():
    global jog_choice
    jog_choice = int(input(f'''[1] - Pedra
[2] - Papel
[3] - Tesoura
Sua jogada: '''))
    if jog_choice == 1:
        jog_choice = ped
    elif jog_choice == 2:
        jog_choice = pap
    elif jog_choice == 3:
        jog_choice = tes
    else:
        print('Só é possível escolher Pedra, Papel ou Tesoura.')
        player()

# QUEM SERA VENCEDOR E SOMA DE PONTOS

def winner():
    global player_pts
    global computer_pts
    global both_pts
    pc_escolha = pc_choice
    jog_escolha = jog_choice
    print('=-' * 12)
    funex.jokenpo()
    print(f'''{'=-' * 12}
Você Escolheu: {jog_escolha}
O PC Escohlheu: {pc_escolha}
{'=-' * 12}''')
    if (pc_escolha == ped and jog_escolha == pap) or (pc_escolha == pap and jog_escolha == tes) \
        or (pc_escolha == tes and jog_escolha == ped):
        player_pts += 1
        print(f'{" "*8}VITÓRIA{" "*8}')
    elif (jog_escolha == ped and pc_escolha == pap) or (jog_escolha == pap and pc_escolha == tes) \
        or (jog_escolha == tes and pc_escolha == ped):
        computer_pts += 1
        print(f'{" "*8}DERROTA{" "*8}')
    elif pc_escolha == jog_escolha:
        both_pts += 1
        print(f'{" "*8}EMPATE{" "*8}')
    print(f'''{'=-' * 12}''')

# Revanche
def revanche():
    global player_pts
    global computer_pts
    global both_pts
    rev = int(input('''Jogar novamente? 
[1] SIM
[2] NÃO
Escolha: '''))
    if rev == 1:
        main()
    else:
        print(f'''{'=-' * 12}
Total de partidas: {player_pts + computer_pts + both_pts}
Vitórias: {player_pts}
Derrotas: {computer_pts}
Empates: {both_pts}
{'=-' * 12}
OBRIGADO POR JOGAR''')

def main():
    funex.cabecario_jokenpo('JOKENPO')
    pc()
    player()
    winner()
    revanche()
main()
