from random import randint
from time import sleep


while True:
    com = randint(1,3)
    pes = int(input('''Escolha uma opcao para se jogar: 

    [1] Pedra
    [2] Papel
    [3] Tesoura
 
    Digite sua escolha: '''))
    if com == 1:
        print('Computador escolheu Pedra')
    if com == 2:
        print('Computador escolheu Papel')
    if com == 3:
        print('Computador escolheu Tesoura')

    if pes == 1:
        print('Jogador escolheu Pedra')
    if pes == 2:
        print('Jogador escolheu Papel')
    if pes == 3:
        print('Jogador escolheu Tesoura')

    nome = str('JOCKENPô\n')
    for i in nome:
        sleep(0.5)
        print(i, end=' ')
         
        


    if (com == 1 and pes == 1 or com == 2 and pes == 2 or com == 3 and pes ==3):
        print('Empate')
        break
        
    if (com == 1 and pes == 2 or com == 2 and pes == 3 or com == 3 and pes == 1):
        print( 'Jogador Venceu!')
        break
        
    if (com == 3 and pes == 2 or com == 1 and pes == 3 or com ==2 and pes == 1):
        print('Computador Venceu!')
        break
    

