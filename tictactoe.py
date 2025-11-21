print("Welcome to Tic-Tac-Toe")

print("Here is our playing board:")

# Constants
EMPTY_CELL = ' '

# The play board
play_board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]


# prints the board
def print_board():
  for i in range(3):
    for j in range(3):
      print("[" + play_board[i][j] + "]",
            end="")  # print elements without new line
    print()  # print empty line after each row
  print('--------------')


def play(player, x, y):
  if play_board[x][y] == EMPTY_CELL:
    play_board[x][y] = player
    print_board()
  else:
    print("Position is not empty")


# checks the different scenarios of wining
# NOTE: Not all scneaiors are tested and the draw scenaio is not implemented as well.
def check_win():
  for row in play_board:  # each row separately
    # check all rows first
    if row[0] != ' ' and row[0] == row[1] == row[
      2]:  # If all the items in row are the same
      return row[0]  # X or O
  
  for i in range(3):  # check all columns
    if play_board[0][i] != ' ' and play_board[0][i] == play_board[1][i] == \
            play_board[2][i]:
      return play_board[0][i]
      # check cross items
  if play_board[0][0] == play_board[1][1] == play_board[2][2] != EMPTY_CELL:
    if play_board[0][0] == 'X':
      return "X"
    else:
      return "O"
  
  if play_board[2][0] == play_board[1][1] == play_board[0][2] != EMPTY_CELL:
    if play_board[2][0] == 'X':
      return "X"
    else:
      return "O"


print_board()

while True:
  # player X
  player_x_position = input('X, Enter play position (i.e. 0,1): ')
  pos_x = int(player_x_position.split(',')[0])
  pos_y = int(player_x_position.split(',')[1])
  
  play('X', pos_x, pos_y)
  
  if (check_win()):
    print("X wins")
    break;
  
  # player O
  # another shorter way to get the input
  pos_x, pos_y = input('O, Enter play position (i.e. 0,1): ').split(',')
  
  play('O', int(pos_x), int(pos_y))
  
  if (check_win()):
    print("O wins")
    break;
