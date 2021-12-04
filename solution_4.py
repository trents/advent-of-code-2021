''' Advent of Code 2021 Day 4 solution '''

def check_off_number(board, number):
    """ Checks for a given number on a board.  If it's found, checks it off. """
    for rcount, row in enumerate(board):
        for ccount, col in enumerate(row):
            if col == number:
                board[rcount][ccount] = "*"
    return board

def is_winner(board):
    """ Checks to see if a board contains a winning pattern. """

    return_value = False

    # Check rows
    for row in board:
        if row[0] == "*" and row[1] == "*" and row[2] == "*" and row[3] == "*" and row[4] == "*":
            return_value = True

    # Check cols
    for count in range(5):
        if (board[0][count] == "*" and board[1][count] == "*" and board[2][count] == "*" and
            board[3][count] == "*" and board[4][count] == "*"):
            return_value = True

    return return_value

def board_value(board):
    """ Calculates the value of a given board. """

    bvalue = 0

    for row in board:
        for item in row:
            if item != "*":
                bvalue += int(item)

    return bvalue

def main():
    """ driver for solution to puzzle """
    with open('4.txt') as file:
        drawn = file.readline().strip().split(",")
        result = file.readline()
        lines = file.readlines()

    num_boards = (len(lines) + 1) // 6
    boards = []

    for count in range(num_boards):
        boards.append([[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],[0, 0, 0, 0, 0]])

    for count, line in enumerate(lines):
        cur_board = count // 6
        cur_board_row = count % 6
        board_row = line.strip().split()

        if cur_board_row != 5:
            boards[cur_board][cur_board_row] = board_row
        else:
            continue

    # determine first winner, for 4a

    result = 0

    winner = False

    for number in drawn:
        if winner:
            break
        for count, board in enumerate(boards):
            if not winner:
                boards[count] = check_off_number(board, number)
                if is_winner(boards[count]):
                    result = board_value(boards[count]) * int(number)
                    winner = True
            else:
                break

    print("4a -> ",result)

    # determine last linner, for 4b

    result = 0

    for number in drawn:
        if len(boards) == 1:
            break
        temp_boards = []
        for board in boards:
            board = check_off_number(board, number)
            if not is_winner(board):
                temp_boards.append(board)
            else:
                continue
        boards = temp_boards

    for number in drawn:
        boards[0] = check_off_number(boards[0], number)
        if is_winner(boards[0]):
            break

    result = board_value(boards[0]) * int(number)

    print("4b -> ",result)

if __name__ == "__main__":
    main()
