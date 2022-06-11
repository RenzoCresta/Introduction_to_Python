#TA-TE-TI!

def drawboard(board):
  """
  Drawboard() recibe una lista de 9 elementos donde
  los elementos de la lista son cruces, círculos, o espacios
  """
  # Dibujamos el 1er renglón
  print(' ', board[0][0], ' | ', board[0][1], ' | ', board[0][2] )
  # Separamos
  print('-----------------')
  # Dibujamos el 2do renglón
  print(' ', board[1][0], ' | ', board[1][1], ' | ', board[1][2] )
  # Separamos
  print('-----------------')
  # Dibujamos el 3er renglón
  print(' ', board[2][0], ' | ', board[2][1], ' | ', board[2][2] )

def winnercheck(board):
  for i in range (0,3):

    # Revisamos columna a columna.
    if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != " ":
      return  board[0][i]

    # Revisamos fila a fila.
    elif board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != " ":
      return  board[i][0]

  # Revisamos la primer diagonal.
  if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " ":
    return  board[1][1]

  # Revisamos la segunda diagonal.
  elif board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[1][1] != " ":
    return  board[1][1]

  return  False

def checkavaliable(board, place):

  # Verificamos que sea una casilla válida
  if place > 9 or place < 1:
    print("Casilla inválida.")
    return False

  # Tomamos las coordenadas de la casilla
  col= (place-1) % 3
  fil= int((place-1) / 3)
  if board[fil][col]==" ":
    return True

  #Si la casilla ya está ocupada: aviso que no es posible colocar la pieza.
  else:
    print("Casilla ocupada.")
    return False

def tiedgame(board):
  pieces = 0
  for i in range(3):
    for j in range(3):        # Por cada casilla
      if board[i][j] != " ":  # si la casilla esta completa
        pieces += 1           # incremento un cont de "fichas"

  # Si todas las casillas estan ocupadas y no hay ganador,
  # aviso que es un empate
  if pieces == 9:
    return True
  else:
    return False

def changeplayer(player):
  if player == "O":
    return "X"
  elif player == "X":
    return "O"


def putpiece(board, place, player):
  row = int((place-1)/3)  # Tomamos coord de la pieza
  col = (place-1) %3
  board[row][col] = player  # Ubicamos la pieza en el tablero.
  return board


#Inicializamos variables
tablero=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
turno="O"

while winnercheck(tablero) == False and tiedgame(tablero) == False:

  print("Turno de " + turno)
  casilla = int(input("Ingrese una casilla (1-9): "))

  # Pido que se ingrese una casilla válida
  while(checkavaliable(tablero, casilla) == False):
    casilla = int(input("Ingrese otra casilla (1-9): "))

  # Colocamos la pieza.
  tablero = putpiece(tablero, casilla, turno)

  # Cambiamos el "dueño del turno"
  turno = changeplayer(turno)

  # Dibujamos el tablero
  drawboard(tablero)

#Indicamos el resultado de la partida
if winnercheck(tablero) == "X" or winnercheck(tablero) == "O":
  print("Ha ganado el jugador " + winnercheck(tablero))
elif tiedgame(tablero):
  print("Partida empatada")
