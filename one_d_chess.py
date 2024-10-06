"""
Ben Phan
CSC 110
Project - 4
This program has 7 functions in order to create a 1-D chest game. 
"""
def create_board():
  """
  This function returns a list represent the intial state of the board.
  Arg: 
    None
  Return:
    A list of the intial state of the board.     
  """
  create=["WKi", "WKn", "WKn", "EMPTY", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]
  return create

def printable_board(board):
  """
  This function returns graphical representation of the board. 
  Arg: 
    board: the list of the state of the board. 
  Return:
     The graphical representation of the board.    
  """
  new_string = ""
  i = 0
  while i < len (board):
    if board [i] == "EMPTY":
      new_string += "|     "
    else:
      new_string += "| " + board [i] + " " 
    i +=1
  first_line="+-----------------------------------------------------+\n"
  second_line="\n+-----------------------------------------------------+" 
  return first_line + new_string  + "|" + second_line 

def is_valid_move(board,position,player):
  """
  This function returns whether or not a move is valid
  Arg: 
    board: the list of the state of the board. 
    position: an index represents the position of the piece the player want to move. 
    player: the player who control either black pieces or white pieces. 
  Return:
     Whether or not if a move made by the player is valid.     
  """
  if 0 <= position < len (board):
    piece =board[position]
    if player[0]==piece[0]:
        return True
    else:
        return False
  else:
    return False
    
def move_king (board, position, direction):
  """
  This function changes the position of the king on the board. 
  Arg: 
    board: the list of the state of the board. 
    position: an index represents the position of the king the player want to move. 
    direction: the direction in which the king will move.  
  Return:
     The new postion of the king.    
  """
  i = position
  move = True 
  if direction == "LEFT":
    i -= 1
    while 0 <= i < 8 and move == True:
      if board [i] == "EMPTY":
        i -= 1
      else: 
        board [i] = board[position]
        board [position] = "EMPTY"
        move = False
  if direction == "RIGHT":
    i += 1
    while 0 <= i < 8 and move == True:
      if board [i] == "EMPTY":
        i += 1
      else: 
        board [i] = board[position]
        board [position] = "EMPTY"
        move = False
def move_knight (board, position, direction):
  """
  This function changes the position of the knight on the board. 
  Arg: 
    board: the list of the state of the board. 
    position: an index represents the position of the knight the player want to move. 
    direction: the direction in which the knight will move.  
  Return:
     The new postion of the knight.    
     """
  fin_pos = position
  if direction == "LEFT":
    fin_pos -= 2
    if 0 <= fin_pos < len (board):
      board [fin_pos] = board[position]
      board [position] = "EMPTY"
    else:
      board [position] = board [position]
  if direction == "RIGHT":
      fin_pos += 2
      if fin_pos < len (board):
        board [fin_pos] = board [position]
        board [position] = "EMPTY"
      else:
        board [position] = board [position]

def move (board, position, direction):
  """
  This function determines if the king or knight will be moved. 
  Arg: 
    board: the list of the state of the board. 
    position: an index represents the position of the piece the player want to move. 
    direction: the direction in which the piece will move.  
  Return:
     The new position of the moved piece (king or knight).  
    """
  piece = board [position]
  if piece [2] == "i":
    return move_king (board, position, direction)
  else:
    return move_knight (board, position, direction)

def is_game_over (board):
  """
  This function determines if the game is over.
  Arg: 
    board: the list of the state of the board. 
  Return:
    If the game is over or not. 
  """
  if "BKi" not in board:
    return True 
  elif "WKi" not in board:
    return True
  else: 
    return False

def whos_the_winner (board):
  """
  This function determines the winner of the chess game. 
  Arg: 
    board: the list of the state of the board. 
  Return:
     The player who won the chess game. 
"""
  if "WKi" not in board:
    return "Black"
  elif "BKi"not in board:
    return "White"
  else:
    return None
