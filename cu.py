from time import sleep
from random import randint

layout = [
   [' ', ' ',' '],
   [' ', ' ',' '],
   [' ', ' ',' ']
]

Jogador = 'x'

cont_jogadas = 0

for lin in layout:
    for col in lin:
        print(f'|{col}', end='')
    print('|')


