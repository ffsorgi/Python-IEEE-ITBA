# Desarrollar un juego Ta-Te-Ti en el cual dos usuarios se enfrenten. 
# Por cada turno, un usuario (al que le corresponda) deberá indicar por consola con un número del 1 (casilla superior izquierda) al 9 (casilla inferior derecha) en función de la casilla en que quiere colocar su ficha. 
# El juego termina cuando un jugador coloca 3 fichas en línea o ya no se pueden colocar más fichas. 
# Al finalizar la partida, indicar qué jugador ganó o si hubo empate.

# drawboard() recibe una lista de 9 elementos donde
# los elementos de la lista son cruces, círculos, o espacios

import os
import sys

def drawboard(board):
  print(' ', board[0], ' | ', board[1], ' | ', board[2] ) #Dibujamos el 1er renglón
  print('-----------------')
  print(' ', board[3], ' | ', board[4], ' | ', board[5] ) #Dibujamos el 2do renglón
  print('-----------------')
  print(' ', board[6], ' | ', board[7], ' | ', board[8] ) #Dibujamos el 3er renglón

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def menu(board, player):
    clearConsole()
    drawboard(board)
    print("")
    place = int(input(f"Indique donde quiere colocar su ficha, jugador {player}:"))
    print("")
    while board[place] == "X" or board[place] == "O":
        clearConsole()
        drawboard(board)
        print("")
        place = int(input(f"Espacio ocupado, indique de nuevo el lugar, jugador {player}:"))
        print("")
    if player == 1:
        board[place] = "X"
    else:
        board[place] = "O"

def finishGame(board):

    file = None
    endGame = False

    #Filas
    if board[0] == board[1] == board[2]:
        file = board[0]
    if board[3] == board[4] == board[5]:
        file = board[3]
    if board[6] == board[7] == board[8]:
        file = board[6]

    #Diagonales
    if board[0] == board[4] == board[8]:
        file = board[0]
    if board[2] == board[4] == board[6]:
        file = board[2]

    #Columnas
    if board[0] == board[3] == board[6]:
        file = board[0]
    if board[1] == board[4] == board[7]:
        file = board[1]
    if board[2] == board[5] == board[8]:
        file = board[2]

    if file:
        endGame = True
        if file == "X":
            sys.exit("El ganador es el jugador 1.")
        elif file == "O":
            sys.exit("El ganador es el jugador 2.")

    return endGame

def game():
    turno = 0
    board = [0,1,2,3,4,5,6,7,8]

    while turno < 8:
        
        if not finishGame(board):
            menu(board, 1)

        turno += 1

        if not finishGame(board):
            menu(board, 2)

        turno += 1

    if not finishGame(board):
        menu(board,1)
    if not finishGame(board):
        print("Empate.")

game()