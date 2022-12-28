def draw_board(board):
  for row in board:
    print(" ".join(row))

def get_move(player, board):
  while True:
    print(f"{player}'s turn. Enter a move (e.g. e2 e4):")
    move = input()
    if is_valid_move(move, player, board):
      return move
    print("Invalid move, try again.")

def is_valid_move(move, player, board):
  # Check if the move is in the correct format
  if not re.match(r"[a-h][1-8] [a-h][1-8]", move):
    return False
  # Check if the player is trying to move their own piece
  if not player_has_piece_at(player, move[:2], board):
    return False
  # Check if the destination square is empty or occupied by an enemy piece
  if player_has_piece_at(player, move[3:], board) and not is_capture(move, board):
    return False
  # Check if the move follows the rules of chess for the piece being moved
  if not is_legal_chess_move(move, player, board):
    return False
  # If all checks pass, the move is valid
  return True

def player_has_piece_at(player, square, board):
  # Get the row and column of the square
  row = ord(square[0]) - ord("a")
  col = int(square[1]) - 1
  # Check if the square is occupied by a piece belonging to the player
  if player == "white":
    return board[row][col].isupper()
  else:
    return board[row][col].islower()

def is_capture(move, board):
  # Check if the destination square is occupied by an enemy piece
  return player_has_piece_at("white" if move[:2] < move[3:] else "black", move[3:], board)

def is_legal_chess_move(move, player, board):
  # Implement the rules of chess for each piece type here
  return True  # Placeholder

board = [["r", "n", "b", "q", "k", "b", "n", "r"],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
]
