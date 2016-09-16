"""
A basic tic tac toe game.
"""

OPTIONS = ['O', 'X']


def show_board(board):
    """ Show the game board to the players. """
    for line in board:
        print(line)


def take_input(board, player):
    """ Take input and make sure it's not already filled. """
    inp = input('Choose a position for ' + player + ' as x,y co-ordinates. e.g. 0 1: ')

    # Map is a special function which applies another fucntion to every item in a list.
    # In this case we are turning all items in the split list of co-ordinates into
    # integers (they are originally strings due to inputs behaviour).
    x, y = map(int, inp.split())

    if board[x][y] == ' ':
        board[x][y] = player

    else:
        print('That position is already used, please try again.')

        # Calling a function inside itself is called recursion. It's useful if
        # you need to repeat a function until you get a good result.
        board = take_input(board, player)

    return board


def check_victory(board):
    """ Check if a player has won the game. """

    for idx in range(3):
        if board[idx][0] != ' ' and board[idx][0] == board[idx][1] == board[idx][2]:
            # This checks if all items in each horizontal row is complete.
            print('Victory to ' + board[idx][0])
            return True
        elif board[0][idx] != ' ' and board[0][idx] == board[1][idx] == board[2][idx]:
            # This checks if all the items in each vertical column is complete.
            print('Victory to ' + board[0][idx])
            return True

    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        # This checks if the left to right diagonal is complete.
        print('Victory to ' + board[0][0])
        return True
    elif board[2][0] != ' ' and board[2][0] == board[1][1] == board[0][2]:
        # This checks if the right to left diagonal is complete.
        print('Victory to ' + board[2][0])
        return True

    return False


def main():
    """ The main function to manage the game. """
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    counter = 0

    while not check_victory(board):
        # This is called the game loop. It keeps the game running until it is finished.
        # On every iteration of the loop we check to see if a player has won.

        # Show the board to the player.
        show_board(board)

        # Take input to add a new token.
        board = take_input(board, OPTIONS[counter % 2])

        counter += 1

if __name__ == '__main__':
    main()
