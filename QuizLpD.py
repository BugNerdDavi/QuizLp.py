from asyncio.base_futures import _FINISHED
from os import system
from time import sleep
system('cls')
print('-' * 30)
print('')
respInicial = str(input('Pressione enter para começar: '))
print('')
print('-' * 30)
if respInicial == '':
    while True:
        system('cls')
        pontos = 0
        print('-' * 42)
        print('')
        print('Quiz: Lingua Portuguesa.')
        print('')
        print('Notas: 0 a 10')
        print('')
        print('-' * 42)
        sleep(5)
        system('cls')
        print('-' * 30)
        print('')
        print('           Iniciando')
        print('')
        print('-' * 30)
        sleep(3)
        system('cls')
        print('-' * 50)
        print('')
        print('A grafia correta é:')
        print('[1] Franceza')
        print('[2] Francesa')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp1 = int(input('Escolha [1, 2]: '))
            if resp1 == 1:
                pontos += 0
                break
            elif resp1 == 2:
                pontos += 1
                break
            else:
                continue 
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('S ou Z? Marque a alternativa que completa corretamente')
        print('a palavra HOLANDE_A:')
        print('[1] S')
        print('[2] Z')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp2 = int(input('Escolha [1, 2]: '))
            if resp2 == 1:
                pontos += 1
                break
            elif resp2 == 2:
                pontos += 0
                break
            else:
                continue
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('X ou CH? Marque a alternativa que completa')
        print('corretamente a palavra FAI_A.')
        print('[1] CH')
        print('[2] X')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp2e = int(input('Escolha [1, 2]: '))
            if resp2e == 1:
                pontos += 0
                break
            elif resp2e == 2:
                pontos += 1
                break
            else:
                continue 
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('O correto é:')
        print('[1] Trouxa')
        print('[2] troucha')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp3 = int(input('Escolha [1, 2]: '))
            if resp3 == 1:
                pontos += 1
                break
            elif resp3 == 2:
                pontos += 0
                break
            else:
                continue
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('Ditongo é o encontro de duas vogais, na mesma sílaba.')
        print('Qual das palavras é um ditongo?:')
        print('[1] Circuito')
        print('[2] Paraguai')
        print('[3] Quieto')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp4 = int(input('Escolha [1, 2, 3]: '))
            if resp4 == 1:
                pontos += 1
                break
            elif resp4 == 2:
                pontos += 0
                break
            elif resp4 == 3:
                pontos += 0
                break
            else:
                continue
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('Tritongo é o encontro de três vogais, na mesma sílaba.')
        print('Qual das palavras é um tritongo?:')
        print('[1] Aguentar')
        print('[2] Triunfo')
        print('[3] Saguâo')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp5 = int(input('Escolha [1, 2, 3]: '))
            if resp5 == 1:
                pontos += 0
                break
            elif resp5 == 2:
                pontos += 0
                break
            elif resp5 == 3:
                pontos += 1
                break
            else:
                continue
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('O agrupamento de consoantes em uma mesma palavra')
        print('é chamado de "encontro consonantal". Nele, ouve-se o som de')
        print('cada uma das consoentes. Qual das palavras')
        print('abaixo é um encontro consonantal')
        print('[1] Palha')
        print('[2] Tigre')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp6 = int(input('Escolha [1, 2]: '))
            if resp6 == 1:
                pontos += 0
                break
            elif resp6 == 2:
                pontos += 1
                break
            else:
                continue
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('O conjunto de duas letras que representam um único')
        print('som é chamado de dígrafo. Qual das palavras')
        print('abaixo é um dígrafo?:')
        print('[1] Prata')
        print('[2] Pássaro')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp7 = int(input('Escolha [1, 2]: '))
            if resp7 == 1:
                pontos += 0
                break
            elif resp7 == 2:
                pontos += 1
                break
            else:
                continue
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('É um dígrafo:')
        print('[1] chato')
        print('[2] absoluto')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp8 = int(input('Escolha [1, 2]: '))
            if resp8 == 1:
                pontos += 1
                break
            elif resp8 == 2:
                pontos += 0
                break
            else:
                continue
        sleep(1)
        system('cls')
        print('-' * 50)
        print('')
        print('É um encontro consonantal:')
        print('[1] Claridade')
        print('[2] Galinha')
        print('')
        print('-' * 50)
        print('')
        while True:
            resp9 = int(input('Escolha [1, 2]: '))
            if resp9 == 1:
                pontos += 1
                break
            elif resp9 == 2:
                pontos += 0
                break
            else:
                continue
        system('cls')
        sleep(1)
        print('-' * 40)
        print('')
        print('Seus pontos:')
        print(pontos)
        print('')
        print('-' * 40)
        sleep(10)
        system('cls')
        print('-' * 40)
        print('')
        while True:
          resp11 = str(input('Deseja Reiniciar o Quiz? [S/N] ')).upper()
          if resp11 == 'S':
              break
          elif resp11 == 'N':
              system('cls')
              break
        if resp11 == 'S':
            continue
        elif resp11 == 'N':
            system('cls')
            break
else:
    print('Finalizando')
    sleep(5)
    system('cls')
