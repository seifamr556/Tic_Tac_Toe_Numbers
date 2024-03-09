# Program: This is Tic Tac Toe by numbers game in this game the player who reached the sum 15 horizontally, vertically or diagonally ein
# Author: Seif Eldeen Amr Abd Al-Mawgod (No section) (20230184)
# Version: 1.0v
# Date: 3/3/2024

# function to print the game board
def print_board(board):
    for row in board:
        print(":".join(row))
        print("-" * 14)

# check if the Vertically, Horizontally or Diagonally numbers have sum = 15
def checkWinner(board):
    total_list = []
    total1_list = []
    total2_list = []
    total3_list = []
    # loop on the game board
    for x in range(3):
        for y in range(3):
            # check Horizontally sum
            if board[x][y] != ' * ':
                total_list.append(int(board[x][y]))
            sum = 0
            for i in total_list:
                sum += i
            # check if sum == 15 and the number of numbers = 3
            if sum == 15 and len(total_list) == 3:
                return True
            # check Vertically Sum
            if board[y][x] != ' * ':
                total1_list.append(int(board[y][x]))
            sum1 = 0
            for j in total1_list:
                sum1 += j
            # check if sum == 15 and the number of numbers = 3
            if sum1 == 15 and len(total1_list) == 3:
                return True
        total_list.clear()
        total1_list.clear()

    # check Diagonally sum
    for i in range(3):
        if board[i][i] != ' * ':
            total2_list.append(int(board[i][i]))
    sum = 0
    for num in total2_list:
        sum += num

    if sum == 15 and len(total2_list) == 3:
        return True

    k = 0
    # check Diagonally sum
    for j in range(2, -1, -1):
        if board[k][j] != ' * ':
            total3_list.append(int(board[k][j]))
        k += 1

    sum1 = 0
    for num in total3_list:
        sum1 += num
    if sum1 == 15 and len(total3_list) == 3:
        return True
    return False


def main():
    board = [
        [' * ', ' * ', ' * '],
        [' * ', ' * ', ' * '],
        [' * ', ' * ', ' * ']
    ]
    # Declare the players lists
    player1_list = [1, 3, 5, 7, 9]
    player2_list = [0, 2, 4, 6, 8]
    # game loop[
    while True:
        # ask user to play or exit
        print("Welcome in Tic Tac Toe numbers game:\n 1) Play\n 2) Exit")
        choice = input("Enter your choice from (1/2): ")
        current_player = 1
        if choice == "1":
            print_board(board)
            while True:
                # take player 1 move and check if it in the list and integer or not
                while True:
                    print("Player1 list: ", player1_list)
                    try:
                        player_move = int(input(f"Player {current_player}: Select number from your list: "))
                        if player_move not in player1_list:
                            print("Please select a number from the list")
                            continue
                        else:
                            player1_list.remove(player_move)
                            break
                    except ValueError:
                        print("Please enter a valid numbers")

                # take player 1 move position and check if it in the board and integer or not
                while True:
                    try:
                        player_row = int(input(f"Player {current_player}: Enter row number (1\\2\\3): "))
                        player_column = int(input(f"Player {current_player}: Enter column number (1\\2\\3): "))
                    except ValueError:
                        print("Please enter a valid numbers")
                        continue
                    if player_row > 3 or player_row < 1 or player_column > 3 or player_column < 1:
                        print("Please enter a valid row and column.")
                        continue
                    if board[player_row - 1][player_column - 1] != ' * ':
                        print("This position has a number.Try again")
                        continue
                    else:
                        board[player_row - 1][player_column - 1] = f" {str(player_move)} "
                        break

                # check if player 1 win
                print_board(board)
                if checkWinner(board):
                    print(f"\n* Player {current_player} win *")
                    print("\nDo you want play again ?")
                    main()

                checkDraw = False
                for i in range(3):
                    for j in range(3):
                        if board[i][j] != ' * ':
                            checkDraw = True
                        else:
                            checkDraw = False
                            break
                if checkDraw:
                    print("It's a draw")
                    break

                current_player = 2
                print("Player2 list: ", player2_list)

                # take player 2 move and check if it in the list and integer or not
                while True:
                    try:
                        player_move = int(input(f"Player {current_player}: Select number from your list: "))
                        if player_move not in player2_list:
                            print("Please select a number from the list")
                            continue
                        else:
                            player2_list.remove(player_move)
                            break
                    except ValueError:
                        print("Please enter a valid numbers")

                # take player 2 move position and check if it in the board and integer or not
                while True:
                    try:
                        player_row = int(input(f"Player {current_player}: Enter row number (1\\2\\3): "))
                        player_column = int(input(f"Player {current_player}: Enter column number (1\\2\\3): "))
                    except ValueError:
                        print("Please enter a valid numbers")
                        continue
                    if player_row > 3 or player_row < 1 or player_column > 3 or player_column < 1:
                        print("Please enter a valid row and column.")
                        continue
                    if board[player_row - 1][player_column - 1] != ' * ':
                        print("This position has a number.Try again")
                        continue
                    else:
                        board[player_row - 1][player_column - 1] = f" {str(player_move)} "
                        break

                # check if player 2 win
                print_board(board)
                if checkWinner(board):
                    print(f"\n* Player {current_player} win *")
                    print("\nDo you want play again ?")
                    main()

                checkDraw = False
                for i in range(3):
                    for j in range(3):
                        if board[i][j] != ' * ':
                            checkDraw = True
                        else:
                            checkDraw = False
                            break
                if checkDraw:
                    print("It's a draw")
                    break

        elif choice == "2":
            # exit the game
            exit()
        else:
            print("Enter a valid choice.Try again")


main()