# -*- coding: utf-8 -*-
def tablero(A):                                     
    """Dibuja un tablero de Ta-Te-Ti con
    los valores de la matriz A. Precondición:
    A es una matriz 3x3
    """
    print('',A[0][0],A[0][1],A[0][2],sep='│',end='│\n')
    print('',A[1][0],A[1][1],A[1][2],sep='│',end='│\n')
    print('',A[2][0],A[2][1],A[2][2],sep='│',end='│\n')


def posicion(A,numero,valor):
    """Define si la posicion @numero en la matriz @A es válida y si está ocupada. En caso de estarlo, pide otra posicion.
       Si es válida y está libre, agrega el @valor a la posicion @numero.
    """
    posiciones = [
    [7,8,9],
    [4,5,6],
    [1,2,3]
    ]
    numvalidos = [1,2,3,4,5,6,7,8,9]
    inic = True
    while inic == True:
        if numero not in numvalidos:
            print('La posición no es válida.')
            numero = int(input('Seleccione otra posición'))
            continue
        for x in range(0,3) :
            for y in range(0,3) :
                if posiciones[x][y] == numero and A[x][y] == '_':
                    A[x][y] = valor
                    inic = False
                    continue
                elif posiciones[x][y] == numero and A[x][y] != '_':
                    print('La posición está ocupada')
                    numero = int(input('Seleccione otra posición'))
    return tablero(A)


def partida_terminada(A):
    """Busca si en la matriz @A se presentan las condiciones de partida ganada o de empate. Devuelve True en caso de ser así
        Devuelve False en caso de no haber terminado la partida.
    """
    contador = 0
    for x in range(0,3):
        contador = A[x].count('_')
    
    for x in range(0,3):                                        
        if A[x] == ['X','X','X']:
            print('Partida terminada. Ganó la X!')
            return True
        elif A[x] == ['O','O','O']:
            print('Partida terminada. Ganó la O!')
            return True
        elif A[0][x] == A[1][x] == A[2][x] == 'X':            
            print('Partida terminada. Ganó la X!')
            return True
        elif A[0][x] == A[1][x] == A[2][x] == 'O':
            print('Partida terminada. Ganó la O!')
            return True
        elif A[0][0] == A[1][1] == A[2][2] == 'X' or A[2][0] == A[1][1] == A[0][2] == 'X':              
            print('Partida terminada. Ganó la X!')
            return True
        elif A[0][0] == A[1][1] == A[2][2] == 'O' or A[2][0] == A[1][1] == A[0][2] == 'O':
            print('Partida terminada. Ganó la O')
            return True
        elif contador == 0:
            print('Partida terminada. Hay empate!')
        else:
            return False







#Mensaje inicial
print('Bienvenido a jugar a Ta-Te-Ti!')
a = input('Elija O ó X para jugar.')
iniciador = 1
while iniciador == 1 :                              
    if a.upper() == 'X' or a.upper() == 'O':
        jugador1 = 'X'
        jugador2 = 'O'
        iniciador = 0
    else:
        print('La entrada no es válida')
        a = input('Elija O ó X para jugar.')

print('Estamos listos para jugar!\n','Las posiciones del tablero son las siguientes:', sep='')
posiciones = [
    [7,8,9],
    [4,5,6],
    [1,2,3]
]
tablero(posiciones)                                


jugada = [                                         
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

print('El tablero está vacío')
tablero(jugada)

finalizar_partida = False
turno = 1
while finalizar_partida == False:
    if turno == 1:
        print('Es el turno del jugador', jugador1)
        lugar = int(input('Seleccione la posición a ocupar'))
        posicion(jugada,lugar,jugador1)
        finalizar_partida = partida_terminada(jugada)
        turno = 2
    if turno == 2:
        print('Es el turno del jugador', jugador2)
        lugar = int(input('Seleccione la posición a ocupar'))
        posicion(jugada,lugar,jugador2)
        finalizar_partida = partida_terminada(jugada)
        turno = 1
