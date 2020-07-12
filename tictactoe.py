def check_win(board):
    def check_equal(n1, n2, n3, value):
        return board[n1] == board[n2] == board[n3] == value
    if (
       check_equal(0,1,2,'X') or
       check_equal(3,4,5,'X') or
       check_equal(6,7,8,'X') or
       check_equal(0,3,6,'X') or
       check_equal(1,4,7,'X') or
       check_equal(2,5,8,'X') or
       check_equal(0,4,8,'X') or
       check_equal(2,4,6,'X')
       ):
        return 'X'
    elif (
       check_equal(0,1,2,'O') or
       check_equal(3,4,5,'O') or
       check_equal(6,7,8,'O') or
       check_equal(0,3,6,'O') or
       check_equal(1,4,7,'O') or
       check_equal(2,5,8,'O') or
       check_equal(0,4,8,'O') or
       check_equal(2,4,6,'O')
       ):
        return 'O'
    return None
def dead_end(board):
    return '' not in board
board = [
        '','','',
        '','','',
        '','','',
        ]
turn = 'O'
def print_board(board):
    def print_tile(tile):
        if board[tile] == '':
            return tile
        else:
            return board[tile]
    print(f" {print_tile(0)} | {print_tile(1)} | {print_tile(2)} \n {print_tile(3)} | {print_tile(4)} | {print_tile(5)} \n {print_tile(6)} | {print_tile(7)} | {print_tile(8)}")


if __name__ == '__main__':
    print("Tic Tac Toe: ")
    print("2 Player Mode")
    while (not dead_end(board) or check_win(board) is None ):
        print(f"Turn {turn} ")
        print_board(board)
        pos = int(input("Position: "))
        if pos >= 9:
            print("Invalid position")
            continue
        if board[pos] == '':
            board[pos] = turn
            if turn == 'O':
                turn = 'X'
            else:
                turn = 'O'
        else:
            print("Sorry it is not blank")
            continue
        if dead_end(board):
            print("Stalemate. Run this to try again")
            break
        winner = check_win(board)
        if winner == 'O':
            print("O win. Let's celebrate")
            break
        elif winner == 'X':
            print("X win. Extremely easy ya.")
            break



