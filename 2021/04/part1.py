import os, sys

input = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as in_file:
    input = in_file.readlines()

draws = input[0].split(',')

boards = []

picks = []

current_board = []

current_picks = [[False, False, False, False, False], [False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False] ]
row=None
for i in range(1, len(input)):
    line = input[i].strip()
    if len(line) == 0:
        if len(current_board) > 0:
            boards.append(current_board)
            current_board = []

            picks.append([[False, False, False, False, False], [False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False] ])
        continue
    
    row = line.split() 
    current_board.append(row)

boards.append(current_board)
picks.append([[False, False, False, False, False], [False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False] ])


print ("GOMBALEYOO\n\n\n\n")

def debug():
    for i in range(len(boards)):
        print(boards[i])
        print(picks[i])
        print("\n")


def did_board_win(board_picks):
    for i in range(5):
        row_full = True
        for j in range(5):
            if board_picks[i][j] == False:
                row_full = False
                break

        if row_full: 
            print("correct 1")
            return True

    for i in range(5):
        row_full = True
        for j in range(5):
            if board_picks[j][i] == False:
                row_full = False
                break

        if row_full: 
            print("correct 2")
            return True

    diag_full = True
    for i in range(5):
        
        if board_picks[i][j] == False:
            diag_full = False
            break

    if  diag_full == True:
        print("correct 3")
        return True

    diag_full = True
    for i in range(5):
        
        if board_picks[i][4-j] == False:
            diag_full = False
            break

    if  diag_full == True:
        print("correct 4")
        return True

    return False


def calculate_board(board, bpicks, draw):
    sum = 0

    for i in range(5):
        for j in range(5):
            if bpicks[i][j] == False:
                sum += int(board[i][j])

    print(sum * int(draw))



def process_draw(draw):
    for board_i in range(len(boards)):
        for i in range(5):
            for j in range(5):
                if boards[board_i][i][j].strip() == draw.strip():
                    picks[board_i][i][j] = True


                    # debug()
                    # print("*****************************")
                    if did_board_win(picks[board_i]):
                        calculate_board(boards[board_i], picks[board_i], draw)
                        exit(0)




def part_1():
    for draw in draws:
        print("#####################################")
        print(draw)
        process_draw(draw)



def part_2():
    pass


part_1()
part_2() 