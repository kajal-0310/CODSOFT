import random

board = [" " for i in range(9)]

def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])


def check_win(player):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def player_move():
    move = int(input("Enter position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move. Try again.")


def ai_move():
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"


while True:
    print_board()

    player_move()

    if check_win("X"):
        print_board()
        print("You win!")
        break

    ai_move()

    if check_win("O"):
        print_board()
        print("AI wins!")
        break

    if " " not in board:
        print_board()
        print("Draw!")
        break